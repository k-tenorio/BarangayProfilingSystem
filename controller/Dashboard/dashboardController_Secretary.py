from PyQt6 import QtWidgets, QtCore
from view.Dashboard.dashboard_Secretary import dashboard_Secretary
from datetime import datetime
from PyQt6.QtCore import pyqtSignal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from model.db_connections import connect_db
import mysql.connector

class LogoutConfirmDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Logout Confirmation")
        self.setFixedSize(300, 150)

        self.setStyleSheet("""
            QDialog {
                background-color: white;
                border: 2px solid #dcdcdc;
                border-radius: 10px;
            }
            QLabel {
                color: #333333;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #c0c0c0;
                border-radius: 5px;
                padding: 5px 15px;
                min-width: 70px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            #yesButton {
                background-color: #ff4d4d;
                color: white;
                border: none;
            }
            #yesButton:hover {
                background-color: #ff3333;
            }
        """)

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Are you sure you want to log out?")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        button_layout = QtWidgets.QHBoxLayout()
        self.yes_button = QtWidgets.QPushButton("Yes")
        self.yes_button.setObjectName("yesButton")  # For the red styling
        self.no_button = QtWidgets.QPushButton("No")

        button_layout.addWidget(self.yes_button)
        button_layout.addWidget(self.no_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.yes_button.clicked.connect(self.accept)
        self.no_button.clicked.connect(self.reject)

class PopulationCharts(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.age_chart_layout = QtWidgets.QVBoxLayout()
        self.age_figure = Figure(figsize=(4, 3), dpi=80)
        self.age_canvas = FigureCanvas(self.age_figure)
        self.age_chart_layout.addWidget(self.age_canvas)

        self.purok_chart_layout = QtWidgets.QVBoxLayout()
        self.purok_figure = Figure(figsize=(4, 3), dpi=80)
        self.purok_canvas = FigureCanvas(self.purok_figure)
        self.purok_chart_layout.addWidget(self.purok_canvas)

    def update_age_chart(self, minors, adults, seniors):
        # Remove all existing axes and clear the figure
        self.age_figure.clf()

        # Create a new axes
        ax = self.age_figure.add_subplot(111)

        total = minors + adults + seniors

        if total == 0:
            ax.text(0.5, 0.5, 'No Data Available', ha='center', va='center', fontsize=10)
            ax.axis('off')
            self.age_canvas.draw()
            return

        labels = ['Minors (0-18)', 'Adults (19-59)', 'Seniors (60+)']
        sizes = [minors, adults, seniors]
        colors = ['#ff9999', '#66b3ff', '#99ff99']

        wedges, texts, autotexts = ax.pie(sizes, colors=colors, autopct='%1.1f%%',
                                          startangle=90, textprops={'fontsize': 8})

        ax.set_title('Population by Age Group', fontsize=10, fontweight='bold', pad=10)

        ax.legend(wedges, labels, title="Age Groups",
                  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=8)

        ax.axis('equal')

        self.age_figure.subplots_adjust(right=0.7)
        self.age_canvas.draw()

    def update_purok_chart(self, purok_data):
        self.purok_figure.clear()

        if not purok_data:
            ax = self.purok_figure.add_subplot(111)
            ax.text(0.5, 0.5, 'No purok data available', ha='center', va='center')
            ax.axis('off')
            self.purok_canvas.draw()
            return

        purok_names = [str(item[0]) for item in purok_data]
        purok_counts = [item[1] for item in purok_data]

        ax = self.purok_figure.add_subplot(111)

        color_list = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
                      '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2']

        colors = [color_list[i % len(color_list)] for i in range(len(purok_names))]

        bars = ax.bar(purok_names, purok_counts, color=colors, alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height,
                    f'{int(height)}', ha='center', va='bottom', fontsize=8)

        ax.set_xlabel('Purok', fontsize=9)
        ax.set_ylabel('Population', fontsize=9)
        ax.set_title('Population by Purok', fontsize=10, fontweight='bold')
        ax.tick_params(axis='x', rotation=45, labelsize=8)
        ax.tick_params(axis='y', labelsize=8)

        from matplotlib.patches import Patch
        legend_elements = [Patch(facecolor=colors[i], alpha=0.7, label=name)
                           for i, name in enumerate(purok_names)]

        if len(legend_elements) <= 10:
            ax.legend(handles=legend_elements, loc='upper right', fontsize=8)
        else:
            ax.legend(['Population by Purok'], loc='upper right')

        self.purok_figure.tight_layout()
        self.purok_canvas.draw()

class DashboardSecretary(QtWidgets.QDialog):
    logout_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = dashboard_Secretary()
        self.ui.setupUi(self)

        self.charts = PopulationCharts()

        self.setup_charts()

        self.view_population_window = None

        self.update_date_time()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)

        self.load_population_data()
        self.ui.viewPopulation_Button.clicked.connect(self.open_view_population)
        self.ui.register_Button.clicked.connect(self.open_register_resident)
        self.ui.generateReports_Button.clicked.connect(self.open_generate_reports)
        self.ui.home_Button_2.clicked.connect(self.refresh_dashboard)
        self.ui.logout_Button.clicked.connect(self.handle_logout)
        self.setup_refresh_button()

    def setup_charts(self):
        if self.ui.populationByAge.layout() is not None:
            QtWidgets.QWidget().setLayout(self.ui.populationByAge.layout())
        if self.ui.populationPurok.layout() is not None:
            QtWidgets.QWidget().setLayout(self.ui.populationPurok.layout())

        age_layout = QtWidgets.QVBoxLayout()
        age_layout.addWidget(self.charts.age_canvas)
        self.ui.populationByAge.setLayout(age_layout)

        purok_layout = QtWidgets.QVBoxLayout()
        purok_layout.addWidget(self.charts.purok_canvas)
        self.ui.populationPurok.setLayout(purok_layout)

    def setup_refresh_button(self):
        self.refresh_button = QtWidgets.QPushButton("Refresh Data", parent=self)
        self.refresh_button.setGeometry(QtCore.QRect(290, 720, 100, 30))
        self.refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px;
                font-weight: bold;
                font-family: 'Segoe UI';
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.refresh_button.clicked.connect(self.load_population_data)

    def refresh_dashboard(self):
        self.load_population_data()

    def load_population_data(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()

            #Total Population
            cursor.execute("SELECT COUNT(*) FROM residents WHERE is_deceased = 0")
            total_population = cursor.fetchone()[0]
            self.ui.totalPopulationNum.setText(str(total_population))

            #Total Households
            cursor.execute("""
                SELECT COUNT(DISTINCT ra.house_id) 
                FROM residents r
                LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
                WHERE ra.house_id IS NOT NULL AND ra.house_id != ''
            """)
            total_households = cursor.fetchone()[0]
            self.ui.totalHouseHoldNum.setText(str(total_households))

            #Total Men
            cursor.execute("SELECT COUNT(*) FROM residents WHERE sex IN ('Male', 'M', 'male') AND is_deceased = 0")
            total_men = cursor.fetchone()[0]
            self.ui.numMen.setText(str(total_men))

            #Total Women
            cursor.execute("SELECT COUNT(*) FROM residents WHERE sex IN ('Female', 'F', 'female') AND is_deceased = 0")
            total_women = cursor.fetchone()[0]
            self.ui.womenNum.setText(str(total_women))

            #Total Seniors
            cursor.execute("""
                SELECT COUNT(*) FROM residents 
                WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) >= 60 
                AND is_deceased = 0
            """)
            total_seniors = cursor.fetchone()[0]
            self.ui.seniorsNum.setText(str(total_seniors))

            #Total PWD
            cursor.execute("SELECT COUNT(*) FROM residents WHERE is_pwd = 1 AND is_deceased = 0")
            total_pwd = cursor.fetchone()[0]
            self.ui.pwdNum.setText(str(total_pwd))

            #Total Minors
            cursor.execute("""
                SELECT COUNT(*) FROM residents 
                WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) < 18 
                AND is_deceased = 0
            """)
            total_minors = cursor.fetchone()[0]
            self.ui.minorsNum.setText(str(total_minors))

            #Total Adults
            cursor.execute("""
                SELECT COUNT(*) FROM residents
                WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 19 AND 59 
                AND is_deceased = 0
            """)
            total_adults = cursor.fetchone()[0]
            self.ui.numAdult.setText(str(total_adults))

            self.update_charts(total_minors, total_adults, total_seniors)
            self.load_purok_distribution()

            conn.close()

        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            self.set_default_values()
        except Exception as e:
            print(f"Error loading population data: {e}")
            self.set_default_values()

    def set_default_values(self):
        self.ui.totalPopulationNum.setText("0")
        self.ui.totalHouseHoldNum.setText("0")
        self.ui.numMen.setText("0")
        self.ui.womenNum.setText("0")
        self.ui.seniorsNum.setText("0")
        self.ui.pwdNum.setText("0")
        self.ui.minorsNum.setText("0")
        self.ui.numAdult.setText("0")

        self.update_charts(0, 0, 0)

    def update_charts(self, minors, adults, seniors):
        self.charts.update_age_chart(minors, adults, seniors)

    def load_purok_distribution(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT ra.purok, COUNT(*) 
                FROM residents r
                JOIN resident_addresses ra ON r.resident_id = ra.resident_id 
                WHERE r.is_deceased = 0 
                GROUP BY ra.purok
            """)

            purok_data = cursor.fetchall()
            conn.close()

            self.charts.update_purok_chart(purok_data)

        except mysql.connector.Error as e:
            print(f"Database error loading purok data: {e}")
            self.charts.update_purok_chart([])
        except Exception as e:
            print(f"Error loading purok distribution: {e}")
            self.charts.update_purok_chart([])

    def handle_logout(self):
        dialog = LogoutConfirmDialog(self)

        if dialog.exec():
            self.logout_requested.emit()
            self.close()

    def update_date_time(self):
        now = datetime.now()
        date_time_str = now.strftime("%A, %b %d, %Y | %I:%M:%S %p")
        self.ui.dateTime_Label.setText(date_time_str)

    def show_from_population(self):
        if self.view_population_window:
            self.view_population_window.close()
            self.view_population_window = None
        self.show()
        self.raise_()
        self.activateWindow()

    def open_view_population(self):
        from controller.ViewPopulation.viewPopulationController_Secretary import ViewPopulationController

        self.view_population_window = ViewPopulationController(dashboard_reference=self)
        self.view_population_window.dashboard_requested.connect(self.show_from_population)
        self.hide()
        self.view_population_window.show()

    def open_register_resident(self):
        from controller.RegisterResident.registerResidentController_Secretary import RegisterResidentController

        if hasattr(self, 'register_page') and self.register_page:
            self.register_page.deleteLater()
            self.register_page = None

        self.register_page = RegisterResidentController(parent=self)
        self.hide()

        self.register_page.dashboard_requested.connect(self.show)

        self.register_page.logout_requested.connect(self.logout_requested.emit)

        self.register_page.show()

    def open_generate_reports(self):
        from controller.GenerateReport.generateReportController_Secretary import GenerateReportController
        self.hide()
        self.reports_page = GenerateReportController()

        self.reports_page.dashboard_requested.connect(self.show)
        self.reports_page.logout_requested.connect(self.logout_requested.emit)
        self.reports_page.show()

    def closeEvent(self, event):
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()

        plt.close('all')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    controller = DashboardSecretary()
    controller.show()
    sys.exit(app.exec())