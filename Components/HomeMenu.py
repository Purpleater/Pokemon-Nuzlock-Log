from common import *

class HomeMenu(QWidget):
    def __init__(self):
        super().__init__()

        # create layout
        self.menuLayout = QVBoxLayout()

        self.currentGameDisplayedLabel = QLabel("This is eventually display the game file.")
        self.memberRosterButton = QPushButton("View Member Roster")
        self.editGameSaveButton = QPushButton("Edit Nuzlock File")
        self.creditsButton = QPushButton("Credits")
        self.exitApplicationButton = QPushButton("Exit")

        # create menu signal
        self.showMenuSignal = pyqtSignal(int)

        self.menuLayout.addWidget(self.currentGameDisplayedLabel)
        self.menuLayout.addWidget(self.memberRosterButton)
        self.menuLayout.addWidget(self.editGameSaveButton)
        self.menuLayout.addWidget(self.creditsButton)
        self.menuLayout.addWidget(self.exitApplicationButton)

        self.setLayout(self.menuLayout)

    def emitShowMenuSignal(self, menuIndex):
        self.showMenuSignal.emit(menuIndex)


