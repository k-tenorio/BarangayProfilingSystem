# controller/GenerateReport/generateReportController_Secretary.py

from PyQt6 import QtWidgets, QtCore
from view.GenerateReport.generateReport import Ui_ViewPopulation
from PyQt6.QtCore import pyqtSignal
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from model.db_connections import connect_db
import mysql.connector
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Spacer, HRFlowable, Paragraph, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from datetime import datetime


# ──────────────────────────────────────────────────────────────────────────────
# Logout Dialog
# ──────────────────────────────────────────────────────────────────────────────
class LogoutConfirmDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Logout Confirmation")
        self.setFixedSize(300, 150)
        self.setStyleSheet("""
            QDialog { background-color: white; border: 2px solid #dcdcdc; border-radius: 10px; }
            QLabel  { color: #333333; font-size: 14px; font-weight: bold; }
            QPushButton { background-color: #f0f0f0; border: 1px solid #c0c0c0;
                          border-radius: 5px; padding: 5px 15px; min-width: 70px; }
            QPushButton:hover { background-color: #e0e0e0; }
            #yesButton { background-color: #ff4d4d; color: white; border: none; }
            #yesButton:hover { background-color: #ff3333; }
        """)
        layout = QtWidgets.QVBoxLayout()
        lbl = QtWidgets.QLabel("Are you sure you want to log out?")
        lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl)
        btn_layout = QtWidgets.QHBoxLayout()
        self.yes_button = QtWidgets.QPushButton("Yes")
        self.yes_button.setObjectName("yesButton")
        self.no_button = QtWidgets.QPushButton("No")
        btn_layout.addWidget(self.yes_button)
        btn_layout.addWidget(self.no_button)
        layout.addLayout(btn_layout)
        self.setLayout(layout)
        self.yes_button.clicked.connect(self.accept)
        self.no_button.clicked.connect(self.reject)


