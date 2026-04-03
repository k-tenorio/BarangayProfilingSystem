import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from view.LoginPage.loginPage import loginPage_Secretary
from controller.Dashboard.dashboardController_Secretary import DashboardSecretary
from controller.Dashboard.dashboardController_Staff import DashboardStaff
from model.user_model import UserModel

class Main:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(True)
        self.secretaryWindow = QDialog()
        self.ui_secretary = loginPage_Secretary()
        self.ui_secretary.setupUi(self.secretaryWindow)
        self.ui_secretary.submitButton_QPushButton.clicked.connect(self.login)
        self.ui_secretary.password_QLineEdit.returnPressed.connect(self.login)

    def login(self):
        username = self.ui_secretary.username_QLineEdit.text().strip()
        password = self.ui_secretary.password_QLineEdit.text()

        if not username or not password:
            self.showInputError("Please enter both username and password.")
            return

        user = UserModel.login(username, password)

        if not user:
            self.showLoginError()
            return

        if user["role"] == "Secretary":
            self.openSecretaryDashboard()

        elif user["role"] == "Staff":
            self.openStaffDashboard()

        else:
            self.showLoginError()

    def showInputError(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Icon.Warning)
        error_box.setWindowTitle("Missing Information")
        error_box.setText(message)
        error_box.exec()

    def showLoginError(self):
        self.ui_secretary.password_QLineEdit.clear()
        self.ui_secretary.password_QLineEdit.setFocus()

        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Icon.Critical)
        error_box.setWindowTitle("Login Failed")
        error_box.setText("Invalid username or password. Please try again.")
        error_box.exec()

    def handleLogoutStaff(self):
        if hasattr(self, 'dashboard_staff'):
            self.dashboard_staff.close()

        self.ui_secretary.username_QLineEdit.clear()
        self.ui_secretary.password_QLineEdit.clear()

        self.secretaryWindow.show()

    def openSecretaryDashboard(self):
        self.secretaryWindow.close()
        self.dashboard_secretary = DashboardSecretary()
        self.dashboard_secretary.logout_requested.connect(self.handleLogoutSecretary)
        self.dashboard_secretary.show()

    def openStaffDashboard(self):
        self.secretaryWindow.close()
        self.dashboard_staff = DashboardStaff()
        self.dashboard_staff.logout_requested.connect(self.handleLogoutStaff)
        self.dashboard_staff.show()

    def handleLogoutSecretary(self):
        if hasattr(self, 'dashboard_secretary'):
            self.dashboard_secretary.close()

        self.ui_secretary.username_QLineEdit.clear()
        self.ui_secretary.password_QLineEdit.clear()

        self.secretaryWindow.show()

    def run(self):
        self.secretaryWindow.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    try:
        main = Main()
        main.run()
    except Exception as e:
        import traceback
        print("Error:", e)
        traceback.print_exc()
