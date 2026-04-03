import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QMessageBox, QTableWidgetItem,
    QDialog, QVBoxLayout, QLabel, QLineEdit,
    QComboBox, QCheckBox, QGroupBox, QGridLayout, QDateEdit,
    QDialogButtonBox, QTableWidget, QHeaderView, QHBoxLayout, QWidget
)
from PyQt6.QtCore import QDate, pyqtSignal, Qt
from PyQt6.QtCore import QTimer, QDateTime

from model import resident_model
from view.ViewPopulation.viewPopulation_Secretary import Ui_ViewPopulation


class EditResidentDialog(QDialog):
    def __init__(self, resident_id, parent=None):
        super().__init__(parent)
        self.resident_id = resident_id

        self.setWindowTitle("Edit Resident")
        self.setModal(True)
        self.setFixedSize(800, 600)

        self.init_ui()
        self.load_resident_data()

    def init_ui(self):
        layout = QVBoxLayout()

        # Personal Information Group
        personal_group = QGroupBox("Personal Information")
        personal_layout = QGridLayout()

        self.first_name_input = QLineEdit()
        self.middle_name_input = QLineEdit()
        self.last_name_input = QLineEdit()

        self.sex_combo = QComboBox()
        self.sex_combo = QLineEdit()

        self.date_of_birth_input = QDateEdit()
        self.date_of_birth_input.setCalendarPopup(True)
        self.date_of_birth_input.setMaximumDate(QDate.currentDate())

        self.place_of_birth_input = QLineEdit()
        self.nationality_input = QLineEdit()
        self.nationality_input.setText("Filipino")

        self.religion_input = QLineEdit()

        personal_layout.addWidget(QLabel("First Name:"), 0, 0)
        personal_layout.addWidget(self.first_name_input, 0, 1)
        personal_layout.addWidget(QLabel("Middle Name:"), 0, 2)
        personal_layout.addWidget(self.middle_name_input, 0, 3)
        personal_layout.addWidget(QLabel("Last Name:"), 1, 0)
        personal_layout.addWidget(self.last_name_input, 1, 1)
        personal_layout.addWidget(QLabel("Sex:"), 1, 2)
        personal_layout.addWidget(self.sex_combo, 1, 3)
        personal_layout.addWidget(QLabel("Date of Birth:"), 2, 0)
        personal_layout.addWidget(self.date_of_birth_input, 2, 1)
        personal_layout.addWidget(QLabel("Place of Birth:"), 2, 2)
        personal_layout.addWidget(self.place_of_birth_input, 2, 3)
        personal_layout.addWidget(QLabel("Nationality:"), 3, 0)
        personal_layout.addWidget(self.nationality_input, 3, 1)
        personal_layout.addWidget(QLabel("Religion:"), 3, 2)
        personal_layout.addWidget(self.religion_input, 3, 3)

        personal_group.setLayout(personal_layout)

        # Status Information Group
        status_group = QGroupBox("Status Information")
        status_layout = QGridLayout()

        self.is_deceased_check = QCheckBox("Deceased")
        self.is_pwd_check = QCheckBox("Person with Disability")

        self.blood_type_combo = QComboBox()
        self.blood_type_combo.addItems(["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])

        self.height_input = QLineEdit()
        self.weight_input = QLineEdit()

        self.civil_status_combo = QComboBox()
        self.civil_status_combo.addItems(["Single", "Married", "Widowed", "Separated"])

        status_layout.addWidget(self.is_deceased_check, 0, 0)
        status_layout.addWidget(self.is_pwd_check, 0, 1)
        status_layout.addWidget(QLabel("Blood Type:"), 1, 0)
        status_layout.addWidget(self.blood_type_combo, 1, 1)
        status_layout.addWidget(QLabel("Height (cm):"), 2, 0)
        status_layout.addWidget(self.height_input, 2, 1)
        status_layout.addWidget(QLabel("Weight (kg):"), 2, 2)
        status_layout.addWidget(self.weight_input, 2, 3)
        status_layout.addWidget(QLabel("Civil Status:"), 3, 0)
        status_layout.addWidget(self.civil_status_combo, 3, 1)

        status_group.setLayout(status_layout)

        # Family Information Group
        family_group = QGroupBox("Family Information")
        family_layout = QGridLayout()

        self.father_name_input = QLineEdit()
        self.mother_name_input = QLineEdit()

        family_layout.addWidget(QLabel("Father's Name:"), 0, 0)
        family_layout.addWidget(self.father_name_input, 0, 1, 1, 3)
        family_layout.addWidget(QLabel("Mother's Name:"), 1, 0)
        family_layout.addWidget(self.mother_name_input, 1, 1, 1, 3)

        family_group.setLayout(family_layout)

        # Contact Information Group
        contact_group = QGroupBox("Contact Information")
        contact_layout = QGridLayout()

        self.contact_number_input = QLineEdit()
        self.email_input = QLineEdit()

        self.emergency_contact_name_input = QLineEdit()
        self.emergency_contact_number_input = QLineEdit()

        contact_layout.addWidget(QLabel("Contact Number:"), 0, 0)
        contact_layout.addWidget(self.contact_number_input, 0, 1)
        contact_layout.addWidget(QLabel("Email:"), 0, 2)
        contact_layout.addWidget(self.email_input, 0, 3)
        contact_layout.addWidget(QLabel("Emergency Contact Name:"), 1, 0)
        contact_layout.addWidget(self.emergency_contact_name_input, 1, 1)
        contact_layout.addWidget(QLabel("Emergency Contact Number:"), 1, 2)
        contact_layout.addWidget(self.emergency_contact_number_input, 1, 3)

        contact_group.setLayout(contact_layout)

        # Address Information Group
        address_group = QGroupBox("Address Information")
        address_layout = QGridLayout()

        self.purok_combo = QComboBox()
        puroks = resident_model.get_all_puroks()
        self.purok_combo.addItems(["Select Purok"] + puroks)

        self.street_input = QLineEdit()
        self.house_id_input = QLineEdit()

        address_layout.addWidget(QLabel("Purok:"), 0, 0)
        address_layout.addWidget(self.purok_combo, 0, 1)
        address_layout.addWidget(QLabel("Street:"), 0, 2)
        address_layout.addWidget(self.street_input, 0, 3)
        address_layout.addWidget(QLabel("House ID:"), 1, 0)
        address_layout.addWidget(self.house_id_input, 1, 1)

        address_group.setLayout(address_layout)

        # Buttons
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        # Add all groups to main layout
        layout.addWidget(personal_group)
        layout.addWidget(status_group)
        layout.addWidget(family_group)
        layout.addWidget(contact_group)
        layout.addWidget(address_group)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def load_resident_data(self):
        data = resident_model.get_resident_details(self.resident_id)
        if data:
            self.first_name_input.setText(data['first_name'] or '')
            self.middle_name_input.setText(data['middle_name'] or '')
            self.last_name_input.setText(data['last_name'] or '')

            self.sex_combo.setText(data['sex'] or '')

            if data['date_of_birth']:
                self.date_of_birth_input.setDate(QDate.fromString(str(data['date_of_birth']), "yyyy-MM-dd"))

            self.place_of_birth_input.setText(data['place_of_birth'] or '')
            self.nationality_input.setText(data['nationality'] or 'Filipino')
            self.religion_input.setText(data['religion'] or '')

            self.is_deceased_check.setChecked(bool(data['is_deceased']))
            self.is_pwd_check.setChecked(bool(data['is_pwd']))

            self.blood_type_combo.setCurrentText(data['blood_type'] or '')
            self.height_input.setText(str(data['height_cm']) if data['height_cm'] else '')
            self.weight_input.setText(str(data['weight_kg']) if data['weight_kg'] else '')
            self.civil_status_combo.setCurrentText(data['civil_status'] or 'Single')

            self.father_name_input.setText(data['father_name'] or '')
            self.mother_name_input.setText(data['mother_name'] or '')

            self.contact_number_input.setText(data['contact_number'] or '')
            self.email_input.setText(data['email'] or '')

            self.emergency_contact_name_input.setText(data['emergency_contact_name'] or '')
            self.emergency_contact_number_input.setText(data['emergency_contact_number'] or '')

            if data['purok']:
                index = self.purok_combo.findText(data['purok'])
                if index >= 0:
                    self.purok_combo.setCurrentIndex(index)

            self.street_input.setText(data['street'] or '')
            self.house_id_input.setText(data['house_id'] or '')

    def get_updated_data(self):
        return {
            'first_name': self.first_name_input.text().strip(),
            'middle_name': self.middle_name_input.text().strip(),
            'last_name': self.last_name_input.text().strip(),
            'sex': self.sex_combo.text().strip(),
            'date_of_birth': self.date_of_birth_input.date().toString("yyyy-MM-dd"),
            'place_of_birth': self.place_of_birth_input.text().strip(),
            'nationality': self.nationality_input.text().strip(),
            'religion': self.religion_input.text().strip(),
            'is_deceased': 1 if self.is_deceased_check.isChecked() else 0,
            'is_pwd': 1 if self.is_pwd_check.isChecked() else 0,
            'blood_type': self.blood_type_combo.currentText(),
            'height_cm': self.height_input.text().strip() or None,
            'weight_kg': self.weight_input.text().strip() or None,
            'civil_status': self.civil_status_combo.currentText(),
            'father_name': self.father_name_input.text().strip(),
            'mother_name': self.mother_name_input.text().strip(),
            'contact_number': self.contact_number_input.text().strip(),
            'email': self.email_input.text().strip(),
            'emergency_contact_name': self.emergency_contact_name_input.text().strip(),
            'emergency_contact_number': self.emergency_contact_number_input.text().strip(),
            'purok': self.purok_combo.currentText(),
            'street': self.street_input.text().strip(),
            'house_id': self.house_id_input.text().strip()
        }


class ViewPopulationController(QMainWindow):
    dashboard_requested = pyqtSignal()
    generate_reports_requested = pyqtSignal()
    register_resident_requested = pyqtSignal()

    def __init__(self, dashboard_reference=None):
        super().__init__()
        self.ui = Ui_ViewPopulation()
        self.ui.setupUi(self)

        self.dashboard_reference = dashboard_reference

        self.current_page = 1
        self.rows_per_page = 10
        self.all_current_data = []

        self.current_filters = {
            'sex': 'All',
            'purok': 'All',
            'civil_status': 'All',
            'age_range': 'All'
        }
        self.current_search_keyword = ""
        self.current_sort_by = "ResidentID"
        self.sort_order = "ASC"

        # Connect Navigation
        self.ui.prevButton.clicked.connect(self.prev_page)
        self.ui.nextButton.clicked.connect(self.next_page)

        self.setup_filters()
        self.load_data()

        # Connect side panel buttons
        self.ui.register_Button_2.clicked.connect(self.open_register_resident)
        self.ui.generateReports_Button_2.clicked.connect(self.open_generate_reports)
        self.ui.home_Button_3.clicked.connect(self.go_back_to_dashboard)
        self.ui.logout_Button_2.clicked.connect(self.logout)

        # Connect archive button
        self.ui.viewArchivedButton.clicked.connect(self.show_archived_residents)

        # Connect signals
        self.ui.searchLineEdit.textChanged.connect(self.search_data)
        self.ui.filterSexCombo.currentTextChanged.connect(self.apply_filters)
        self.ui.filterPurokCombo.currentTextChanged.connect(self.apply_filters)
        self.ui.filterCivilStatusCombo.currentTextChanged.connect(self.apply_filters)
        self.ui.filterAgeRangeCombo.currentTextChanged.connect(self.apply_filters)
        self.ui.sortCombo.currentTextChanged.connect(self.sort_data)

        self.ui.sortButton.clicked.connect(self.toggle_sort_order)

        # Set table properties
        self.ui.tableWidget.setColumnCount(7)
        headers = ["ResidentID", "Full Name", "Sex", "Age", "Purok", "Civil Status", "Actions"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget.setColumnWidth(0, 90)  # ResidentID
        self.ui.tableWidget.setColumnWidth(1, 180)  # Full Name
        self.ui.tableWidget.setColumnWidth(2, 70)  # Sex
        self.ui.tableWidget.setColumnWidth(3, 60)  # Age
        self.ui.tableWidget.setColumnWidth(4, 100)  # Purok
        self.ui.tableWidget.setColumnWidth(5, 120)  # Civil Status

        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)
        self.update_datetime()

    def toggle_sort_order(self):
        if self.sort_order == "ASC":
            self.sort_order = "DESC"
            self.ui.sortButton.setText("⬇")
        else:
            self.sort_order = "ASC"
            self.ui.sortButton.setText("⬆")

        self.sort_data()

    def update_datetime(self):
        current = QDateTime.currentDateTime().toString("dddd, MMM d, yyyy | hh:mm:ss AP")
        self.ui.dateTime_Label.setText(current)

    def logout(self):
        from controller.Dashboard.dashboardController_Secretary import LogoutConfirmDialog

        dialog = LogoutConfirmDialog(self)
        if dialog.exec():
            if self.dashboard_reference:
                self.dashboard_reference.logout_requested.emit()
                self.dashboard_reference.close()

            self.close()

    def open_generate_reports(self):
        if self.dashboard_reference and hasattr(self.dashboard_reference, 'show'):
            self.close()
            self.dashboard_reference.show()
        else:
            from controller.GenerateReport.generateReportController_Secretary import GenerateReportController
            self.close()
            self.generate_reports = GenerateReportController()
            self.generate_reports.show()

    def open_register_resident(self):
        if self.dashboard_reference and hasattr(self.dashboard_reference, 'show'):
            self.close()
            self.dashboard_reference.hide()  # Hide generate reports
            from controller.RegisterResident.registerResidentController_Secretary import RegisterResidentController
            self.register_window = RegisterResidentController(parent=self.dashboard_reference)
            self.register_window.dashboard_requested.connect(self.dashboard_reference.show)
            self.register_window.show()
        else:
            from controller.RegisterResident.registerResidentController_Secretary import RegisterResidentController
            self.close()
            self.register_window = RegisterResidentController()
            self.register_window.show()

    def go_back_to_dashboard(self):
        if self.dashboard_reference:
            self.dashboard_reference.show()
        self.close()

    def setup_filters(self):
        # Get all puroks for filter
        puroks = resident_model.get_all_puroks()
        self.ui.filterPurokCombo.clear()
        self.ui.filterPurokCombo.addItems(["All"] + puroks)

        # Set default values
        self.ui.filterSexCombo.addItems(["All", "Male", "Female"])
        self.ui.filterCivilStatusCombo.addItems(["All", "Single", "Married", "Widowed", "Separated"])
        self.ui.filterAgeRangeCombo.addItems(["All", "0-17", "18-59", "60+"])
        self.ui.sortCombo.addItems(["ResidentID", "Full Name", "Age", "Purok"])

    # LOAD
    def load_data(self):
        self.all_current_data = resident_model.get_all_residents()
        self.current_page = 1
        self.update_display()

    def refresh_data(self):
        # Start with all residents
        data = resident_model.get_all_residents()

        # Apply filters
        data = self._apply_filters_to_data(data)

        # Apply search
        if self.current_search_keyword:
            data = self._apply_search_to_data(data, self.current_search_keyword)

        # Apply sort
        data = self._apply_sort_to_data(data)

        self.all_current_data = data
        self.current_page = 1
        self.update_display()

    def _apply_filters_to_data(self, data):
        filtered_data = []

        for resident in data:
            resident_id, full_name, sex, age, purok, civil_status, address = resident

            sex_match = (self.current_filters['sex'] == 'All' or
                         sex == self.current_filters['sex'])

            purok_match = (self.current_filters['purok'] == 'All' or
                           purok == self.current_filters['purok'])

            civil_match = (self.current_filters['civil_status'] == 'All' or
                           civil_status == self.current_filters['civil_status'])

            age_match = True
            if self.current_filters['age_range'] != 'All':
                if self.current_filters['age_range'] == '0-17':
                    age_match = 0 <= age <= 17
                elif self.current_filters['age_range'] == '18-59':
                    age_match = 18 <= age <= 59
                elif self.current_filters['age_range'] == '60+':
                    age_match = age >= 60

            if sex_match and purok_match and civil_match and age_match:
                filtered_data.append(resident)

        return filtered_data

    def _apply_search_to_data(self, data, keyword):
        if not keyword:
            return data

        keyword = keyword.lower()
        filtered_data = []

        for resident in data:
            resident_id, full_name, sex, age, purok, civil_status, address = resident

            if (keyword in full_name.lower() or
                    keyword in str(resident_id) or
                    keyword in purok.lower()):
                filtered_data.append(resident)

        return filtered_data

    def _apply_sort_to_data(self, data):
        if not data:
            return data

        reverse = (self.sort_order == "DESC")

        if self.current_sort_by == "ResidentID":
            data.sort(key=lambda x: x[0], reverse=reverse)
        elif self.current_sort_by == "Full Name":
            data.sort(key=lambda x: x[1].lower(), reverse=reverse)
        elif self.current_sort_by == "Age":
            data.sort(key=lambda x: x[3], reverse=reverse)
        elif self.current_sort_by == "Purok":
            data.sort(key=lambda x: x[4].lower(), reverse=reverse)

        return data

    def update_display(self):
        total_rows = len(self.all_current_data)
        self.total_pages = max(1, (total_rows + self.rows_per_page - 1) // self.rows_per_page)

        if self.current_page > self.total_pages:
            self.current_page = self.total_pages

        start_idx = (self.current_page - 1) * self.rows_per_page
        end_idx = start_idx + self.rows_per_page
        page_data = self.all_current_data[start_idx:end_idx]

        self.populate_table(page_data)
        self.update_pagination_ui()

    def populate_table(self, data):
        self.ui.tableWidget.setRowCount(0)
        for row_data in data:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            for col, value in enumerate(row_data[:6]):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))
            self.add_action_buttons(row, row_data[0])

    def update_pagination_ui(self):
        for i in reversed(range(self.ui.pageButtonsContainer.count())):
            self.ui.pageButtonsContainer.itemAt(i).widget().setParent(None)

        for i in range(1, self.total_pages + 1):
            btn = QPushButton(str(i))
            btn.setFixedSize(30, 30)
            if i == self.current_page:
                btn.setStyleSheet("background-color: #007bff; color: white; font-weight: bold;")
            btn.clicked.connect(lambda checked, p=i: self.go_to_page(p))
            self.ui.pageButtonsContainer.addWidget(btn)

        self.ui.prevButton.setEnabled(self.current_page > 1)
        self.ui.nextButton.setEnabled(self.current_page < self.total_pages)

    def go_to_page(self, page_num):
        self.current_page = page_num
        self.update_display()

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_display()

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_display()

    # ACTIONS
    def add_action_buttons(self, row, resident_id):
        button_layout = QtWidgets.QHBoxLayout()
        button_widget = QtWidgets.QWidget()

        edit_btn = QPushButton("Edit")
        delete_btn = QPushButton("Archive")

        edit_btn.setFixedSize(60, 25)
        delete_btn.setFixedSize(70, 25)

        edit_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffc107; 
                color: black;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
        """)

        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)

        edit_btn.clicked.connect(lambda _, rid=resident_id: self.edit_resident(rid))
        delete_btn.clicked.connect(lambda _, rid=resident_id: self.delete_resident(rid))

        button_layout.addWidget(edit_btn)
        button_layout.addWidget(delete_btn)
        button_layout.setContentsMargins(5, 2, 5, 2)
        button_layout.setSpacing(5)

        button_widget.setLayout(button_layout)
        self.ui.tableWidget.setCellWidget(row, 6, button_widget)

    def edit_resident(self, resident_id):
        dialog = EditResidentDialog(resident_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            updated_data = dialog.get_updated_data()
            try:
                resident_model.update_resident(resident_id, updated_data)
                QMessageBox.information(self, "Success", "Resident information updated successfully!")
                self.refresh_data()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to update resident: {str(e)}")

    def delete_resident(self, resident_id):
        confirm = QMessageBox.question(
            self, "Confirm Archive",
            f"Archive resident ID: {resident_id}?\n\n"
            "- The record will be hidden from view\n"
            "- Data is preserved in database\n"
            "- Can be restored later if needed\n\n"
            "Proceed with archiving?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                success = resident_model.archive_resident(resident_id, "Secretary")
                if success:
                    QMessageBox.information(
                        self,
                        "Success",
                        "Resident archived successfully!\n\n"
                        "You can view and restore archived residents\n"
                        "using the 'View Archived' button."
                    )
                    self.refresh_data()
                else:
                    QMessageBox.warning(self, "Warning", "Resident not found or already archived.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to archive resident: {str(e)}")

    def show_archived_residents(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Archived Residents - Recovery Panel")
        dialog.setFixedSize(1300, 600)

        layout = QVBoxLayout()

        # Title
        title = QLabel("Archived Residents")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)

        # Create table
        table = QTableWidget()
        table.setColumnCount(10)
        headers = ["ResidentID", "Full Name", "Sex", "Age", "Purok", "Civil Status",
                   "Address", "Archived Date", "Archived By", "Actions"]
        table.setHorizontalHeaderLabels(headers)

        # Set resize modes BEFORE setting widths
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)

        # Set column widths
        table.setColumnWidth(0, 70)  # ResidentID
        table.setColumnWidth(1, 150)  # Full Name
        table.setColumnWidth(2, 50)  # Sex
        table.setColumnWidth(3, 40)  # Age
        table.setColumnWidth(4, 70)  # Purok
        table.setColumnWidth(5, 100)  # Civil Status
        table.setColumnWidth(6, 250)  # Address
        table.setColumnWidth(7, 120)  # Archived Date
        table.setColumnWidth(8, 120)  # Archived By
        table.setColumnWidth(9, 180)  # Actions

        table.horizontalHeader().setStretchLastSection(True)

        # Load archived data
        try:
            archived_data = resident_model.get_archived_residents()
            table.setRowCount(len(archived_data))

            for row, row_data in enumerate(archived_data):
                for col in range(7):
                    value = row_data[col] if row_data[col] is not None else ""
                    table.setItem(row, col, QTableWidgetItem(str(value)))

                archived_date = row_data[7] if len(row_data) > 7 and row_data[7] else ""
                if archived_date:
                    if hasattr(archived_date, 'strftime'):
                        archived_date = archived_date.strftime("%Y-%m-%d %H:%M")
                table.setItem(row, 7, QTableWidgetItem(str(archived_date)))

                archived_by = row_data[8] if len(row_data) > 8 and row_data[8] else ""
                table.setItem(row, 8, QTableWidgetItem(str(archived_by)))

                # Add action buttons
                restore_btn = QPushButton("Restore")
                restore_btn.setStyleSheet("""
                      QPushButton {
                          background-color: #28a745;
                          color: white;
                          padding: 5px 10px;
                          border-radius: 3px;
                          font-weight: bold;
                          border: none;
                          min-width: 80px;
                      }
                      QPushButton:hover {
                          background-color: #218838;
                      }
                  """)

                delete_btn = QPushButton("🗑 Delete")
                delete_btn.setStyleSheet("""
                      QPushButton {
                          background-color: #dc3545;
                          color: white;
                          padding: 5px 10px;
                          border-radius: 3px;
                          font-weight: bold;
                          border: none;
                          min-width: 80px;
                      }
                      QPushButton:hover {
                          background-color: #c82333;
                      }
                  """)

                # Connect buttons
                resident_id = row_data[0]
                restore_btn.clicked.connect(
                    lambda checked, rid=resident_id, dlg=dialog: self.restore_resident(rid, dlg))
                delete_btn.clicked.connect(
                    lambda checked, rid=resident_id, dlg=dialog: self.permanent_delete_resident(rid, dlg))

                # Create button layout
                button_layout = QHBoxLayout()
                button_layout.addWidget(restore_btn)
                button_layout.addWidget(delete_btn)
                button_layout.setContentsMargins(5, 2, 5, 2)
                button_layout.setSpacing(5)

                button_widget = QWidget()
                button_widget.setLayout(button_layout)
                table.setCellWidget(row, 9, button_widget)  # Actions in column 9

        except Exception as e:
            table.setRowCount(1)
            table.setColumnCount(1)
            table.setItem(0, 0, QTableWidgetItem(f"Error loading archived data: {str(e)}"))

        # Add close button
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""
              QPushButton {
                  background-color: #007bff;
                  color: white;
                  padding: 8px 20px;
                  border-radius: 5px;
                  font-weight: bold;
                  border: none;
              }
              QPushButton:hover {
                  background-color: #0056b3;
              }
          """)
        close_btn.clicked.connect(dialog.close)
        close_btn.setFixedWidth(100)

        layout.addWidget(table)
        layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        dialog.setLayout(layout)
        dialog.exec()

    def restore_resident(self, resident_id, parent_dialog=None):
        confirm = QMessageBox.question(
            self, "Restore Resident",
            f"Restore resident ID: {resident_id}?\n\n"
            "This will make the resident visible again in the main list.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                success = resident_model.restore_resident(resident_id)
                if success:
                    QMessageBox.information(self, "Success", "Resident restored successfully!")
                    if parent_dialog:
                        parent_dialog.close()
                        self.show_archived_residents()
                    self.refresh_data()
                else:
                    QMessageBox.warning(self, "Warning", "Resident not found or already restored.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to restore resident: {str(e)}")

    def permanent_delete_resident(self, resident_id, parent_dialog=None):
        confirm = QMessageBox.warning(
            self, "WARNING: Permanent Delete",
            f"PERMANENTLY delete resident ID: {resident_id}?\n\n"
            "- This action CANNOT be undone!\n"
            "- All data will be lost forever!\n\n"
            "Are you absolutely sure?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                success = resident_model.permanently_delete_resident(resident_id)
                if success:
                    QMessageBox.information(self, "Deleted", "Resident permanently deleted!")
                    if parent_dialog:
                        parent_dialog.close()
                        self.show_archived_residents()
                else:
                    QMessageBox.warning(self, "Warning", "Resident not found or not archived.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete resident: {str(e)}")

    # SEARCH
    def search_data(self):
        keyword = self.ui.searchLineEdit.text().strip()
        self.current_search_keyword = keyword
        self.refresh_data()

    # FILTER
    def apply_filters(self):
        self.current_filters = {
            'sex': self.ui.filterSexCombo.currentText(),
            'purok': self.ui.filterPurokCombo.currentText(),
            'civil_status': self.ui.filterCivilStatusCombo.currentText(),
            'age_range': self.ui.filterAgeRangeCombo.currentText()
        }
        self.refresh_data()

    # SORT
    def sort_data(self):
        self.current_sort_by = self.ui.sortCombo.currentText()
        self.refresh_data()

