import Components.HomeMenu
import Components.MemberRosterMenu
import Components.EditGameSaveMenu
import Components.CreditsPage

from common import *

# import other menu components


class MainApplication(QMainWindow):

    def __init__(self):
        super().__init__()

        # create main layout
        self.mainLayout = QStackedLayout()

        # initialize other widgets into main application
        self.homeMenu = Components.HomeMenu.HomeMenu()
        self.memberRosterMenu = Components.MemberRosterMenu.MemberRosterMenu()
        self.editGameSaveMenu = Components.EditGameSaveMenu.EditGameSaveMenu()
        self.creditsPage = Components.CreditsPage.CreditsPage()

        # add the other menus to the stacked layout
        self.mainLayout.addWidget(self.homeMenu)
        self.mainLayout.addWidget(self.memberRosterMenu)
        self.mainLayout.addWidget(self.editGameSaveMenu)
        self.mainLayout.addWidget(self.creditsPage)

        # create signal slots that allow for the changing of the menus
        self.homeMenu.showMenuSignal.connect(self.showMenu)
        self.memberRosterMenu.returnSignal.connect(self.showMenu)
        self.editGameSaveMenu.returnSignal.connect(self.showMenu)
        self.creditsPage.returnSignal.connect(self.showMenu)

        #... and quitting
        self.homeMenu.quitApplicationSignal.connect(self.exitApplication)

        # create a central widget for the application
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.setGeometry(200, 200, 300, 300)
        self.showMenu(0)

    def showMenu(self, index):
        # self.mainLayout.setCurrentIndex(index)
        self.setWindowTitle(f"Pokemon Nuzlock Log - {signalToMenuIndex[index]}")
        self.mainLayout.setCurrentIndex(index)

    def exitApplication(self):
        QApplication.quit()


def main():
    app = QApplication(sys.argv)
    mainApplication = MainApplication()
    mainApplication.show()
    sys.exit((app.exec_()))


if __name__ == "__main__":
    main()
