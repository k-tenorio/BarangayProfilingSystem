# view/GenerateReport/generateReport.py

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ViewPopulation(object):
    def setupUi(self, ViewPopulation):
        ViewPopulation.setObjectName("ViewPopulation")
        ViewPopulation.resize(1400, 860)
        ViewPopulation.setMinimumSize(QtCore.QSize(1400, 860))

        # ── Side Panel ────────────────────────────────────────────────
        self.sidePanel = QtWidgets.QFrame(parent=ViewPopulation)
        self.sidePanel.setGeometry(QtCore.QRect(-11, -21, 261, 920))
        self.sidePanel.setStyleSheet(
            "QFrame { border: 2px solid #2C3E50; border-radius: 10px; background-color: #2C3E50; }"
        )
        self.sidePanel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sidePanel.setObjectName("sidePanel")

        self.logo_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.logo_2.setGeometry(QtCore.QRect(40, 50, 191, 171))
        self.logo_2.setStyleSheet("QLabel { background-color: transparent; border: none; }")
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap("Assets/logo/logo 3.png"))
        self.logo_2.setScaledContents(True)
        self.logo_2.setObjectName("logo_2")

        self.secretary_Label_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.secretary_Label_2.setGeometry(QtCore.QRect(70, 230, 141, 31))
        font = QtGui.QFont(); font.setPointSize(13); font.setBold(True)  # noqa
        self.secretary_Label_2.setFont(font)
        self.secretary_Label_2.setStyleSheet(
            "QLabel { background-color: transparent; border: none; color: #FFFFFF; font-weight: bold; }"
        )
        self.secretary_Label_2.setObjectName("secretary_Label_2")

        _nav_btn_style = """
QPushButton {
    background-color: transparent; border: none; color: #FFFFFF;
    font-weight: bold; text-align: left; padding-left: 5px;
}
QPushButton:hover { background-color: #34495E; border-radius: 5px; }
"""
        _active_btn_style = """
QPushButton {
    background-color: #467099; border: none; color: #FFFFFF;
    font-weight: bold; text-align: left; padding-left: 5px;
}
QPushButton:hover { background-color: #34495E; border-radius: 5px; }
"""

        icon_style = "QLabel { background-color: transparent; border: none; }"

        self.home_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.home_2.setGeometry(QtCore.QRect(50, 295, 35, 25))
        self.home_2.setStyleSheet(icon_style); self.home_2.setText("")
        self.home_2.setPixmap(QtGui.QPixmap("Assets/icons/homepage new.png"))
        self.home_2.setScaledContents(True); self.home_2.setObjectName("home_2")

        self.home_Button_3 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.home_Button_3.setGeometry(QtCore.QRect(90, 295, 120, 25))
        f = QtGui.QFont(); f.setPointSize(10)
        self.home_Button_3.setFont(f)
        self.home_Button_3.setStyleSheet(_nav_btn_style)
        self.home_Button_3.setObjectName("home_Button_3")

        self.viewPopulation_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.viewPopulation_2.setGeometry(QtCore.QRect(45, 335, 40, 25))
        self.viewPopulation_2.setStyleSheet(icon_style); self.viewPopulation_2.setText("")
        self.viewPopulation_2.setPixmap(QtGui.QPixmap("Assets/icons/view population new.png"))
        self.viewPopulation_2.setScaledContents(True); self.viewPopulation_2.setObjectName("viewPopulation_2")

        self.viewPopulation_Button_2 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.viewPopulation_Button_2.setGeometry(QtCore.QRect(89, 335, 130, 25))
        self.viewPopulation_Button_2.setFont(f)
        self.viewPopulation_Button_2.setStyleSheet(_nav_btn_style)
        self.viewPopulation_Button_2.setFlat(True)
        self.viewPopulation_Button_2.setObjectName("viewPopulation_Button_2")

        self.registerResident_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.registerResident_2.setGeometry(QtCore.QRect(45, 375, 39, 25))
        self.registerResident_2.setStyleSheet(icon_style); self.registerResident_2.setText("")
        self.registerResident_2.setPixmap(QtGui.QPixmap("Assets/icons/add new.png"))
        self.registerResident_2.setScaledContents(True); self.registerResident_2.setObjectName("registerResident_2")

        self.register_Button_2 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.register_Button_2.setGeometry(QtCore.QRect(87, 375, 140, 25))
        self.register_Button_2.setFont(f)
        self.register_Button_2.setStyleSheet(_nav_btn_style)
        self.register_Button_2.setFlat(True)
        self.register_Button_2.setObjectName("register_Button_2")

        self.generateReports_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.generateReports_2.setGeometry(QtCore.QRect(45, 415, 39, 25))
        self.generateReports_2.setStyleSheet(icon_style); self.generateReports_2.setText("")
        self.generateReports_2.setPixmap(QtGui.QPixmap("Assets/icons/generate report new.png"))
        self.generateReports_2.setScaledContents(True); self.generateReports_2.setObjectName("generateReports_2")

        self.generateReports_Button_2 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.generateReports_Button_2.setGeometry(QtCore.QRect(87, 415, 140, 25))
        self.generateReports_Button_2.setFont(f)
        self.generateReports_Button_2.setStyleSheet(_active_btn_style)
        self.generateReports_Button_2.setFlat(True)
        self.generateReports_Button_2.setObjectName("generateReports_Button_2")

        self.logout_Button_2 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.logout_Button_2.setGeometry(QtCore.QRect(50, 780, 171, 41))
        fb = QtGui.QFont(); fb.setPointSize(10); fb.setBold(True)
        self.logout_Button_2.setFont(fb)
        self.logout_Button_2.setStyleSheet(
            "QPushButton { background-color: #dc3545; color: white; border: none; border-radius: 5px; font-weight: bold; }"
            "QPushButton:hover { background-color: #c82333; }"
        )
        self.logout_Button_2.setObjectName("logout_Button_2")

        # ── Main Frame (outer, fixed) ──────────────────────────────────
        self.frame = QtWidgets.QFrame(parent=ViewPopulation)
        self.frame.setGeometry(QtCore.QRect(240, 0, 1160, 860))
        self.frame.setStyleSheet("QFrame { background-color: #E5E7E9; }")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setObjectName("frame")

        # ── Top bar (fixed, outside scroll area) ──────────────────────
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 5, 1140, 55))
        self.frame_2.setStyleSheet("""
            QFrame {
                background-color: #f0f7ff; border-radius: 12px;
                border: 1px solid #d0e1f9; border-bottom: 3px solid #3498db;
            }
            QLabel { color: #1a2a3a; border: none; background: transparent; font-weight: bold; }
        """)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setObjectName("frame_2")

        self.icon = QtWidgets.QLabel(parent=self.frame_2)
        self.icon.setGeometry(QtCore.QRect(10, 7, 38, 38))
        self.icon.setText(""); self.icon.setPixmap(QtGui.QPixmap("Assets/Icons/home (2).png"))
        self.icon.setScaledContents(True); self.icon.setObjectName("icon")

        self.home_Button = QtWidgets.QPushButton(parent=self.frame_2)
        self.home_Button.setGeometry(QtCore.QRect(40, 7, 200, 38))
        fh = QtGui.QFont(); fh.setPointSize(13); fh.setBold(True)
        self.home_Button.setFont(fh)
        self.home_Button.setFlat(True); self.home_Button.setObjectName("home_Button")

        self.dateTime_Label = QtWidgets.QLabel(parent=self.frame_2)
        self.dateTime_Label.setGeometry(QtCore.QRect(780, 16, 350, 22))
        fd = QtGui.QFont(); fd.setFamily("Segoe UI"); fd.setPointSize(11); fd.setBold(True)
        self.dateTime_Label.setFont(fd); self.dateTime_Label.setObjectName("dateTime_Label")

        # ── Scroll Area (contains all content below the top bar) ──────
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(10, 65, 1140, 790))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setStyleSheet("QScrollArea { border: none; background-color: #E5E7E9; }")
        self.scrollArea.setObjectName("scrollArea")

        # ── Scroll content widget ──────────────────────────────────────
        self.scrollContent = QtWidgets.QWidget()
        self.scrollContent.setObjectName("scrollContent")
        # Total inner height: 85 + 10 + 160 + 10 + 55 + 10 + 45 + 10 + 320 + 10 + 45 + 10 = ~760
        # We set a tall enough fixed height so all content fits and scroll works
        self.scrollContent.setMinimumWidth(1110)
        self.scrollArea.setWidget(self.scrollContent)

        # ── Registration Analytics Frame ───────────────────────────────
        self.RegistrationAnalytics = QtWidgets.QFrame(parent=self.scrollContent)
        self.RegistrationAnalytics.setGeometry(QtCore.QRect(10, 10, 1110, 80))
        self.RegistrationAnalytics.setStyleSheet(
            "QFrame { background-color: #f7fff7; border-radius: 15px; }"
        )
        self.RegistrationAnalytics.setObjectName("RegistrationAnalytics")

        reg_font = QtGui.QFont(); reg_font.setFamily("Arial"); reg_font.setPointSize(10)
        reg_num_font = QtGui.QFont(); reg_num_font.setFamily("Arial"); reg_num_font.setPointSize(14); reg_num_font.setBold(True)

        reg_items = [
            ("Today",      "registrationsToday",  "registrationTodayNum",  10),
            ("This Week",  "registrationsWeek",   "registrationsWeek_2",   280),
            ("This Month", "registrationMonth",   "registrationsMonthNum", 550),
            ("This Year",  "label_4",             "registrationsYearNum",  820),
        ]
        for (lbl_txt, lbl_obj, num_obj, x) in reg_items:
            lbl = QtWidgets.QLabel(lbl_txt, parent=self.RegistrationAnalytics)
            lbl.setGeometry(QtCore.QRect(x, 8, 170, 22))
            lbl.setFont(reg_font); lbl.setObjectName(lbl_obj); setattr(self, lbl_obj, lbl)

            num = QtWidgets.QLabel("0", parent=self.RegistrationAnalytics)
            num.setGeometry(QtCore.QRect(x + 35, 32, 90, 35))
            num.setFont(reg_num_font); num.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            num.setObjectName(num_obj); setattr(self, num_obj, num)

        # ── Population Summary Frame ───────────────────────────────────
        # Added "Other Gender" row → needs extra height: 5 rows in col1 → 160px
        self.Summarize = QtWidgets.QFrame(parent=self.scrollContent)
        self.Summarize.setGeometry(QtCore.QRect(10, 100, 1110, 160))
        self.Summarize.setStyleSheet(
            "QFrame { background-color: #f7fff7; border: none; border-radius: 15px; }"
        )
        self.Summarize.setObjectName("Summarize")

        _lbl_font = QtGui.QFont("Arial", 11)
        _num_font = QtGui.QFont("Arial", 12)
        _num_font.setBold(True)

        # col1: Demographics (5 rows now with Other Gender)
        rows = [
            ("Total Population:", "totalPopulationLabel", "totalPopulationNum"),
            ("Total Household:",  "totalHouseholdLabel",  "totalHouseholdNum"),
            ("Total Men:",        "menLabel",             "menNum"),
            ("Total Women:",      "womenLabel",           "womenNum"),
            ("Other Gender:",     "otherGenderLabel",     "otherGenderNum"),
        ]
        # col2: Age / PWD / Deceased
        rows2 = [
            ("Total Seniors (60+):", "totalSeniorsLabel", "seniorsNum"),
            ("Total Adults (19-59):", "totalAdultsLabel", "adultsNum"),
            ("Total Minors (<18):",   "totalMinorsLabel",  "minorsNum"),
            ("Total PWD:",            "totalPWDLabel",     "pwdNum"),
            ("Deceased:",             "deceasedLabel",     "deceasedNum"),
        ]
        # col3: Civil Status
        rows3 = [
            ("Single:",    "singleLabel",    "singleNum"),
            ("Married:",   "marriedLabel",   "marriedNum"),
            ("Widowed:",   "widowedLabel",   "widowedNum"),
            ("Separated:", "separatedLabel", "separatedNum"),
        ]
        # col4: Nationality
        rows4 = [
            ("Filipino:",          "filipinoLabel",  "filipinoNum"),
            ("Other Nationality:", "otherNatLabel",  "otherNatNum"),
        ]

        def make_summary_col(parent, items, base_x):
            y = 12
            for (lbl_txt, lbl_name, num_name) in items:
                lbl = QtWidgets.QLabel(parent=parent)
                lbl.setGeometry(QtCore.QRect(base_x, y, 180, 22))
                lbl.setFont(_lbl_font); lbl.setText(lbl_txt)
                lbl.setObjectName(lbl_name)
                setattr(self, lbl_name, lbl)

                num = QtWidgets.QLabel(parent=parent)
                num.setGeometry(QtCore.QRect(base_x + 185, y, 60, 22))
                num.setFont(_num_font); num.setText("0")
                num.setObjectName(num_name)
                setattr(self, num_name, num)
                y += 27

        make_summary_col(self.Summarize, rows,  10)
        make_summary_col(self.Summarize, rows2, 290)
        make_summary_col(self.Summarize, rows3, 570)
        make_summary_col(self.Summarize, rows4, 850)

        # ── Filter / Category Row ──────────────────────────────────────
        self.filterFrame = QtWidgets.QFrame(parent=self.scrollContent)
        self.filterFrame.setGeometry(QtCore.QRect(10, 270, 1110, 55))
        self.filterFrame.setStyleSheet(
            "QFrame { background-color: #dce8f5; border: 1px solid #b0c8e8; border-radius: 10px; }"
            "QLabel { color: #1a2a3a; background: transparent; border: none; font-weight: bold; }"
        )
        self.filterFrame.setObjectName("filterFrame")

        fl = QtGui.QFont("Arial", 11); fl.setBold(True)

        self.filterCategoryLabel = QtWidgets.QLabel("Filter Category:", parent=self.filterFrame)
        self.filterCategoryLabel.setGeometry(QtCore.QRect(15, 14, 130, 25))
        self.filterCategoryLabel.setFont(fl)

        self.filterCategoryCombo = QtWidgets.QComboBox(parent=self.filterFrame)
        self.filterCategoryCombo.setGeometry(QtCore.QRect(150, 12, 200, 30))
        self.filterCategoryCombo.setFont(QtGui.QFont("Arial", 10))
        self.filterCategoryCombo.addItems([
            "All Categories", "Demographics", "Nationality",
            "Civil Status", "Blood Type", "Religion", "Age Group"
        ])
        self.filterCategoryCombo.setObjectName("filterCategoryCombo")

        self.dateRangeLabel = QtWidgets.QLabel("Registered:", parent=self.filterFrame)
        self.dateRangeLabel.setGeometry(QtCore.QRect(370, 14, 90, 25))
        self.dateRangeLabel.setFont(fl)

        self.dateRangeCombo = QtWidgets.QComboBox(parent=self.filterFrame)
        self.dateRangeCombo.setGeometry(QtCore.QRect(460, 12, 160, 30))
        self.dateRangeCombo.setFont(QtGui.QFont("Arial", 10))
        self.dateRangeCombo.addItems(["All Time", "Today", "This Week", "This Month", "This Year", "Custom Range"])
        self.dateRangeCombo.setObjectName("dateRangeCombo")

        self.dateFromLabel = QtWidgets.QLabel("From:", parent=self.filterFrame)
        self.dateFromLabel.setGeometry(QtCore.QRect(635, 14, 45, 25))
        self.dateFromLabel.setFont(fl); self.dateFromLabel.setVisible(False)

        self.dateFromEdit = QtWidgets.QDateEdit(parent=self.filterFrame)
        self.dateFromEdit.setGeometry(QtCore.QRect(680, 12, 120, 30))
        self.dateFromEdit.setCalendarPopup(True)
        self.dateFromEdit.setDate(QtCore.QDate.currentDate().addDays(-30))
        self.dateFromEdit.setFont(QtGui.QFont("Arial", 10))
        self.dateFromEdit.setVisible(False); self.dateFromEdit.setObjectName("dateFromEdit")

        self.dateToLabel = QtWidgets.QLabel("To:", parent=self.filterFrame)
        self.dateToLabel.setGeometry(QtCore.QRect(808, 14, 30, 25))
        self.dateToLabel.setFont(fl); self.dateToLabel.setVisible(False)

        self.dateToEdit = QtWidgets.QDateEdit(parent=self.filterFrame)
        self.dateToEdit.setGeometry(QtCore.QRect(838, 12, 120, 30))
        self.dateToEdit.setCalendarPopup(True)
        self.dateToEdit.setDate(QtCore.QDate.currentDate())
        self.dateToEdit.setFont(QtGui.QFont("Arial", 10))
        self.dateToEdit.setVisible(False); self.dateToEdit.setObjectName("dateToEdit")

        self.applyFilterBtn = QtWidgets.QPushButton("Apply Filter", parent=self.filterFrame)
        self.applyFilterBtn.setGeometry(QtCore.QRect(975, 12, 110, 32))
        self.applyFilterBtn.setStyleSheet(
            "QPushButton { background-color: #3498db; color: white; border: none; border-radius: 5px; font-weight: bold; font-size: 11px; }"
            "QPushButton:hover { background-color: #2980b9; }"
        )
        self.applyFilterBtn.setObjectName("applyFilterBtn")

        # ── Who Registered panel ───────────────────────────────────────
        self.whoRegisteredFrame = QtWidgets.QFrame(parent=self.scrollContent)
        self.whoRegisteredFrame.setGeometry(QtCore.QRect(10, 335, 1110, 45))
        self.whoRegisteredFrame.setStyleSheet(
            "QFrame { background-color: #fefefe; border: 1px solid #ddd; border-radius: 10px; }"
        )
        self.whoRegisteredFrame.setObjectName("whoRegisteredFrame")

        self.whoRegisteredLabel = QtWidgets.QLabel("Registered in selected period: ", parent=self.whoRegisteredFrame)
        self.whoRegisteredLabel.setGeometry(QtCore.QRect(15, 12, 300, 22))
        wrf = QtGui.QFont(); wrf.setFamily("Arial"); wrf.setPointSize(11); wrf.setBold(True)
        self.whoRegisteredLabel.setFont(wrf)
        self.whoRegisteredLabel.setStyleSheet("border: none; background-color: transparent;")

        self.whoRegisteredCount = QtWidgets.QLabel("0 residents", parent=self.whoRegisteredFrame)
        self.whoRegisteredCount.setGeometry(QtCore.QRect(250, 12, 120, 22))
        self.whoRegisteredCount.setFont(wrf)
        self.whoRegisteredCount.setStyleSheet("""
            color: #2980b9;
            border: none;
            background-color: transparent;
        """)

        self.viewWhoRegisteredBtn = QtWidgets.QPushButton("View Names ▼", parent=self.whoRegisteredFrame)
        self.viewWhoRegisteredBtn.setGeometry(QtCore.QRect(400, 9, 130, 28))
        self.viewWhoRegisteredBtn.setStyleSheet(
            "QPushButton { background-color: #2ecc71; color: white; border: none; border-radius: 5px; font-size: 10px; font-weight: bold; }"
            "QPushButton:hover { background-color: #27ae60; }"
        )
        self.viewWhoRegisteredBtn.setObjectName("viewWhoRegisteredBtn")

        # ── Purok Distribution Table ───────────────────────────────────
        self.tableWidget = QtWidgets.QTableWidget(parent=self.scrollContent)
        self.tableWidget.setGeometry(QtCore.QRect(10, 390, 1110, 320))
        self.tableWidget.setStyleSheet("QTableWidget { background-color: #FFFFFF; }")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(26)
        self.tableWidget.verticalHeader().setMinimumSectionSize(22)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setObjectName("tableWidget")

        # ── Generate PDF Button ────────────────────────────────────────
        self.generatePdfFrame = QtWidgets.QFrame(parent=self.scrollContent)
        self.generatePdfFrame.setGeometry(QtCore.QRect(10, 720, 1110, 40))
        self.generatePdfFrame.setStyleSheet("QFrame { background-color: transparent; border: none; }")
        self.generatePdfFrame.setObjectName("generatePdfFrame")

        # Set scroll content minimum height to fit all widgets + padding
        self.scrollContent.setMinimumHeight(770)

        # Raise all frames
        self.frame_2.raise_()
        self.scrollArea.raise_()
        self.frame.raise_()
        self.sidePanel.raise_()

        self.retranslateUi(ViewPopulation)
        QtCore.QMetaObject.connectSlotsByName(ViewPopulation)

    def retranslateUi(self, ViewPopulation):
        _translate = QtCore.QCoreApplication.translate
        ViewPopulation.setWindowTitle(_translate("ViewPopulation", "Generate Report"))
        self.secretary_Label_2.setText(_translate("ViewPopulation", "SECRETARY"))
        self.viewPopulation_Button_2.setText(_translate("ViewPopulation", "VIEW POPULATION"))
        self.register_Button_2.setText(_translate("ViewPopulation", "REGISTER RESIDENT"))
        self.generateReports_Button_2.setText(_translate("ViewPopulation", "GENERATE REPORTS"))
        self.logout_Button_2.setText(_translate("ViewPopulation", "LOGOUT"))
        self.home_Button_3.setText(_translate("ViewPopulation", "DASHBOARD"))
        self.home_Button.setText(_translate("ViewPopulation", "Generate Report"))
        self.dateTime_Label.setText(_translate("ViewPopulation", "date and time"))
        self.tableWidget.setSortingEnabled(False)