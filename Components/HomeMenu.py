from common import *

class HomeMenu(QWidget):
    showMenuSignal = pyqtSignal(int)
    quitApplicationSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        # create layout
        self.menuLayout = QVBoxLayout()

        self.currentGameDisplayedLabel = QLabel("This is eventually display the game file.")

        self.memberRosterButton = QPushButton("View Member Roster")
        self.editGameSaveButton = QPushButton("Edit Nuzlock File")
        self.creditsButton = QPushButton("Credits")
        self.exitApplicationButton = QPushButton("Exit")

        # connect buttons
        self.memberRosterButton.clicked.connect(lambda: self.emitShowMenuSignal(1))
        self.editGameSaveButton.clicked.connect(lambda: self.emitShowMenuSignal(2))
        self.creditsButton.clicked.connect(lambda: self.emitShowMenuSignal(3))
        self.exitApplicationButton.clicked.connect(self.quitApplication)

        self.menuLayout.addWidget(self.currentGameDisplayedLabel)
        self.menuLayout.addWidget(self.memberRosterButton)
        self.menuLayout.addWidget(self.editGameSaveButton)
        self.menuLayout.addWidget(self.creditsButton)
        self.menuLayout.addWidget(self.exitApplicationButton)

        self.setLayout(self.menuLayout)

    def emitShowMenuSignal(self, menuIndex):
        self.showMenuSignal.emit(menuIndex)

    def quitApplication(self):
        self.quitApplicationSignal.emit()


