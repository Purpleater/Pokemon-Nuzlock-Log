from common import *

# import other menu components
from Components.HomeMenu import HomeMenu


class MainApplication(QMainWindow):

    def __init__(self):
        super().__init__()

        # create main layout
        self.mainLayout = QStackedLayout()

        # initialize other widgets into main application
        self.homeMenu = HomeMenu()

        # add the other menus to the stacked layout
        self.mainLayout.addWidget(self.homeMenu)

        # create a signal slot that allows for the changing of the menus
        self.homeMenu.showMenuSignal.connect(self.showMenu)

        # create a central widget for the application
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.showMenu(0)

    def showMenu(self, index):
        # self.mainLayout.setCurrentIndex(index)
        self.setWindowTitle(f"Pokemon Nuzlock Log - {signalToMenuIndex[index]}")






def main():
    app = QApplication(sys.argv)
    mainApplication = MainApplication()
    mainApplication.show()
    sys.exit((app.exec_()))


if __name__ == "__main__":
    main()
