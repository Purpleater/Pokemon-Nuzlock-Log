from common import *


class MemberRosterMenu(QWidget):
    returnSignal = pyqtSignal(int)

    genderKey ={
        "Male": "♂",
        "Female": "♀",
        "-": "—"
    }
    def __init__(self):
        super().__init__()

        self.memberListRaw = loadJson("DataFolder/SaveFiles/FrenchPMDNuzlock")["partyRoster"]

        # create layout
        self.menuLayout = QVBoxLayout()
        self.mainContainer = QHBoxLayout()
        self.memberDetails = QVBoxLayout()

        # widgets
        self.memberList = QListWidget()
        self.backButton = QPushButton("Back")

        self.memberName = QLabel("meese")
        self.memberGender = QLabel("moose")
        self.memberSpeciesName = QLabel("mess")
        self.memberSpeciesImage = QLabel()


        # connect widgets to event procedures
        self.backButton.clicked.connect(self.returnToHomeSignal)
        self.memberList.itemClicked.connect(self.showMemberInformation)

        # add widgets to the mainContainer
        self.mainContainer.addWidget(self.memberList)
        self.mainContainer.addLayout(self.memberDetails)

        # add widgets to memberDetails
        self.memberDetails.addWidget(self.memberName)
        self.memberDetails.addWidget(self.memberGender)
        self.memberDetails.addWidget(self.memberSpeciesName)
        # set layouts
        self.menuLayout.addLayout(self.mainContainer)
        self.menuLayout.addWidget(self.backButton)
        self.setLayout(self.menuLayout)
        self.populateMemberList()

    def returnToHomeSignal(self):
        self.returnSignal.emit(0)


    def populateMemberList(self):
        for i in range(len(self.memberListRaw)):
            self.memberList.addItem(self.memberListRaw[i]["name"])

    def showMemberInformation(self):
        memberName = self.memberList.selectedItems()[0].text()
        memberInfo = next((pokemon for pokemon in self.memberListRaw if pokemon["name"] == memberName))
        memberSpecies = getPokemonByID(memberInfo['speciesID'])

        self.memberName.setText(f"Name: {memberInfo['name']}")
        self.memberGender.setText(f"Gender: {self.genderKey[memberInfo['gender']]}")
        self.memberSpeciesName.setText(f"Species: {memberSpecies['name']}")

        memberPortrait = QPixmap(f"PortraitDirectory/{memberSpecies['imageID']}")
        self.memberSpeciesImage.setPixmap(memberPortrait)
        self.memberSpeciesImage.update()



