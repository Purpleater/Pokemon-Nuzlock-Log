from common import *


class CreditsPage(QWidget):
    def __init__(self):
        super().__init__()

        # create layout
        self.menuLayout = QVBoxLayout()

        self.label = QLabel("This is the credits page")

        self.menuLayout.addWidget(self.label)
        self.setLayout(self.menuLayout)