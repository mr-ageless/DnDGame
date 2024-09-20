from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QStackedWidget, QLabel
from CharacterSheet import CharacterSheet
from Dashboards.CharacterDashboard import CharacterDashboard
from Dashboards.StatsDashboard import StatsDashboard

class DnDApp(QWidget):
    def __init__(self):
        super().__init__()

        self.character_sheet = CharacterSheet()  # Create a CharacterSheet instance

        self.initUI()

    def initUI(self):
        self.setWindowTitle('AD&D 2nd Edition')

        # Main layout
        main_layout = QHBoxLayout()

        # Left-side layout for checkboxes (dashboard selection)
        left_layout = QVBoxLayout()

        # Create checkboxes for dashboards
        self.character_checkbox = QCheckBox("Character")
        self.stats_checkbox = QCheckBox("Stats")

        self.character_checkbox.stateChanged.connect(self.switch_dashboard)
        self.stats_checkbox.stateChanged.connect(self.switch_dashboard)

        left_layout.addWidget(self.character_checkbox)
        left_layout.addWidget(self.stats_checkbox)

        # Right-side layout for dashboards
        self.dashboard_stack = QStackedWidget()

        # Create the different dashboards
        self.character_dashboard = CharacterDashboard(self.character_sheet)
        self.stats_dashboard = StatsDashboard(self.character_sheet)

        # Add dashboards to the stack
        self.dashboard_stack.addWidget(self.character_dashboard)  # Index 0
        self.dashboard_stack.addWidget(self.stats_dashboard)      # Index 1

        # Add left and right layouts to main layout
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.dashboard_stack)

        # Set main layout
        self.setLayout(main_layout)

    def switch_dashboard(self):
        # Switch dashboard based on the selected checkbox
        if self.character_checkbox.isChecked():
            self.dashboard_stack.setCurrentIndex(0)  # Show Character dashboard
        elif self.stats_checkbox.isChecked():
            self.dashboard_stack.setCurrentIndex(1)  # Show Stats dashboard

if __name__ == '__main__':
    app = QApplication([])
    ex = DnDApp()
    ex.show()
    app.exec_()
