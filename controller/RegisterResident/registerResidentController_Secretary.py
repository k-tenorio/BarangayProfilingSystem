# view/RegisterResident/registerResidentController.py

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import pyqtSignal, QTimer
from view.RegisterResident.registerResident_Secretary import register_Secretary
from model.db_connections import connect_db
from datetime import datetime

REQUIRED_LABEL_STYLE = "color: red; font-size: 10px; font-style: italic;"


class RegisterResidentController(QtWidgets.QDialog):
    dashboard_requested = pyqtSignal()
    logout_requested = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModal(False)

        self.ui = register_Secretary()
        self.ui.setupUi(self)

        self.update_date_time()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)

        self.ui.home_Button_3.clicked.connect(self.go_back_to_dashboard)
        self.ui.registerResidentButton.clicked.connect(self.save_resident)
        self.ui.logout_Button_3.clicked.connect(self.handle_logout)

        self.ui.viewPopulation_Button_2.clicked.connect(self.open_view_population)
        self.ui.generateReports_Button_2.clicked.connect(self.open_generate_reports)

        self.setup_combo_box_connections()
        self._setup_required_labels()

    def _make_required_label(self, parent_widget):
        lbl = QtWidgets.QLabel("* Required", parent_widget)
        lbl.setStyleSheet(REQUIRED_LABEL_STYLE)
        lbl.hide()
        lbl.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        return lbl

    def _position_required_label(self, label: QtWidgets.QLabel, field: QtWidgets.QWidget):
        x = field.x() + field.width() + 5
        y = field.y() + (field.height() - 16) // 2
        label.setGeometry(x, y, 80, 16)

    def _setup_required_labels(self):

        frame = self.ui.personalInfromationFrame_2

        required_text_fields = {
            "req_firstName":      (self.ui.firstNameInput_2,            frame),
            "req_lastName":       (self.ui.lastNameInput_2,             frame),
            "req_placeOfBirth":   (self.ui.placeOfBirthInput_2,         frame),
            "req_fathersName":    (self.ui.fathersNameInput_2,          frame),
            "req_mothersName":    (self.ui.mothersNameInput_2,          frame),
            "req_contact":        (self.ui.contactNumberInput_2,        frame),
            "req_height":         (self.ui.heightInput_2,               frame),
            "req_weight":         (self.ui.weightInput_2,               frame),
        }

        extra_fields = {
            "req_street":         (self.ui.streetInput,                 self.ui.streetInput.parentWidget()),
            "req_houseID":        (self.ui.houseIDInput,                self.ui.houseIDInput.parentWidget()),
            "req_email":          (self.ui.emailInput,                  self.ui.emailInput.parentWidget()),
            "req_emergName":      (self.ui.emergencyContactNameInput,   self.ui.emergencyContactNameInput.parentWidget()),
            "req_emergNumber":    (self.ui.emergencyContactNumberInput, self.ui.emergencyContactNumberInput.parentWidget()),
        }

        all_fields = {**required_text_fields, **extra_fields}

        for attr, (field, parent) in all_fields.items():
            lbl = self._make_required_label(parent)
            self._position_required_label(lbl, field)
            setattr(self, attr, lbl)

            field.textChanged.connect(
                lambda text, l=lbl: l.hide() if text.strip() else None
            )

    def _show_required(self, label: QtWidgets.QLabel):
        label.show()
        label.raise_()

    def _hide_required(self, label: QtWidgets.QLabel):
        label.hide()

    def go_back_to_dashboard(self):
        self.dashboard_requested.emit()
        self.close()

    def open_view_population(self):
        dashboard = self.parent()
        if dashboard and hasattr(dashboard, 'open_view_population'):
            self.close()
            dashboard.show()
            dashboard.open_view_population()
        else:
            from controller.ViewPopulation.viewPopulationController_Secretary import ViewPopulationController
            self.close()
            self.view_pop = ViewPopulationController(dashboard_reference=dashboard)
            self.view_pop.show()

    def handle_logout(self):
        from controller.Dashboard.dashboardController_Secretary import LogoutConfirmDialog
        dialog = LogoutConfirmDialog(self)
        if dialog.exec():
            self.logout_requested.emit()
            self.close()

    def update_date_time(self):
        now = datetime.now()
        date_time_str = now.strftime("%A, %b %d, %Y | %I:%M:%S %p")
        self.ui.dateTime_Label.setText(date_time_str)

    def setup_combo_box_connections(self):
        self.ui.nationalityComboBox_2.currentIndexChanged.connect(
            lambda index: self.toggle_other_field(index, self.ui.otherInput_4, 6)
        )
        self.ui.religionComboBox_2.currentIndexChanged.connect(
            lambda index: self.toggle_other_field(index, self.ui.otherInput_5, 7)
        )
        self.ui.sexComboBox_2.currentIndexChanged.connect(
            lambda index: self.toggle_other_field(index, self.ui.otherInput_6, 2)
        )
        self.ui.otherInput_4.setVisible(False)
        self.ui.otherInput_5.setVisible(False)
        self.ui.otherInput_6.setVisible(False)

    def toggle_other_field(self, index, field_widget, other_index):
        if index == other_index:
            field_widget.setEnabled(True)
            field_widget.setVisible(True)
            field_widget.setFocus()
        else:
            field_widget.setEnabled(False)
            field_widget.setVisible(False)
            field_widget.clear()

    def validate_required_fields(self):

        format_errors = []
        has_empty = False

        def check_empty(value, label):
            nonlocal has_empty
            if not value:
                self._show_required(label)
                has_empty = True
            else:
                self._hide_required(label)

        first_name = self.ui.firstNameInput_2.text().strip()
        check_empty(first_name, self.req_firstName)

        last_name = self.ui.lastNameInput_2.text().strip()
        check_empty(last_name, self.req_lastName)

        place_of_birth = self.ui.placeOfBirthInput_2.text().strip()
        check_empty(place_of_birth, self.req_placeOfBirth)

        fathers_name = self.ui.fathersNameInput_2.text().strip()
        check_empty(fathers_name, self.req_fathersName)

        mothers_name = self.ui.mothersNameInput_2.text().strip()
        check_empty(mothers_name, self.req_mothersName)

        height_text = self.ui.heightInput_2.text().strip()
        if not height_text:
            self._show_required(self.req_height)
            has_empty = True
        else:
            self._hide_required(self.req_height)
            try:
                h = float(height_text)
                if h <= 0 or h > 300:
                    format_errors.append("Height must be between 1 and 300 cm")
            except ValueError:
                format_errors.append("Height must be a valid number")

        weight_text = self.ui.weightInput_2.text().strip()
        if not weight_text:
            self._show_required(self.req_weight)
            has_empty = True
        else:
            self._hide_required(self.req_weight)
            try:
                w = float(weight_text)
                if w <= 0 or w > 500:
                    format_errors.append("Weight must be between 1 and 500 kg")
            except ValueError:
                format_errors.append("Weight must be a valid number")

        contact = self.ui.contactNumberInput_2.text().strip()
        if not contact:
            self._show_required(self.req_contact)
            has_empty = True
        else:
            self._hide_required(self.req_contact)
            if not contact.replace('+', '').isdigit():
                format_errors.append("Contact Number must contain only numbers")
            elif len(contact.replace('+', '')) < 7:
                format_errors.append("Contact Number is too short")
            elif len(contact) > 13:
                format_errors.append("Contact Number is too long")

        street = self.ui.streetInput.text().strip()
        check_empty(street, self.req_street)

        house_id = self.ui.houseIDInput.text().strip()
        check_empty(house_id, self.req_houseID)

        email = self.ui.emailInput.text().strip()
        if not email:
            self._show_required(self.req_email)
            has_empty = True
        else:
            self._hide_required(self.req_email)
            if '@' not in email or '.' not in email:
                format_errors.append("Valid email is required (must contain '@' and '.')")

        emerg_name = self.ui.emergencyContactNameInput.text().strip()
        check_empty(emerg_name, self.req_emergName)

        emerg_number = self.ui.emergencyContactNumberInput.text().strip()
        if not emerg_number:
            self._show_required(self.req_emergNumber)
            has_empty = True
        else:
            self._hide_required(self.req_emergNumber)
            if not emerg_number.replace('+', '').isdigit():
                format_errors.append("Emergency Contact Number must contain only numbers")
            elif len(emerg_number.replace('+', '')) < 7:
                format_errors.append("Emergency Contact Number is too short")
            elif len(emerg_number) > 15:
                format_errors.append("Emergency Contact Number is too long")

        dob = self.ui.dateOfBirthInput_2.date()
        current_date = QtCore.QDate.currentDate()
        age = dob.daysTo(current_date) // 365
        if dob > current_date:
            format_errors.append("Date of Birth cannot be in the future")
        elif age < 1:
            format_errors.append("Resident must be at least 1 year old")
        elif age > 120:
            format_errors.append("Please verify Date of Birth (age over 120)")

        if self.ui.sexComboBox_2.currentIndex() == 2 and not self.ui.otherInput_6.text().strip():
            format_errors.append("Please specify gender when 'Other' is selected")
        if self.ui.nationalityComboBox_2.currentIndex() == 6 and not self.ui.otherInput_4.text().strip():
            format_errors.append("Please specify nationality when 'Other' is selected")
        if self.ui.religionComboBox_2.currentIndex() == 7 and not self.ui.otherInput_5.text().strip():
            format_errors.append("Please specify religion when 'Other' is selected")

        if format_errors:
            error_message = "Please fix the following:\n\n" + "\n".join(f"• {e}" for e in format_errors)
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Validation Error")
            msg.setText(error_message)
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setStyleSheet("""
                QMessageBox { background-color: white; }
                QLabel { color: black; }
                QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    padding: 4px 12px;
                }
                QPushButton:hover { background-color: #e0e0e0; }
            """)
            msg.exec()
            return False

        if has_empty:
            return False

        return True

    def save_resident(self):
        if not self.validate_required_fields():
            return
        try:
            conn = connect_db()
            cursor = conn.cursor()

            resident_sql = """
            INSERT INTO residents (
                first_name, middle_name, last_name,
                sex, date_of_birth, place_of_birth,
                nationality, religion,
                is_deceased, is_pwd,
                civil_status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            sex_value = self.get_combo_box_value(self.ui.sexComboBox_2, self.ui.otherInput_6, 2)
            nationality_value = self.get_combo_box_value(self.ui.nationalityComboBox_2, self.ui.otherInput_4, 6)
            religion_value = self.get_combo_box_value(self.ui.religionComboBox_2, self.ui.otherInput_5, 7)

            resident_values = (
                self.ui.firstNameInput_2.text().strip(),
                self.ui.middleNameInput_2.text().strip(),
                self.ui.lastNameInput_2.text().strip(),
                sex_value,
                self.ui.dateOfBirthInput_2.date().toString("yyyy-MM-dd"),
                self.ui.placeOfBirthInput_2.text().strip(),
                nationality_value,
                religion_value,
                1 if self.ui.deceasedBox_2.isChecked() else 0,
                1 if self.ui.pwdCheckBox_2.isChecked() else 0,
                self.ui.civilStatusInput_2.currentText()
            )

            print(f"DEBUG → sex={sex_value}, nationality={nationality_value}, religion={religion_value}")

            cursor.execute(resident_sql, resident_values)
            resident_id = cursor.lastrowid

            cursor.execute(
                "INSERT INTO resident_addresses (resident_id, purok, street, house_id) VALUES (%s, %s, %s, %s)",
                (resident_id, self.ui.purokInput.currentText(),
                 self.ui.streetInput.text(), self.ui.houseIDInput.text())
            )
            cursor.execute(
                "INSERT INTO resident_contacts (resident_id, contact_number, email) VALUES (%s, %s, %s)",
                (resident_id, self.ui.contactNumberInput_2.text(), self.ui.emailInput.text())
            )
            cursor.execute(
                "INSERT INTO resident_emergency_contacts (resident_id, emergency_contact_name, emergency_contact_number) VALUES (%s, %s, %s)",
                (resident_id, self.ui.emergencyContactNameInput.text(), self.ui.emergencyContactNumberInput.text())
            )
            cursor.execute(
                "INSERT INTO resident_parents (resident_id, father_name, mother_name) VALUES (%s, %s, %s)",
                (resident_id, self.ui.fathersNameInput_2.text(), self.ui.mothersNameInput_2.text())
            )
            cursor.execute(
                "INSERT INTO resident_physical_info (resident_id, blood_type, height_cm, weight_kg) VALUES (%s, %s, %s, %s)",
                (resident_id, self.ui.bloodTypeInput_2.currentText(),
                 float(self.ui.heightInput_2.text() or 0),
                 float(self.ui.weightInput_2.text() or 0))
            )

            conn.commit()
            cursor.close()
            conn.close()

            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Success")
            msg.setText("Resident registered successfully!")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setStyleSheet("background-color: white; color: black;")
            msg.exec()

            self.clear_form_fields()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to save resident:\n{e}")

    def get_combo_box_value(self, combo_box, other_field, other_index):
        if combo_box.currentIndex() == other_index:
            custom_text = other_field.text().strip()
            return custom_text if custom_text else "Other"
        return combo_box.currentText()

    def open_generate_reports(self):
        from controller.GenerateReport.generateReportController_Secretary import GenerateReportController
        self.hide()
        self.reports_page = GenerateReportController(parent=self.parent())
        # Connect the logout signal from the reports page
        self.reports_page.logout_requested.connect(self.handle_child_logout)
        self.reports_page.dashboard_requested.connect(self.handle_child_dashboard)
        self.reports_page.show()

    def handle_child_logout(self):
        self.logout_requested.emit()
        self.close()

    def handle_child_dashboard(self):
        self.dashboard_requested.emit()
        self.close()

    def clear_form_fields(self):
        for field in [
            self.ui.firstNameInput_2, self.ui.middleNameInput_2, self.ui.lastNameInput_2,
            self.ui.placeOfBirthInput_2, self.ui.heightInput_2, self.ui.weightInput_2,
            self.ui.contactNumberInput_2, self.ui.fathersNameInput_2, self.ui.mothersNameInput_2,
            self.ui.emailInput, self.ui.emergencyContactNameInput,
            self.ui.emergencyContactNumberInput, self.ui.streetInput, self.ui.houseIDInput,
            self.ui.otherInput_4, self.ui.otherInput_5, self.ui.otherInput_6,
        ]:
            field.clear()

        self.ui.otherInput_4.setVisible(False)
        self.ui.otherInput_5.setVisible(False)
        self.ui.otherInput_6.setVisible(False)

        self.ui.sexComboBox_2.setCurrentIndex(0)
        self.ui.nationalityComboBox_2.setCurrentIndex(0)
        self.ui.religionComboBox_2.setCurrentIndex(0)
        self.ui.bloodTypeInput_2.setCurrentIndex(0)
        self.ui.civilStatusInput_2.setCurrentIndex(0)
        self.ui.purokInput.setCurrentIndex(0)

        from PyQt6.QtCore import QDate
        self.ui.dateOfBirthInput_2.setDate(QDate.currentDate())

        self.ui.deceasedBox_2.setChecked(False)
        self.ui.pwdCheckBox_2.setChecked(False)

        # Hide all required labels after clearing
        for attr in [
            "req_firstName", "req_lastName", "req_placeOfBirth", "req_fathersName",
            "req_mothersName", "req_contact", "req_height", "req_weight",
            "req_street", "req_houseID", "req_email", "req_emergName", "req_emergNumber",
        ]:
            getattr(self, attr).hide()

    def closeEvent(self, event):
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()
        super().closeEvent(event)

