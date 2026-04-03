# viewPopulation_Staff.py
# Form implementation generated from reading ui file 'viewPopulation_Staff.ui'
# Created by: PyQt6 UI code generator 6.10.0
import sys

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ViewPopulation_Staff(object):
    def setupUi(self, ViewPopulation_Staff):
        ViewPopulation_Staff.setObjectName("ViewPopulation_Staff")
        ViewPopulation_Staff.resize(1240, 745)
        ViewPopulation_Staff.setMaximumSize(QtCore.QSize(1240, 745))
        self.sidePanel = QtWidgets.QFrame(parent=ViewPopulation_Staff)
        self.sidePanel.setGeometry(QtCore.QRect(-11, -21, 261, 811))
        self.sidePanel.setStyleSheet("QFrame {\n"
"    border: 2px solid #2C3E50;   \n"
"    border-radius: 10px;         \n"
"    background-color: #2C3E50;   \n"
"}")
        self.sidePanel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sidePanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sidePanel.setObjectName("sidePanel")
        self.staff_Label_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.staff_Label_2.setGeometry(QtCore.QRect(105, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.staff_Label_2.setFont(font)
        self.staff_Label_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"  
"    border: none;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"}")
        self.staff_Label_2.setObjectName("staff_Label_2")
        self.viewPopulation_Button_2 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.viewPopulation_Button_2.setGeometry(QtCore.QRect(89, 340, 125, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.viewPopulation_Button_2.setFont(font)
        self.viewPopulation_Button_2.setStyleSheet("""
QPushButton {
    background-color: #467099;
    border: none;
    color: #FFFFFF;             
    font-weight: bold;          
    text-align: left;           
    padding-left: 5px;          
}

QPushButton:hover {
    background-color: #34495E;
    border-radius: 5px;
}
""")
        self.viewPopulation_Button_2.setDefault(False)
        self.viewPopulation_Button_2.setFlat(True)
        self.viewPopulation_Button_2.setObjectName("viewPopulation_Button_2")
        self.register_Button_2 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.register_Button_2.setGeometry(QtCore.QRect(87, 380, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_Button_2.setFont(font)
        self.register_Button_2.setStyleSheet("""
QPushButton {
    background-color: transparent;
    border: none;
    color: #FFFFFF;             
    font-weight: bold;          
    text-align: left;           
    padding-left: 5px;          
}

QPushButton:hover {
    background-color: #34495E;
    border-radius: 5px;
}
""")
        self.register_Button_2.setFlat(True)
        self.register_Button_2.setObjectName("register_Button_2")

        self.logout_Button_2 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.logout_Button_2.setGeometry(QtCore.QRect(50, 691, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.logout_Button_2.setFont(font)
        self.logout_Button_2.setStyleSheet(" QPushButton {\n"
"                background-color: #dc3545;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #c82333;\n"
"            }")
        self.logout_Button_2.setFlat(False)
        self.logout_Button_2.setObjectName("logout_Button_2")
        self.logo_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.logo_2.setGeometry(QtCore.QRect(40, 45, 190, 175))
        self.logo_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap("Assets/logo/logo 3.png"))
        self.logo_2.setScaledContents(True)
        self.logo_2.setWordWrap(False)
        self.logo_2.setOpenExternalLinks(False)
        self.logo_2.setObjectName("logo_2")
        self.home_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.home_2.setGeometry(QtCore.QRect(50, 295, 35, 25))
        self.home_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.home_2.setText("")
        self.home_2.setPixmap(QtGui.QPixmap("Assets/icons/homepage new.png"))
        self.home_2.setScaledContents(True)
        self.home_2.setWordWrap(False)
        self.home_2.setObjectName("home_2")
        self.viewPopulation_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.viewPopulation_2.setGeometry(QtCore.QRect(45, 335, 40, 25))
        self.viewPopulation_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.viewPopulation_2.setText("")
        self.viewPopulation_2.setPixmap(QtGui.QPixmap("Assets/icons/view population new.png"))
        self.viewPopulation_2.setScaledContents(True)
        self.viewPopulation_2.setWordWrap(False)
        self.viewPopulation_2.setObjectName("viewPopulation_2")

        self.home_Button_3 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.home_Button_3.setGeometry(QtCore.QRect(90, 300, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_Button_3.setFont(font)
        self.home_Button_3.setStyleSheet("""
QPushButton {
    background-color: transparent;
    border: none;
    color: #FFFFFF;             
    font-weight: bold;          
    text-align: left;           
    padding-left: 5px;          
}

QPushButton:hover {
    background-color: #34495E;
    border-radius: 5px;
}
""")
        self.home_Button_3.setFlat(False)
        self.home_Button_3.setObjectName("home_Button_3")
        self.registerResident_2 = QtWidgets.QLabel(parent=self.sidePanel)
        self.registerResident_2.setGeometry(QtCore.QRect(45, 375, 39, 25))
        self.registerResident_2.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.registerResident_2.setText("")
        self.registerResident_2.setPixmap(QtGui.QPixmap("Assets/icons/add new.png"))
        self.registerResident_2.setScaledContents(True)
        self.registerResident_2.setWordWrap(False)
        self.registerResident_2.setObjectName("registerResident_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=ViewPopulation_Staff)
        self.tableWidget.setGeometry(QtCore.QRect(290, 30, 901, 61))
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: white;
            }
            QHeaderView::section {
                background-color: white;
                padding: 8px;
                border: 1px solid #000000;
                font-weight: bold;
            }
        """)

        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(124)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.Title_Label = QtWidgets.QLabel(parent=ViewPopulation_Staff)
        self.Title_Label.setGeometry(QtCore.QRect(300, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        self.Title_Label.setFont(font)
        self.Title_Label.setObjectName("Title_Label")
        self.frame = QtWidgets.QFrame(parent=ViewPopulation_Staff)
        self.frame.setGeometry(QtCore.QRect(250, 0, 991, 741))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color:#E5E7E9;\n"
"}\n"
"")

        # Search bar
        self.searchLineEdit = QtWidgets.QLineEdit(parent=ViewPopulation_Staff)
        self.searchLineEdit.setGeometry(QtCore.QRect(300, 110, 300, 35))
        self.searchLineEdit.setPlaceholderText("Search resident...")

        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.sidePanel.raise_()
        self.tableWidget.raise_()
        self.Title_Label.raise_()
        self.searchLineEdit.raise_()

        self.retranslateUi(ViewPopulation_Staff)
        QtCore.QMetaObject.connectSlotsByName(ViewPopulation_Staff)

        # Filter components
        # Sex Filter
        self.filterSexLabel = QtWidgets.QLabel(parent=ViewPopulation_Staff)
        self.filterSexLabel.setGeometry(QtCore.QRect(300, 160, 50, 25))
        self.filterSexLabel.setText("Sex:")

        self.filterSexCombo = QtWidgets.QComboBox(parent=ViewPopulation_Staff)
        self.filterSexCombo.setGeometry(QtCore.QRect(340, 160, 100, 30))

        # Purok Filter
        self.filterPurokLabel = QtWidgets.QLabel(parent=ViewPopulation_Staff)
        self.filterPurokLabel.setGeometry(QtCore.QRect(455, 160, 50, 25))
        self.filterPurokLabel.setText("Purok:")

        self.filterPurokCombo = QtWidgets.QComboBox(parent=ViewPopulation_Staff)
        self.filterPurokCombo.setGeometry(QtCore.QRect(505, 160, 100, 30))

        # Civil Status Filter
        self.filterCivilStatusLabel = QtWidgets.QLabel(parent=ViewPopulation_Staff)
        self.filterCivilStatusLabel.setGeometry(QtCore.QRect(620, 160, 100, 25))
        self.filterCivilStatusLabel.setText("Civil Status:")

        self.filterCivilStatusCombo = QtWidgets.QComboBox(parent=ViewPopulation_Staff)
        self.filterCivilStatusCombo.setGeometry(QtCore.QRect(695, 160, 100, 30))

        # Age Range Filter
        self.filterAgeRangeLabel = QtWidgets.QLabel(parent=ViewPopulation_Staff)
        self.filterAgeRangeLabel.setGeometry(QtCore.QRect(810, 160, 80, 25))
        self.filterAgeRangeLabel.setText("Age Range:")

        self.filterAgeRangeCombo = QtWidgets.QComboBox(parent=ViewPopulation_Staff)
        self.filterAgeRangeCombo.setGeometry(QtCore.QRect(885, 160, 100, 30))

        # Sort components
        self.sortLabel = QtWidgets.QLabel(parent=ViewPopulation_Staff)
        self.sortLabel.setGeometry(QtCore.QRect(300, 200, 40, 25))
        self.sortLabel.setText("Sort:")

        self.sortCombo = QtWidgets.QComboBox(parent=ViewPopulation_Staff)
        self.sortCombo.setGeometry(QtCore.QRect(340, 200, 100, 30))

        self.sortButton = QtWidgets.QPushButton(parent=ViewPopulation_Staff)
        self.sortButton.setGeometry(QtCore.QRect(455, 200, 40, 30))
        self.sortButton.setText("⬆")
        self.sortButton.setStyleSheet("""
                    QPushButton {
                        background-color: white;
                        border: 1px solid #ced4da;
                        border-radius: 4px;
                        font-weight: bold;
                        font-size: 14px;
                    }
                    QPushButton:hover {
                        background-color: #e2e6ea;
                    }
                """)

        # Table settings
        self.tableWidget.setGeometry(QtCore.QRect(300, 240, 890, 342))
        self.tableWidget.setColumnCount(7)

        self.searchLineEdit.raise_()
        self.filterSexLabel.raise_()
        self.filterSexCombo.raise_()
        self.filterPurokLabel.raise_()
        self.filterPurokCombo.raise_()
        self.filterCivilStatusLabel.raise_()
        self.filterCivilStatusCombo.raise_()
        self.filterAgeRangeLabel.raise_()
        self.filterAgeRangeCombo.raise_()
        self.sortLabel.raise_()
        self.sortCombo.raise_()
        self.sortButton.raise_()

        self.paginationWidget = QtWidgets.QWidget(parent=ViewPopulation_Staff)
        self.paginationWidget.setGeometry(QtCore.QRect(300, 600, 891, 50))
        self.paginationWidget.setStyleSheet("background-color: transparent;")

        self.paginationLayout = QtWidgets.QHBoxLayout(self.paginationWidget)
        self.paginationLayout.setContentsMargins(0, 0, 0, 0)
        self.paginationLayout.setSpacing(10)
        self.paginationLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.prevButton = QtWidgets.QPushButton("< Previous")
        self.prevButton.setFixedSize(100, 30)
        self.prevButton.setStyleSheet("""
                    QPushButton { background-color: white; border: 1px solid #ced4da; border-radius: 4px; }
                    QPushButton:hover { background-color: #e2e6ea; }
                    QPushButton:disabled { color: #ccc; }
                """)

        self.pageButtonsContainer = QtWidgets.QHBoxLayout()
        self.pageButtonsContainer.setSpacing(5)

        self.nextButton = QtWidgets.QPushButton("Next >")
        self.nextButton.setFixedSize(100, 30)
        self.nextButton.setStyleSheet("""
                    QPushButton { background-color: white; border: 1px solid #ced4da; border-radius: 4px; }
                    QPushButton:hover { background-color: #e2e6ea; }
                    QPushButton:disabled { color: #ccc; }
                """)

        self.paginationLayout.addWidget(self.prevButton)
        self.paginationLayout.addLayout(self.pageButtonsContainer)
        self.paginationLayout.addWidget(self.nextButton)

        self.paginationWidget.raise_()

        self.frame = QtWidgets.QFrame(parent=ViewPopulation_Staff)
        self.frame.setGeometry(QtCore.QRect(290, 30, 901, 61))
        self.frame.setStyleSheet("""
            QFrame {
                background-color: #f0f7ff; 
                border-radius: 12px;
                border: 1px solid #d0e1f9;
                border-bottom: 3px solid #3498db; 
            }
            QLabel {
                color: #1a2a3a;
                border: none;
                background: transparent;
                font-weight: bold;
            }
        """)

        self.icon_label = QtWidgets.QLabel(parent=self.frame)
        self.icon_label.setGeometry(QtCore.QRect(5, 10, 51, 41))
        self.icon_label.setText("")
        self.icon_label.setPixmap(QtGui.QPixmap("Assets/icons/view population.png"))
        self.icon_label.setScaledContents(True)
        self.icon_label.setObjectName("icon_label")
        self.icon_label.setStyleSheet("border: none; background: transparent;")

        self.Title_Label = QtWidgets.QLabel(parent=self.frame)
        self.Title_Label.setGeometry(QtCore.QRect(60, 10, 271, 41))
        self.Title_Label.setText("VIEW POPULATION")
        self.Title_Label.setStyleSheet("border: none; background: transparent; font-size: 12pt; font-weight: bold;")

        self.dateTime_Label = QtWidgets.QLabel(parent=self.frame)
        self.dateTime_Label.setGeometry(QtCore.QRect(580, 20, 300, 20))
        self.dateTime_Label.setStyleSheet("border: none; background: transparent; font-size: 12pt; font-weight: bold;")

    def retranslateUi(self, ViewPopulation_Staff):
        _translate = QtCore.QCoreApplication.translate
        ViewPopulation_Staff.setWindowTitle(_translate("ViewPopulation_Staff", "View Population"))
        self.staff_Label_2.setText(_translate("ViewPopulation_Staff", "STAFF"))
        self.viewPopulation_Button_2.setText(_translate("ViewPopulation_Staff", "VIEW POPULATION"))
        self.register_Button_2.setText(_translate("ViewPopulation_Staff", "REGISTER RESIDENT"))
        self.logout_Button_2.setText(_translate("ViewPopulation_Staff", "LOGOUT"))
        self.home_Button_3.setText(_translate("ViewPopulation_Staff", "DASHBOARD"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ViewPopulation_Staff", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ViewPopulation_Staff", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ViewPopulation_Staff", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ViewPopulation_Staff", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ViewPopulation_Staff", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("ViewPopulation_Staff", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("ViewPopulation_Staff", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("ViewPopulation_Staff", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("ViewPopulation_Staff", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("ViewPopulation_Staff", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewPopulation_Staff", "ResidentID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewPopulation_Staff", "Full Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewPopulation_Staff", "Sex"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ViewPopulation_Staff", "Age"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ViewPopulation_Staff", "Address"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ViewPopulation_Staff", "Civil Status"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ViewPopulation_Staff", "Actions"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)