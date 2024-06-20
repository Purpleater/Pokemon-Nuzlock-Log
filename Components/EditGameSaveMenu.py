from common import *

class EditGameSaveMenu(QWidget):
    def __init__(self):
        super().__init__()

        # create layout
        self.menuLayout = QVBoxLayout()

        self.label = QLabel("This is the page where you edit which game save you're on")

        self.menuLayout.addWidget(self.label)
        self.setLayout(self.menuLayout)