# ──────────────────────────────────────────────────────────────────────────────
# Who-Registered Dialog — sorting, limit, complete resident info
# ──────────────────────────────────────────────────────────────────────────────
class WhoRegisteredDialog(QtWidgets.QDialog):
    def __init__(self, residents: list, period_label: str, parent=None):
        super().__init__(parent)
        self.all_residents = residents          # full unfiltered list
        self.residents = list(residents)        # working (sorted/limited) list
        self.setWindowTitle(f"Residents Registered — {period_label}")
        self.resize(1200, 600)

        main_layout = QtWidgets.QVBoxLayout(self)

        # Title
        title = QtWidgets.QLabel(f"<b>{len(residents)} resident(s) registered — {period_label}</b>")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:13px; margin-bottom:4px;")
        main_layout.addWidget(title)

        # ── Controls row: Sort + Limit ─────────────────────────────────
        controls_layout = QtWidgets.QHBoxLayout()

        sort_label = QtWidgets.QLabel("Sort:")
        sort_label.setStyleSheet("font-weight: bold;")
        controls_layout.addWidget(sort_label)

        self.sort_combo = QtWidgets.QComboBox()
        self.sort_combo.addItems(["Default (Date Registered)", "A–Z (Name)", "Z–A (Name)"])
        self.sort_combo.setFixedWidth(220)
        controls_layout.addWidget(self.sort_combo)

        controls_layout.addSpacing(20)

        limit_label = QtWidgets.QLabel("Show:")
        limit_label.setStyleSheet("font-weight: bold;")
        controls_layout.addWidget(limit_label)

        self.limit_combo = QtWidgets.QComboBox()
        self.limit_combo.addItems(["All", "1", "10", "15", "Custom"])
        self.limit_combo.setFixedWidth(100)
        controls_layout.addWidget(self.limit_combo)

        self.custom_limit_spin = QtWidgets.QSpinBox()
        self.custom_limit_spin.setMinimum(1)
        self.custom_limit_spin.setMaximum(99999)
        self.custom_limit_spin.setValue(20)
        self.custom_limit_spin.setFixedWidth(80)
        self.custom_limit_spin.setVisible(False)
        controls_layout.addWidget(self.custom_limit_spin)

        self.apply_controls_btn = QtWidgets.QPushButton("Apply")
        self.apply_controls_btn.setFixedWidth(70)
        controls_layout.addWidget(self.apply_controls_btn)

        controls_layout.addStretch()

        self.showing_label = QtWidgets.QLabel(f"Showing: {len(residents)}")
        self.showing_label.setStyleSheet("font-weight: bold;")
        controls_layout.addWidget(self.showing_label)

        main_layout.addLayout(controls_layout)

        # ── Split: left list + right details ──────────────────────────
        content_layout = QtWidgets.QHBoxLayout()

        # Left: table
        left_layout = QtWidgets.QVBoxLayout()
        self.table = QtWidgets.QTableWidget(len(residents), 5)
        self.table.setHorizontalHeaderLabels(["#", "Full Name", "Sex", "Date of Birth", "Date Registered"])
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setAlternatingRowColors(True)
        left_layout.addWidget(self.table)
        content_layout.addLayout(left_layout, 2)

        # Right: complete resident info panel
        right_layout = QtWidgets.QVBoxLayout()

        right_title = QtWidgets.QLabel("Resident Information")
        right_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        right_title.setStyleSheet("font-size:13px; margin-bottom:4px;")
        right_layout.addWidget(right_title)

        # Scrollable details area
        self.details_scroll = QtWidgets.QScrollArea()
        self.details_scroll.setWidgetResizable(True)
        self.details_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.details_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.details_scroll.setStyleSheet("QScrollArea { border: none; }")

        self.details_frame = QtWidgets.QWidget()
        form_layout = QtWidgets.QFormLayout(self.details_frame)
        form_layout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        form_layout.setSpacing(6)

        self.details = {}
        # Complete resident info fields
        detail_fields = [
            ("Full Name", "name"),
            ("Sex", "sex"),
            ("Date of Birth", "dob"),
            ("Date Registered", "created_at"),
            ("Civil Status", "civil_status"),
            ("Nationality", "nationality"),
            ("Religion", "religion"),
            ("Blood Type", "blood_type"),
            ("Purok", "purok"),
            ("Household ID", "house_id"),
            ("Street / Address", "street"),
            ("Place of Birth", "place_of_birth"),  # ← Fixed
            ("Height (cm)", "height"),  # ← Fixed
            ("Weight (kg)", "weight"),  # ← Fixed
            ("Father's Name", "father_name"),  # ← Fixed
            ("Mother's Name", "mother_name"),  # ← Fixed
            ("Contact No.", "contact_number"),
            ("Email", "email"),
            ("Emergency Contact", "emergency_contact"),  # ← Fixed
            ("PWD", "is_pwd"),
            ("Deceased", "is_deceased"),
        ]

        for label_text, key in detail_fields:
            lbl = QtWidgets.QLabel(f"<b>{label_text}:</b>")
            val = QtWidgets.QLabel("—")
            val.setWordWrap(True)
            form_layout.addRow(lbl, val)
            self.details[key] = val

        self.details_scroll.setWidget(self.details_frame)
        right_layout.addWidget(self.details_scroll)
        content_layout.addLayout(right_layout, 1)

        main_layout.addLayout(content_layout)

        # Close button
        close_btn = QtWidgets.QPushButton("Close")
        close_btn.setFixedWidth(100)
        close_btn.setStyleSheet(
            "QPushButton { background-color:#3498db; color:white; border:none; border-radius:5px; padding:6px; }"
            "QPushButton:hover { background-color:#2980b9; }"
        )
        close_btn.clicked.connect(self.accept)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(close_btn)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

        # Connections
        self.table.selectionModel().currentRowChanged.connect(self._on_row_selected)
        self.limit_combo.currentTextChanged.connect(self._on_limit_changed)
        self.apply_controls_btn.clicked.connect(self._apply_controls)

        # Initial populate
        self._populate_table(self.residents)
        self._clear_details()

    # ── Controls ──────────────────────────────────────────────────────
    def _on_limit_changed(self, text):
        self.custom_limit_spin.setVisible(text == "Custom")

    def _apply_controls(self):
        # 1. Sort
        sort_mode = self.sort_combo.currentText()
        data = list(self.all_residents)
        if sort_mode == "A–Z (Name)":
            data.sort(key=lambda r: r.get("name", "").lower())
        elif sort_mode == "Z–A (Name)":
            data.sort(key=lambda r: r.get("name", "").lower(), reverse=True)
        # Default: original order (Date Registered DESC from DB)

        # 2. Limit
        limit_text = self.limit_combo.currentText()
        if limit_text == "All":
            pass
        elif limit_text == "Custom":
            n = self.custom_limit_spin.value()
            data = data[:n]
        else:
            data = data[:int(limit_text)]

        self.residents = data
        self._populate_table(data)
        self.showing_label.setText(f"Showing: {len(data)}")
        self._clear_details()

    def _populate_table(self, data):
        self.table.setRowCount(len(data))
        for i, r in enumerate(data):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(r.get("name", "")))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(r.get("sex", "")))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(r.get("dob", ""))))
            self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(r.get("created_at", ""))))

    # ── Details panel ─────────────────────────────────────────────────
    def _on_row_selected(self, current, previous):
        if current.isValid():
            self._update_details(current.row())
        else:
            self._clear_details()

    def _update_details(self, row_idx):
        r = self.residents[row_idx]
        for key, val_label in self.details.items():
            value = r.get(key, "—")
            if value is None or value == "":
                value = "—"
            if hasattr(value, "strftime"):
                value = value.strftime("%Y-%m-%d")
            val_label.setText(str(value))

    def _clear_details(self):
        for val_label in self.details.values():
            val_label.setText("—")


