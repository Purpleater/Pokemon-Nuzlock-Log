from common import *


class MemberRosterMenu(QWidget):
    returnSignal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.memberListRaw = loadJson("DataFolder/SaveFiles/FrenchPMDNuzlock")["partyRoster"]

        # create layout
        self.menuLayout = QVBoxLayout()

        self.label = QLabel("This is the member roster!")
        self.memberList = QTableWidget(len(self.memberListRaw), 2, self)

        self.backButton = QPushButton("Back")

        self.backButton.clicked.connect(self.returnToHomeSignal)

        self.menuLayout.addWidget(self.label)
        self.menuLayout.addWidget(self.memberList)
        self.menuLayout.addWidget(self.backButton)
        self.setLayout(self.menuLayout)
        self.populateTable()

    def returnToHomeSignal(self):
        self.returnSignal.emit(0)

    def populateTable(self):

        for i in range(len(self.memberListRaw)):
            partyMember = self.memberListRaw[i]

            memberName = QTableWidgetItem(partyMember["name"])
            memberName.setFlags(memberName.flags() & Qt.ItemIsEditable)
            self.memberList.setItem(i, 0, memberName)

            print(partyMember["speciesID"])
            memberSpecies = QTableWidgetItem(getPokemonByID(partyMember["speciesID"])["name"])
            memberSpecies.setFlags(memberSpecies.flags() & Qt.ItemIsEditable)
            self.memberList.setItem(i, 1, memberSpecies)

