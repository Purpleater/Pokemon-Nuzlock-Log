from common import *

class EditGameSaveMenu(QWidget):
    returnSignal = pyqtSignal(int)
    def __init__(self):
        super().__init__()

        # create layout
        self.menuLayout = QVBoxLayout()

        self.label = QLabel("This is the edit game save menu!")
        self.saveList = QListWidget
        self.backButton = QPushButton("Back")

        self.backButton.clicked.connect(self.returnToHomeSignal)

        self.menuLayout.addWidget(self.label)
        self.menuLayout.addWidget(self.backButton)
        self.setLayout(self.menuLayout)

    def returnToHomeSignal(self):
        self.returnSignal.emit(0)

    def loadSaveList(self):
        with open("Datafolder/SaveFiles", 'r') as file:
            print(file)