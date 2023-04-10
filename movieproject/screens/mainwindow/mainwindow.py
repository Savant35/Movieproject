from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDockWidget, QFrame, QGridLayout, QMainWindow, QSizePolicy, QStackedLayout
from PyQt6.QtWidgets import QPushButton
from movieproject.screens.homescreen.home import Home
from movieproject.widgets.header.headerwidget import Header
from movieproject.widgets.sidebar.sidebarwidget import Sidebar

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainFrame = QFrame()
        mainFrame.setObjectName("QMainFrame")


        header = Header()
        sidemenu = Sidebar()
        home = Home()


        mainWindowFramelayout = QGridLayout(mainFrame)
        mainWindowFramelayout.addWidget(header,0,0,1,1,Qt.AlignmentFlag.AlignTop)
        mainWindowFramelayout.addWidget(home,1,0,1,1)
        mainWindowFramelayout.addWidget(sidemenu,0,1,-1,1,Qt.AlignmentFlag.AlignLeft)

        self.setCentralWidget(mainFrame)





        



        self.loadStylesheet()
        self.setWindowTitle("FilmFinder+")

    def loadStylesheet(self):
        with open("movieproject/screens/mainwindow/mainwindow.qss") as f:
            self.setStyleSheet(f.read())


