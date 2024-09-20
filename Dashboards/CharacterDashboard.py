from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit

class CharacterDashboard(QWidget):
    def __init__(self, character_sheet):
        super().__init__()

        self.character_sheet = character_sheet
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Add character-related widgets here
        layout.addWidget(QLabel("Character Information"))
        
        self.name_input = QLineEdit()
        self.name_input.setText(self.character_sheet.name)
        layout.addWidget(QLabel('Name:'))
        layout.addWidget(self.name_input)

        # Add other widgets and logic for this dashboard

        self.setLayout(layout)