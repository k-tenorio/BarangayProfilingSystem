# dashboard_Staff.py
# Form implementation generated from reading ui file 'dashboard_Staff.ui'

from PyQt6 import QtCore, QtGui, QtWidgets


class dashboard_Staff(object):
    def setupUi(self, dashboard_Staff):
        dashboard_Staff.setObjectName("dashboard_Staff")
        dashboard_Staff.resize(1240, 770)  # Changed from 745 to 770 to match secretary
        dashboard_Staff.setMaximumSize(QtCore.QSize(1240, 770))
        dashboard_Staff.setStyleSheet("QDialog {\n"
"    background-color:#E5E7E9;\n"  # Changed from green to match secretary
"}")
        self.sidePanel = QtWidgets.QFrame(parent=dashboard_Staff)
        self.sidePanel.setGeometry(QtCore.QRect(-11, -21, 261, 811))
        self.sidePanel.setStyleSheet("QFrame {\n"
"    border: 2px solid #2C3E50;   \n"
"    border-radius: 10px;         \n"
"    background-color: #2C3E50;   \n"
"}")
        self.sidePanel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sidePanel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sidePanel.setObjectName("sidePanel")
        self.staff_Label = QtWidgets.QLabel(parent=self.sidePanel)
        self.staff_Label.setGeometry(QtCore.QRect(105, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.staff_Label.setFont(font)
        self.staff_Label.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #FFFFFF;              \n"
"    font-weight: bold;\n"
"}")
        self.staff_Label.setObjectName("staff_Label")
        self.viewPopulation_Button = QtWidgets.QPushButton(parent=self.sidePanel)
        self.viewPopulation_Button.setGeometry(QtCore.QRect(89, 340, 125, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.viewPopulation_Button.setFont(font)
        self.viewPopulation_Button.setStyleSheet("""
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
        self.viewPopulation_Button.setDefault(False)
        self.viewPopulation_Button.setFlat(True)
        self.viewPopulation_Button.setObjectName("viewPopulation_Button")
        self.register_Button = QtWidgets.QPushButton(parent=self.sidePanel)
        self.register_Button.setGeometry(QtCore.QRect(87, 380, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_Button.setFont(font)
        self.register_Button.setStyleSheet("""
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
        self.register_Button.setFlat(True)
        self.register_Button.setObjectName("register_Button")
        self.logout_Button = QtWidgets.QPushButton(parent=self.sidePanel)
        self.logout_Button.setGeometry(QtCore.QRect(50, 691, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.logout_Button.setFont(font)
        self.logout_Button.setStyleSheet(" QPushButton {\n"
"                background-color: #dc3545;\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #c82333;\n"
"            }")
        self.logout_Button.setFlat(False)
        self.logout_Button.setObjectName("logout_Button")
        self.logo = QtWidgets.QLabel(parent=self.sidePanel)
        self.logo.setGeometry(QtCore.QRect(40, 50, 191,171))  # Adjusted position to match secretary
        self.logo.setStyleSheet("QLabel {\n"
"    background-color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}")  # Added white background like secretary
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Assets/logo/logo 3.png"))  # Changed to logo 3.png like secretary
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setOpenExternalLinks(False)
        self.logo.setObjectName("logo")
        self.home = QtWidgets.QLabel(parent=self.sidePanel)
        self.home.setGeometry(QtCore.QRect(50, 295, 35, 25))  # Adjusted position
        self.home.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.home.setText("")
        self.home.setPixmap(QtGui.QPixmap("Assets/icons/homepage new.png"))  # Changed to homepage new.png like secretary
        self.home.setScaledContents(True)
        self.home.setWordWrap(False)
        self.home.setObjectName("home")
        self.viewPopulation = QtWidgets.QLabel(parent=self.sidePanel)
        self.viewPopulation.setGeometry(QtCore.QRect(45, 335, 40, 25))  # Adjusted position
        self.viewPopulation.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.viewPopulation.setText("")
        self.viewPopulation.setPixmap(QtGui.QPixmap("Assets/icons/view population new.png"))  # Changed to new.png like secretary
        self.viewPopulation.setScaledContents(True)
        self.viewPopulation.setWordWrap(False)
        self.viewPopulation.setObjectName("viewPopulation")
        self.home_Button_2 = QtWidgets.QPushButton(parent=self.sidePanel)
        self.home_Button_2.setGeometry(QtCore.QRect(90, 300, 100, 20))  # Adjusted position
        font = QtGui.QFont()
        font.setPointSize(10)  # Changed from 9 to 10
        self.home_Button_2.setFont(font)
        self.home_Button_2.setStyleSheet("""
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

        self.home_Button_2.setFlat(False)
        self.home_Button_2.setObjectName("home_Button_2")
        self.registerResident = QtWidgets.QLabel(parent=self.sidePanel)
        self.registerResident.setGeometry(QtCore.QRect(45, 375, 39, 25))  # Adjusted position
        self.registerResident.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.registerResident.setText("")
        self.registerResident.setPixmap(QtGui.QPixmap("Assets/icons/add new.png"))  # Changed to add new.png like secretary
        self.registerResident.setScaledContents(True)
        self.registerResident.setWordWrap(False)
        self.registerResident.setObjectName("registerResident")
        self.frame = QtWidgets.QFrame(parent=dashboard_Staff)
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

        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.home_Button = QtWidgets.QPushButton(parent=self.frame)
        self.home_Button.setGeometry(QtCore.QRect(45, 8, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.home_Button.setFont(font)
        self.home_Button.setFlat(True)
        self.home_Button.setObjectName("home_Button")
        self.dateTime_Label = QtWidgets.QLabel(parent=self.frame)
        self.dateTime_Label.setGeometry(QtCore.QRect(580, 20, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.dateTime_Label.setFont(font)
        self.dateTime_Label.setObjectName("dateTime_Label")
        self.icon = QtWidgets.QLabel(parent=self.frame)
        self.icon.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("Assets/icons/home (2).png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.totalPopulation = QtWidgets.QFrame(parent=dashboard_Staff)
        self.totalPopulation.setGeometry(QtCore.QRect(290, 110, 211, 151))
        self.totalPopulation.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"")
        self.totalPopulation.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.totalPopulation.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.totalPopulation.setObjectName("totalPopulation")
        self.totalPopulationNum = QtWidgets.QLabel(parent=self.totalPopulation)
        self.totalPopulationNum.setGeometry(QtCore.QRect(100, 90, 71, 16))  # Adjusted position
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.totalPopulationNum.setFont(font)
        self.totalPopulationNum.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.totalPopulationNum.setObjectName("totalPopulationNum")
        self.totalDesc = QtWidgets.QLabel(parent=self.totalPopulation)
        self.totalDesc.setGeometry(QtCore.QRect(50, 110, 111, 31))
        self.totalDesc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.totalDesc.setObjectName("totalDesc")
        self.totalPopulation_Icon = QtWidgets.QLabel(parent=self.totalPopulation)
        self.totalPopulation_Icon.setGeometry(QtCore.QRect(85, 30, 41, 41))
        self.totalPopulation_Icon.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 0px;      \n"
"}         ")
        self.totalPopulation_Icon.setText("")
        self.totalPopulation_Icon.setPixmap(QtGui.QPixmap("Assets/icons/population.png"))
        self.totalPopulation_Icon.setScaledContents(True)
        self.totalPopulation_Icon.setObjectName("totalPopulation_Icon")
        self.totalHouseHold = QtWidgets.QFrame(parent=dashboard_Staff)
        self.totalHouseHold.setGeometry(QtCore.QRect(520, 110, 211, 151))
        self.totalHouseHold.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.totalHouseHold.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.totalHouseHold.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.totalHouseHold.setObjectName("totalHouseHold")
        self.totalHouseHoldNum = QtWidgets.QLabel(parent=self.totalHouseHold)
        self.totalHouseHoldNum.setGeometry(QtCore.QRect(100, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.totalHouseHoldNum.setFont(font)
        self.totalHouseHoldNum.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.totalHouseHoldNum.setObjectName("totalHouseHoldNum")
        self.totalHouseHoldDesc = QtWidgets.QLabel(parent=self.totalHouseHold)
        self.totalHouseHoldDesc.setGeometry(QtCore.QRect(50, 110, 111, 31))
        self.totalHouseHoldDesc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.totalHouseHoldDesc.setObjectName("totalHouseHoldDesc")
        self.totalHouseHold_Icon = QtWidgets.QLabel(parent=self.totalHouseHold)
        self.totalHouseHold_Icon.setGeometry(QtCore.QRect(85, 30, 41, 41))
        self.totalHouseHold_Icon.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 0px;      \n"
"}         ")
        self.totalHouseHold_Icon.setText("")
        self.totalHouseHold_Icon.setPixmap(QtGui.QPixmap("Assets/icons/home.png"))
        self.totalHouseHold_Icon.setScaledContents(True)
        self.totalHouseHold_Icon.setObjectName("totalHouseHold_Icon")
        self.men = QtWidgets.QFrame(parent=dashboard_Staff)
        self.men.setGeometry(QtCore.QRect(750, 110, 211, 151))
        self.men.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.men.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.men.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.men.setObjectName("men")
        self.numMen = QtWidgets.QLabel(parent=self.men)
        self.numMen.setGeometry(QtCore.QRect(100, 90, 71, 16))  # Adjusted position
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.numMen.setFont(font)
        self.numMen.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.numMen.setObjectName("numMen")
        self.menDesc = QtWidgets.QLabel(parent=self.men)
        self.menDesc.setGeometry(QtCore.QRect(90, 110, 31, 31))
        self.menDesc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.menDesc.setObjectName("menDesc")
        self.men_Icon = QtWidgets.QLabel(parent=self.men)
        self.men_Icon.setGeometry(QtCore.QRect(80, 30, 51, 51))
        self.men_Icon.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 0px;      \n"
"}         ")
        self.men_Icon.setText("")
        self.men_Icon.setPixmap(QtGui.QPixmap("Assets/icons/men.png"))
        self.men_Icon.setScaledContents(True)
        self.men_Icon.setObjectName("men_Icon")
        self.women = QtWidgets.QFrame(parent=dashboard_Staff)
        self.women.setGeometry(QtCore.QRect(980, 110, 211, 151))
        self.women.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.women.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.women.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.women.setObjectName("women")
        self.womenNum = QtWidgets.QLabel(parent=self.women)
        self.womenNum.setGeometry(QtCore.QRect(100, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.womenNum.setFont(font)
        self.womenNum.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.womenNum.setObjectName("womenNum")
        self.womenDesc = QtWidgets.QLabel(parent=self.women)
        self.womenDesc.setGeometry(QtCore.QRect(80, 110, 51, 31))
        self.womenDesc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.womenDesc.setObjectName("womenDesc")
        self.women_Icon = QtWidgets.QLabel(parent=self.women)
        self.women_Icon.setGeometry(QtCore.QRect(80, 30, 51, 51))
        self.women_Icon.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 0px;      \n"
"}         ")
        self.women_Icon.setText("")
        self.women_Icon.setPixmap(QtGui.QPixmap("Assets/icons/women.png"))
        self.women_Icon.setScaledContents(True)
        self.women_Icon.setObjectName("women_Icon")
        self.seniors = QtWidgets.QFrame(parent=dashboard_Staff)
        self.seniors.setGeometry(QtCore.QRect(290, 280, 211, 151))
        self.seniors.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.seniors.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.seniors.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.seniors.setObjectName("seniors")
        self.seniorsNum = QtWidgets.QLabel(parent=self.seniors)
        self.seniorsNum.setGeometry(QtCore.QRect(100, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.seniorsNum.setFont(font)
        self.seniorsNum.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.seniorsNum.setObjectName("seniorsNum")
        self.seniorsDesc = QtWidgets.QLabel(parent=self.seniors)
        self.seniorsDesc.setGeometry(QtCore.QRect(80, 110, 51, 31))
        self.seniorsDesc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.seniorsDesc.setObjectName("seniorsDesc")
        self.seniors_Icon = QtWidgets.QLabel(parent=self.seniors)
        self.seniors_Icon.setGeometry(QtCore.QRect(85, 30, 41, 41))
        self.seniors_Icon.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 0px;      \n"
"}         ")
        self.seniors_Icon.setText("")
        self.seniors_Icon.setPixmap(QtGui.QPixmap("Assets/icons/seniors.png"))
        self.seniors_Icon.setScaledContents(True)
        self.seniors_Icon.setObjectName("seniors_Icon")
        self.pwd = QtWidgets.QFrame(parent=dashboard_Staff)
        self.pwd.setGeometry(QtCore.QRect(520, 280, 211, 151))
        self.pwd.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.pwd.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pwd.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pwd.setObjectName("pwd")
        self.pwdNum = QtWidgets.QLabel(parent=self.pwd)
        self.pwdNum.setGeometry(QtCore.QRect(100, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pwdNum.setFont(font)
        self.pwdNum.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.pwdNum.setObjectName("pwdNum")
        self.pwdDesc = QtWidgets.QLabel(parent=self.pwd)
        self.pwdDesc.setGeometry(QtCore.QRect(90, 110, 31, 31))
        self.pwdDesc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.pwdDesc.setObjectName("pwdDesc")
        self.pwd_Icon = QtWidgets.QLabel(parent=self.pwd)
        self.pwd_Icon.setGeometry(QtCore.QRect(85, 30, 41, 41))
        self.pwd_Icon.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 0px;      \n"
"}         ")
        self.pwd_Icon.setText("")
        self.pwd_Icon.setPixmap(QtGui.QPixmap("Assets/icons/pwd.png"))
        self.pwd_Icon.setScaledContents(True)
        self.pwd_Icon.setObjectName("pwd_Icon")
        self.minors = QtWidgets.QFrame(parent=dashboard_Staff)
        self.minors.setGeometry(QtCore.QRect(750, 280, 211, 151))
        self.minors.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.minors.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.minors.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.minors.setObjectName("minors")
        self.minorsNum = QtWidgets.QLabel(parent=self.minors)
        self.minorsNum.setGeometry(QtCore.QRect(100, 90, 71, 16))  # Adjusted position
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.minorsNum.setFont(font)
        self.minorsNum.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.minorsNum.setObjectName("minorsNum")
        self.minorsDesc = QtWidgets.QLabel(parent=self.minors)
        self.minorsDesc.setGeometry(QtCore.QRect(82, 110, 51, 31))
        self.minorsDesc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.minorsDesc.setObjectName("minorsDesc")
        self.minors_Icon = QtWidgets.QLabel(parent=self.minors)
        self.minors_Icon.setGeometry(QtCore.QRect(85, 30, 41, 41))
        self.minors_Icon.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 0px;      \n"
"}         ")
        self.minors_Icon.setText("")
        self.minors_Icon.setPixmap(QtGui.QPixmap("Assets/icons/minors.png"))
        self.minors_Icon.setScaledContents(True)
        self.minors_Icon.setObjectName("minors_Icon")
        self.adults = QtWidgets.QFrame(parent=dashboard_Staff)
        self.adults.setGeometry(QtCore.QRect(980, 280, 211, 151))
        self.adults.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.adults.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.adults.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.adults.setObjectName("adults")
        self.numAdult = QtWidgets.QLabel(parent=self.adults)
        self.numAdult.setGeometry(QtCore.QRect(100, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.numAdult.setFont(font)
        self.numAdult.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.numAdult.setObjectName("numAdult")
        self.adultDesc = QtWidgets.QLabel(parent=self.adults)
        self.adultDesc.setGeometry(QtCore.QRect(85, 110, 41, 31))
        self.adultDesc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.adultDesc.setObjectName("adultDesc")
        self.adults_Icon = QtWidgets.QLabel(parent=self.adults)
        self.adults_Icon.setGeometry(QtCore.QRect(85, 30, 41, 41))
        self.adults_Icon.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 0px;      \n"
"}         ")
        self.adults_Icon.setText("")
        self.adults_Icon.setPixmap(QtGui.QPixmap("Assets/icons/adults.png"))
        self.adults_Icon.setScaledContents(True)
        self.adults_Icon.setObjectName("adults_Icon")
        self.populationByAge = QtWidgets.QFrame(parent=dashboard_Staff)
        self.populationByAge.setGeometry(QtCore.QRect(290, 450, 441, 261))
        self.populationByAge.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.populationByAge.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.populationByAge.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.populationByAge.setObjectName("populationByAge")
        self.desc = QtWidgets.QLabel(parent=self.populationByAge)
        self.desc.setGeometry(QtCore.QRect(140, 20, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.desc.setFont(font)
        self.desc.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.desc.setObjectName("desc")
        self.populationPurok = QtWidgets.QFrame(parent=dashboard_Staff)
        self.populationPurok.setGeometry(QtCore.QRect(750, 450, 441, 261))
        self.populationPurok.setStyleSheet("QFrame {\n"
"    background-color: white;\n"  # Changed from f7fff7 to white
"    border-radius: 12px;\n"  # Changed from 15px to 12px
"    border: 1px solid #e0e0e0; \n"
"}\n"
"\n"
"QLabel {\n"
"    color: #2C3E50;\n"  # Changed from #333333 to #2C3E50
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"")
        self.populationPurok.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.populationPurok.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.populationPurok.setObjectName("populationPurok")
        self.desc_2 = QtWidgets.QLabel(parent=self.populationPurok)
        self.desc_2.setGeometry(QtCore.QRect(130, 20, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.desc_2.setFont(font)
        self.desc_2.setStyleSheet("QLabel {\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.desc_2.setObjectName("desc_2")

        self.retranslateUi(dashboard_Staff)
        QtCore.QMetaObject.connectSlotsByName(dashboard_Staff)

    def retranslateUi(self, dashboard_Staff):
        _translate = QtCore.QCoreApplication.translate
        dashboard_Staff.setWindowTitle(_translate("dashboard_Staff", "Dashboard"))
        self.staff_Label.setText(_translate("dashboard_Staff", "STAFF"))
        self.viewPopulation_Button.setText(_translate("dashboard_Staff", "VIEW POPULATION"))
        self.register_Button.setText(_translate("dashboard_Staff", "REGISTER RESIDENT"))
        self.logout_Button.setText(_translate("dashboard_Staff", "LOGOUT"))
        self.home_Button_2.setText(_translate("dashboard_Staff", "DASHBOARD"))
        self.home_Button.setText(_translate("dashboard_Staff", "DASHBOARD"))
        self.dateTime_Label.setText(_translate("dashboard_Staff", "date and time"))
        self.totalPopulationNum.setText(_translate("dashboard_Staff", "TextLabel"))
        self.totalDesc.setText(_translate("dashboard_Staff", "TOTAL POPULATION"))
        self.totalHouseHoldNum.setText(_translate("dashboard_Staff", "TextLabel"))
        self.totalHouseHoldDesc.setText(_translate("dashboard_Staff", "TOTAL HOUSEHOLD"))
        self.numMen.setText(_translate("dashboard_Staff", "TextLabel"))
        self.menDesc.setText(_translate("dashboard_Staff", "MEN"))
        self.womenNum.setText(_translate("dashboard_Staff", "TextLabel"))
        self.womenDesc.setText(_translate("dashboard_Staff", "WOMEN"))
        self.seniorsNum.setText(_translate("dashboard_Staff", "TextLabel"))
        self.seniorsDesc.setText(_translate("dashboard_Staff", "SENIORS"))
        self.pwdNum.setText(_translate("dashboard_Staff", "TextLabel"))
        self.pwdDesc.setText(_translate("dashboard_Staff", "PWD"))
        self.minorsNum.setText(_translate("dashboard_Staff", "TextLabel"))
        self.minorsDesc.setText(_translate("dashboard_Staff", "MINORS"))
        self.numAdult.setText(_translate("dashboard_Staff", "TextLabel"))
        self.adultDesc.setText(_translate("dashboard_Staff", "ADULTS"))
        self.desc.setText(_translate("dashboard_Staff", "POPULATION BY AGE"))
        self.desc_2.setText(_translate("dashboard_Staff", "POPULATION BY PUROK"))