from common import *


class MemberRosterMenu(QWidget):
    returnSignal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        # create layout
        self.menuLayout = QVBoxLayout()

        self.label = QLabel("This is the member roster!")
        self.backButton = QPushButton("Back")

        self.backButton.clicked.connect(self.returnToHomeSignal)

        self.menuLayout.addWidget(self.label)
        self.menuLayout.addWidget(self.backButton)
        self.setLayout(self.menuLayout)

    def returnToHomeSignal(self):
        self.returnSignal.emit(0)