# ──────────────────────────────────────────────────────────────────────────────
# Main Controller
# ──────────────────────────────────────────────────────────────────────────────
class GenerateReportController(QtWidgets.QDialog):
    logout_requested = pyqtSignal()
    dashboard_requested = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ViewPopulation()
        self.ui.setupUi(self)
        self.setWindowTitle("Generate Reports")
        self.ui.home_Button.setText("GENERATE REPORT")
        self.ui.secretary_Label_2.setText("SECRETARY")

        # PDF button injected into scroll content bottom area
        self._inject_pdf_button()

        # Timer
        self.update_date_time()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)

        # Cached who-registered data (full details)
        self._who_registered = []
        self._period_label = "All Time"

        self.generated_by = "Secretary"

        self._connect_sidebar()
        self._connect_filters()
        self.load_all_data()
        self._setup_table_style()

    # ── PDF button injection ───────────────────────────────────────────
    def _inject_pdf_button(self):
        btn_frame = QtWidgets.QFrame(parent=self.ui.scrollContent)
        btn_frame.setGeometry(QtCore.QRect(10, 720, 1110, 40))
        btn_frame.setStyleSheet("background:transparent; border:none;")

        layout = QtWidgets.QHBoxLayout(btn_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()

        self.generate_pdf_button = QtWidgets.QPushButton("GENERATE PDF REPORT")
        self.generate_pdf_button.setFixedSize(230, 35)
        self.generate_pdf_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60; color: white; border: none;
                border-radius: 6px; font-size: 12px; font-weight: bold;
            }
            QPushButton:hover   { background-color: #219a52; }
            QPushButton:pressed { background-color: #1e8449; }
        """)
        self.generate_pdf_button.clicked.connect(self.generate_pdf_report)
        layout.addWidget(self.generate_pdf_button)
        btn_frame.show()

    # ── Sidebar connections ────────────────────────────────────────────
    def _connect_sidebar(self):
        self.ui.home_Button_3.clicked.connect(self.go_to_dashboard)
        self.ui.viewPopulation_Button_2.clicked.connect(self.open_view_population)
        self.ui.register_Button_2.clicked.connect(self.open_register_resident)
        self.ui.generateReports_Button_2.clicked.connect(self.refresh_report)
        self.ui.logout_Button_2.clicked.connect(self.handle_logout)

    # ── Filter connections ─────────────────────────────────────────────
    def _connect_filters(self):
        self.ui.dateRangeCombo.currentTextChanged.connect(self._on_date_range_changed)
        self.ui.applyFilterBtn.clicked.connect(self._apply_filters)
        self.ui.viewWhoRegisteredBtn.clicked.connect(self._show_who_registered)

    def _on_date_range_changed(self, text):
        is_custom = (text == "Custom Range")
        self.ui.dateFromLabel.setVisible(is_custom)
        self.ui.dateFromEdit.setVisible(is_custom)
        self.ui.dateToLabel.setVisible(is_custom)
        self.ui.dateToEdit.setVisible(is_custom)

    def _apply_filters(self):
        self.load_all_data()

    # ── Date range helpers ────────────────────────────────────────────
    def _get_date_filter_sql(self) -> tuple:
        period = self.ui.dateRangeCombo.currentText()
        if period == "Today":
            return "DATE(created_at) = CURDATE()", []
        elif period == "This Week":
            return "YEARWEEK(created_at, 1) = YEARWEEK(CURDATE(), 1)", []
        elif period == "This Month":
            return "MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())", []
        elif period == "This Year":
            return "YEAR(created_at) = YEAR(CURDATE())", []
        elif period == "Custom Range":
            d_from = self.ui.dateFromEdit.date().toString("yyyy-MM-dd")
            d_to = self.ui.dateToEdit.date().toString("yyyy-MM-dd")
            return "DATE(created_at) BETWEEN %s AND %s", [d_from, d_to]
        else:
            return "1=1", []

    def _get_period_label(self) -> str:
        period = self.ui.dateRangeCombo.currentText()
        if period == "Custom Range":
            return (f"{self.ui.dateFromEdit.date().toString('MMM dd, yyyy')} – "
                    f"{self.ui.dateToEdit.date().toString('MMM dd, yyyy')}")
        return period

    # ── Master loader ─────────────────────────────────────────────────
    def load_all_data(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            self._load_population_summary(cursor)
            self._load_registration_analytics(cursor)
            self._load_who_registered(cursor)
            self._load_purok_distribution_table(cursor)
            conn.close()
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            self._set_default_values()
        except Exception as e:
            print(f"Error loading report data: {e}")
            self._set_default_values()

    # ── Population summary (includes Other Gender) ────────────────────
    def _load_population_summary(self, cursor):
        date_sql, params = self._get_date_filter_sql()

        def q(extra_condition="", extra_params=None):
            where_clause = f"is_deceased = 0 AND {date_sql}"
            if extra_condition:
                where_clause += f" AND {extra_condition}"
            cursor.execute(f"SELECT COUNT(*) FROM residents WHERE {where_clause}", params + (extra_params or []))
            result = cursor.fetchone()
            return result[0] if result else 0

        self.ui.totalPopulationNum.setText(str(q()))

        try:
            cursor.execute(f"""
                SELECT COUNT(DISTINCT ra.house_id)
                FROM residents r
                LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
                WHERE ra.house_id IS NOT NULL AND ra.house_id != ''
                AND r.is_deceased = 0 AND {date_sql}
            """, params)
            result = cursor.fetchone()
            self.ui.totalHouseholdNum.setText(str(result[0] if result else 0))
        except:
            self.ui.totalHouseholdNum.setText("0")

        self.ui.menNum.setText(str(q("sex IN ('Male','M','male')")))
        self.ui.womenNum.setText(str(q("sex IN ('Female','F','female')")))

        # Other Gender: not male, not female, not null/empty
        other_gender_count = q(
            "sex NOT IN ('Male','M','male','Female','F','female') AND sex IS NOT NULL AND sex != ''"
        )
        if hasattr(self.ui, 'otherGenderNum'):
            self.ui.otherGenderNum.setText(str(other_gender_count))

        self.ui.seniorsNum.setText(str(q("TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) >= 60")))
        self.ui.adultsNum.setText(str(q("TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 19 AND 59")))
        self.ui.minorsNum.setText(str(q("TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) < 18")))
        self.ui.pwdNum.setText(str(q("is_pwd = 1")))

        self.ui.singleNum.setText(str(q("civil_status = 'Single'")))
        self.ui.marriedNum.setText(str(q("civil_status = 'Married'")))
        self.ui.widowedNum.setText(str(q("civil_status = 'Widowed'")))
        self.ui.separatedNum.setText(str(q("civil_status IN ('Separated','Annulled')")))

        self.ui.filipinoNum.setText(str(q("nationality = 'Filipino'")))
        self.ui.otherNatNum.setText(str(q("nationality != 'Filipino' AND nationality IS NOT NULL")))

        try:
            cursor.execute(f"SELECT COUNT(*) FROM residents WHERE is_deceased = 1 AND {date_sql}", params)
            result = cursor.fetchone()
            self.ui.deceasedNum.setText(str(result[0] if result else 0))
        except:
            self.ui.deceasedNum.setText("0")

    # ── Registration analytics ─────────────────────────────────────────
    def _load_registration_analytics(self, cursor):
        periods = [
            ("DATE(created_at) = CURDATE()", [], "registrationTodayNum"),
            ("YEARWEEK(created_at, 1) = YEARWEEK(CURDATE(), 1)", [], "registrationsWeek_2"),
            ("MONTH(created_at) = MONTH(CURDATE()) AND YEAR(created_at) = YEAR(CURDATE())", [],
             "registrationsMonthNum"),
            ("YEAR(created_at) = YEAR(CURDATE())", [], "registrationsYearNum"),
        ]
        for (cond, p, attr) in periods:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM residents WHERE {cond}", p)
                result = cursor.fetchone()
                getattr(self.ui, attr).setText(str(result[0] if result else 0))
            except:
                getattr(self.ui, attr).setText("0")

    # ── Who registered (fault-tolerant: each table queried separately) ─
    def _load_who_registered(self, cursor):
        date_sql, params = self._get_date_filter_sql()

        try:
            # Main query with all needed tables
            cursor.execute(f"""
                SELECT 
                    r.resident_id,
                    CONCAT(r.first_name, ' ', IFNULL(r.middle_name, ''), ' ', r.last_name) AS name,
                    r.sex,
                    r.date_of_birth AS dob,
                    r.created_at,
                    r.civil_status,
                    r.nationality,
                    r.religion,
                    r.is_pwd,
                    r.is_deceased,
                    r.place_of_birth,
                    ra.purok,
                    ra.house_id,
                    ra.street,
                    rp.blood_type,
                    rp.height_cm AS height,
                    rp.weight_kg AS weight,
                    par.father_name,
                    par.mother_name,
                    rc.contact_number,
                    rc.email,
                    ec.emergency_contact_name AS emergency_contact
                FROM residents r
                LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
                LEFT JOIN resident_physical_info rp ON r.resident_id = rp.resident_id
                LEFT JOIN resident_parents par ON r.resident_id = par.resident_id
                LEFT JOIN resident_contacts rc ON r.resident_id = rc.resident_id
                LEFT JOIN resident_emergency_contacts ec ON r.resident_id = ec.resident_id
                WHERE {date_sql}
                ORDER BY r.created_at DESC
            """, params)

            rows = cursor.fetchall()
        except Exception as e:
            print(f"Error loading who registered: {e}")
            self._who_registered = []
            self.ui.whoRegisteredCount.setText("0 residents")
            return

        self._who_registered = []
        for row in rows:
            self._who_registered.append({
                "resident_id":       row[0],
                "name":              (row[1] or "").strip(),
                "sex":               row[2] or "N/A",
                "dob":               row[3],
                "created_at":        row[4],
                "civil_status":      row[5] or "N/A",
                "nationality":       row[6] or "N/A",
                "religion":          row[7] or "N/A",
                "is_pwd":            "Yes" if row[8] else "No",
                "is_deceased":       "Yes" if row[9] else "No",
                "place_of_birth":    row[10] or "N/A",
                "purok":             row[11] or "N/A",
                "house_id":          row[12] or "N/A",
                "street":            row[13] or "N/A",
                "blood_type":        row[14] or "N/A",
                "height":            f"{row[15]} cm" if row[15] else "N/A",
                "weight":            f"{row[16]} kg" if row[16] else "N/A",
                "father_name":       row[17] or "N/A",
                "mother_name":       row[18] or "N/A",
                "contact_number":    row[19] or "N/A",
                "email":             row[20] or "N/A",
                "emergency_contact": row[21] or "N/A",
            })

        self._period_label = self._get_period_label()
        self.ui.whoRegisteredCount.setText(f"{len(self._who_registered)} residents")

    def _show_who_registered(self):
        dlg = WhoRegisteredDialog(self._who_registered, self._period_label, parent=self)
        dlg.exec()

    # ── Purok distribution table (includes Other Gender) ──────────────
    def _load_purok_distribution_table(self, cursor):
        category = self.ui.filterCategoryCombo.currentText()
        date_sql, date_params = self._get_date_filter_sql()

        try:
            cursor.execute("""
                SELECT DISTINCT ra.purok
                FROM residents r
                JOIN resident_addresses ra ON r.resident_id = ra.resident_id
                WHERE ra.purok IS NOT NULL AND ra.purok != ''
                ORDER BY ra.purok
            """)
            puroks = [row[0] for row in cursor.fetchall()]

            if not puroks:
                self.ui.tableWidget.setColumnCount(0)
                self.ui.tableWidget.setRowCount(0)
                return

            table_data = {}
            blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

            for purok in puroks:
                def pq(extra_cond, extra_params=None, deceased=False):
                    dec_filter = "r.is_deceased = 1" if deceased else "r.is_deceased = 0"
                    p = [purok] + (extra_params or []) + date_params
                    try:
                        cursor.execute(f"""
                            SELECT COUNT(*) FROM residents r
                            JOIN resident_addresses ra ON r.resident_id = ra.resident_id
                            WHERE ra.purok = %s AND {dec_filter}
                            AND {extra_cond} AND {date_sql}
                        """, p)
                        result = cursor.fetchone()
                        return result[0] if result else 0
                    except:
                        return 0

                bt_counts = {}
                for bt in blood_types:
                    try:
                        cursor.execute(f"""
                            SELECT COUNT(*) FROM residents r
                            JOIN resident_addresses ra ON r.resident_id = ra.resident_id
                            JOIN resident_physical_info rp ON r.resident_id = rp.resident_id
                            WHERE ra.purok = %s AND rp.blood_type = %s
                            AND r.is_deceased = 0 AND {date_sql}
                        """, [purok, bt] + date_params)
                        result = cursor.fetchone()
                        bt_counts[bt] = result[0] if result else 0
                    except:
                        bt_counts[bt] = 0

                try:
                    cursor.execute(f"""
                        SELECT COUNT(DISTINCT ra.house_id)
                        FROM residents r
                        JOIN resident_addresses ra ON r.resident_id = ra.resident_id
                        WHERE ra.purok = %s AND ra.house_id IS NOT NULL
                        AND ra.house_id != '' AND r.is_deceased = 0 AND {date_sql}
                    """, [purok] + date_params)
                    result = cursor.fetchone()
                    households = result[0] if result else 0
                except:
                    households = 0

                table_data[purok] = {
                    'male':           pq("r.sex IN ('Male','M','male')"),
                    'female':         pq("r.sex IN ('Female','F','female')"),
                    'other_gender':   pq("r.sex NOT IN ('Male','M','male','Female','F','female') AND r.sex IS NOT NULL AND r.sex != ''"),
                    'total':          pq("1=1"),
                    'seniors':        pq("TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) >= 60"),
                    'adults':         pq("TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) BETWEEN 19 AND 59"),
                    'minors':         pq("TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) < 18"),
                    'filipino':       pq("r.nationality = 'Filipino'"),
                    'other_nat':      pq("r.nationality != 'Filipino' AND r.nationality IS NOT NULL"),
                    'catholic':       pq("r.religion = 'Roman Catholic'"),
                    'other_religion': pq("r.religion != 'Roman Catholic' AND r.religion IS NOT NULL"),
                    'single':         pq("r.civil_status = 'Single'"),
                    'married':        pq("r.civil_status = 'Married'"),
                    'widowed':        pq("r.civil_status = 'Widowed'"),
                    'separated':      pq("r.civil_status IN ('Separated','Annulled')"),
                    'deceased':       pq("1=1", deceased=True),
                    'pwd':            pq("r.is_pwd = 1"),
                    'households':     households,
                    'blood_types':    bt_counts,
                }

            ALL_ROWS = [
                ('Male:',              'male'),
                ('Female:',            'female'),
                ('Other Gender:',      'other_gender'),
                ('Total Population:',  'total'),
                ('Seniors (60+):',     'seniors'),
                ('Adults (19-59):',    'adults'),
                ('Minors (<18):',      'minors'),
                ('Filipino:',          'filipino'),
                ('Other Nationality:', 'other_nat'),
                ('Roman Catholic:',    'catholic'),
                ('Other Religion:',    'other_religion'),
                ('Single:',            'single'),
                ('Married:',           'married'),
                ('Widowed:',           'widowed'),
                ('Separated:',         'separated'),
                ('Deceased:',          'deceased'),
                ('PWD:',               'pwd'),
                ('Households:',        'households'),
            ] + [(f'Blood Type {bt}:', ('blood_type', bt)) for bt in blood_types]

            CATEGORY_MAP = {
                "All Categories": ALL_ROWS,
                "Demographics": [r for r in ALL_ROWS if
                                 r[1] in ('male', 'female', 'other_gender', 'total', 'seniors', 'adults', 'minors',
                                          'pwd', 'deceased', 'households')],
                "Nationality":   [r for r in ALL_ROWS if r[1] in ('filipino', 'other_nat')],
                "Civil Status":  [r for r in ALL_ROWS if r[1] in ('single', 'married', 'widowed', 'separated')],
                "Blood Type":    [r for r in ALL_ROWS if isinstance(r[1], tuple)],
                "Religion":      [r for r in ALL_ROWS if r[1] in ('catholic', 'other_religion')],
                "Age Group":     [r for r in ALL_ROWS if r[1] in ('seniors', 'adults', 'minors')],
            }

            rows = CATEGORY_MAP.get(category, ALL_ROWS)

            self.ui.tableWidget.setColumnCount(len(puroks))
            self.ui.tableWidget.setRowCount(len(rows))

            for i, purok in enumerate(puroks):
                self.ui.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(purok))

            for row_idx, (label, key) in enumerate(rows):
                self.ui.tableWidget.setVerticalHeaderItem(row_idx, QtWidgets.QTableWidgetItem(label))
                for col_idx, purok in enumerate(puroks):
                    if isinstance(key, tuple):
                        value = table_data[purok]['blood_types'][key[1]]
                    else:
                        value = table_data[purok][key]
                    item = QtWidgets.QTableWidgetItem(str(value))
                    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    self.ui.tableWidget.setItem(row_idx, col_idx, item)

        except Exception as e:
            print(f"Error loading purok distribution: {e}")
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(0)

    # ── Table style ───────────────────────────────────────────────────
    def _setup_table_style(self):
        self.ui.tableWidget.setAlternatingRowColors(True)
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(26)
        self.ui.tableWidget.verticalHeader().setMinimumSectionSize(22)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        col_count = self.ui.tableWidget.columnCount()
        if col_count > 0:
            for i in range(col_count):
                self.ui.tableWidget.setColumnWidth(i, 200)

    # ── Defaults ──────────────────────────────────────────────────────
    def _set_default_values(self):
        zero_attrs = [
            'totalPopulationNum', 'totalHouseholdNum', 'menNum', 'womenNum', 'otherGenderNum',
            'seniorsNum', 'adultsNum', 'minorsNum', 'pwdNum',
            'singleNum', 'marriedNum', 'widowedNum', 'separatedNum',
            'filipinoNum', 'otherNatNum', 'deceasedNum',
            'registrationTodayNum', 'registrationsWeek_2',
            'registrationsMonthNum', 'registrationsYearNum',
        ]
        for a in zero_attrs:
            if hasattr(self.ui, a):
                getattr(self.ui, a).setText("0")

    # ── PDF Report (full resident info included) ───────────────────────
    def generate_pdf_report(self):
        try:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"barangay_population_report_{ts}.pdf"
            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                self, "Save PDF Report", filename, "PDF Files (*.pdf)"
            )
            if not file_path:
                return

            doc = SimpleDocTemplate(
                file_path,
                pagesize=landscape(letter),
                rightMargin=0.5 * inch, leftMargin=0.5 * inch,
                topMargin=0.5 * inch, bottomMargin=0.5 * inch,
            )
            elements = []
            styles = getSampleStyleSheet()

            header_style = ParagraphStyle(
                "ReportHeader", parent=styles["Title"],
                fontSize=18, spaceAfter=4, textColor=colors.HexColor("#1a2a3a"),
                alignment=TA_CENTER,
            )
            sub_style = ParagraphStyle(
                "SubTitle", parent=styles["Normal"],
                fontSize=11, textColor=colors.HexColor("#555555"), alignment=TA_CENTER,
            )
            section_style = ParagraphStyle(
                "Section", parent=styles["Heading2"],
                fontSize=13, textColor=colors.HexColor("#1a5276"),
                spaceAfter=6, spaceBefore=12,
            )

            # ── Header ──
            elements.append(Paragraph("BARANGAY POPULATION REPORT", header_style))
            elements.append(Paragraph(
                f"Generated on: {datetime.now().strftime('%B %d, %Y  %I:%M %p')}  |  "
                f"Generated by: {self.generated_by}  |  "
                f"Period Filter: {self._period_label}  |  "
                f"Category Filter: {self.ui.filterCategoryCombo.currentText()}",
                sub_style
            ))
            elements.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#3498db")))
            elements.append(Spacer(1, 10))

            # ── Helper ──
            def _tbl(data, col_widths, header_bg=colors.HexColor("#2C3E50")):
                t = Table(data, colWidths=col_widths)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), header_bg),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#eaf4fb")]),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#b0c0c8")),
                    ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ('LEFTPADDING', (0, 0), (-1, -1), 6),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ]))
                return t

            def ui_val(attr):
                w = getattr(self.ui, attr, None)
                return w.text() if w else "0"

            # ── Population Summary ──
            elements.append(Paragraph("Population Summary", section_style))

            sum_left = [
                ["Metric", "Count"],
                ["Total Population",   ui_val("totalPopulationNum")],
                ["Total Households",   ui_val("totalHouseholdNum")],
                ["Total Men",          ui_val("menNum")],
                ["Total Women",        ui_val("womenNum")],
                ["Other Gender",       ui_val("otherGenderNum")],
                ["Seniors (60+)",      ui_val("seniorsNum")],
                ["Adults (19-59)",     ui_val("adultsNum")],
                ["Minors (<18)",       ui_val("minorsNum")],
                ["PWD",                ui_val("pwdNum")],
                ["Deceased",           ui_val("deceasedNum")],
            ]
            sum_right = [
                ["Civil Status / Nationality", "Count"],
                ["Single",             ui_val("singleNum")],
                ["Married",            ui_val("marriedNum")],
                ["Widowed",            ui_val("widowedNum")],
                ["Separated / Annulled", ui_val("separatedNum")],
                ["Filipino",           ui_val("filipinoNum")],
                ["Other Nationality",  ui_val("otherNatNum")],
            ]

            left_tbl  = _tbl(sum_left,  [2.2 * inch, 1.2 * inch], colors.HexColor("#1a5276"))
            right_tbl = _tbl(sum_right, [2.5 * inch, 1.2 * inch], colors.HexColor("#117a65"))

            combined = Table([[left_tbl, Spacer(0.3 * inch, 1), right_tbl]])
            combined.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')]))
            elements.append(combined)
            elements.append(Spacer(1, 10))

            # ── Registration Analytics ──
            elements.append(Paragraph("Registration Analytics", section_style))
            reg_data = [
                ["Period", "Count"],
                ["Today",               ui_val("registrationTodayNum")],
                ["This Week",           ui_val("registrationsWeek_2")],
                ["This Month",          ui_val("registrationsMonthNum")],
                ["This Year",           ui_val("registrationsYearNum")],
                [f"Selected Period ({self._period_label})", str(len(self._who_registered))],
            ]
            elements.append(_tbl(reg_data, [3 * inch, 1.5 * inch], colors.HexColor("#1f618d")))
            elements.append(Spacer(1, 10))

            # ── Purok Distribution ──
            tw = self.ui.tableWidget
            if tw.rowCount() > 0 and tw.columnCount() > 0:
                elements.append(Paragraph("Purok Distribution", section_style))

                purok_headers = ["Category"]
                for col in range(tw.columnCount()):
                    h = tw.horizontalHeaderItem(col)
                    purok_headers.append(h.text() if h else f"Purok {col + 1}")

                purok_data = [purok_headers]
                for row in range(tw.rowCount()):
                    row_data = []
                    rh = tw.verticalHeaderItem(row)
                    row_data.append(rh.text() if rh else f"Row {row + 1}")
                    for col in range(tw.columnCount()):
                        item = tw.item(row, col)
                        row_data.append(item.text() if item else "0")
                    purok_data.append(row_data)

                n_cols = len(purok_headers)
                first_col_w = 1.5 * inch
                other_col_w = (9.7 * inch - first_col_w) / max(n_cols - 1, 1)
                col_widths = [first_col_w] + [other_col_w] * (n_cols - 1)

                elements.append(_tbl(purok_data, col_widths, colors.HexColor("#117864")))

            # ── Registered residents — full info (next page) ──────────
            if self._who_registered:
                elements.append(PageBreak())
                elements.append(Paragraph(
                    f"Residents Registered — {self._period_label} ({len(self._who_registered)} total)",
                    section_style
                ))

                # Full info table
                who_headers = [
                    "#", "Full Name", "Sex", "Date of Birth", "Date Registered",
                    "Civil Status", "Nationality", "Religion", "Blood Type",
                    "Purok", "Street/Address", "Place of Birth",
                    "Height", "Weight",
                    "Contact No.", "Email", "PWD", "Deceased"
                ]
                who_data = [who_headers]

                for i, r in enumerate(self._who_registered[:200], 1):
                    def _f(key):
                        v = r.get(key, "N/A")
                        if v is None or v == "":
                            return "N/A"
                        if hasattr(v, "strftime"):
                            return v.strftime("%Y-%m-%d")
                        return str(v)

                    who_data.append([
                        str(i),
                        _f("name"),
                        _f("sex"),
                        _f("dob"),
                        _f("created_at"),
                        _f("civil_status"),
                        _f("nationality"),
                        _f("religion"),
                        _f("blood_type"),
                        _f("purok"),
                        _f("street"),
                        _f("place_of_birth"),
                        _f("height"),
                        _f("weight"),
                        _f("contact_number"),
                        _f("email"),
                        _f("is_pwd"),
                        _f("is_deceased"),
                    ])

                if len(self._who_registered) > 200:
                    who_data.append(["...", f"+ {len(self._who_registered) - 200} more residents"] + [""] * 16)

                col_widths_who = [
                    0.25 * inch,   # #
                    1.2 * inch,    # Full Name
                    0.35 * inch,   # Sex
                    0.6 * inch,    # DOB
                    0.65 * inch,   # Date Registered
                    0.55 * inch,   # Civil Status
                    0.55 * inch,   # Nationality
                    0.55 * inch,   # Religion
                    0.4 * inch,    # Blood Type
                    0.4 * inch,    # Purok
                    0.65 * inch,   # Street
                    0.65 * inch,   # Place of Birth
                    0.35 * inch,   # Height
                    0.35 * inch,   # Weight
                    0.8 * inch,    # Father's Name
                    0.8 * inch,    # Mother's Name
                    0.65 * inch,   # Contact
                    0.65 * inch,   # Email
                    0.3 * inch,    # PWD
                    0.35 * inch,   # Deceased
                ]

                # Use smaller font for the full-info table
                full_info_tbl = Table(who_data, colWidths=col_widths_who, repeatRows=1)
                full_info_tbl.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#6c3483")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 6),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#eaf4fb")]),
                    ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor("#b0c0c8")),
                    ('FONTSIZE', (0, 1), (-1, -1), 6),
                    ('LEFTPADDING', (0, 0), (-1, -1), 2),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 2),
                    ('TOPPADDING', (0, 0), (-1, -1), 2),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                    ('WORDWRAP', (0, 0), (-1, -1), True),
                ]))
                elements.append(full_info_tbl)
                elements.append(Spacer(1, 10))

            doc.build(elements)
            QtWidgets.QMessageBox.information(
                self, "Report Generated",
                f"PDF report generated successfully!\n\nSaved to:\n{file_path}"
            )

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self, "Error Generating PDF",
                f"An error occurred while generating the PDF report:\n\n{str(e)}"
            )

    # ── Misc ──────────────────────────────────────────────────────────
    def handle_logout(self):
        if LogoutConfirmDialog(self).exec():
            self.logout_requested.emit()
            self.close()

    def update_date_time(self):
        self.ui.dateTime_Label.setText(datetime.now().strftime("%A, %b %d, %Y | %I:%M:%S %p"))

    def go_to_dashboard(self):
        self.dashboard_requested.emit()
        self.close()

    def refresh_report(self):
        self.load_all_data()
        QtWidgets.QMessageBox.information(self, "Refresh", "Report data refreshed successfully!")

    def open_view_population(self):
        from controller.ViewPopulation.viewPopulationController_Secretary import ViewPopulationController
        self.view_population_window = ViewPopulationController(dashboard_reference=self)
        self.view_population_window.dashboard_requested.connect(self.show)
        self.hide()
        self.view_population_window.show()

    def open_register_resident(self):
        from controller.RegisterResident.registerResidentController_Secretary import RegisterResidentController
        self.hide()
        self.register_window = RegisterResidentController()
        self.register_window.logout_requested.connect(self._child_logout)
        self.register_window.dashboard_requested.connect(self._child_dashboard)
        self.register_window.show()

    def _child_logout(self):
        self.logout_requested.emit()
        self.close()

    def _child_dashboard(self):
        self.dashboard_requested.emit()
        self.close()

    def closeEvent(self, event):
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()
        plt.close('all')
        super().closeEvent(event)


# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    try:
        ctrl = GenerateReportController()
        ctrl.dashboard_requested.connect(lambda: print("Dashboard requested"))
        ctrl.logout_requested.connect(lambda: print("Logout requested"))
        ctrl.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Failed to start: {e}")