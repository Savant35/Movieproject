from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QPushButton
from movieproject.widgets.header.headerwidget import Header

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        header = Header()
        self.setCentralWidget(header)
        

        self.loadStylesheet()
        self.setWindowTitle("My App")

    def loadStylesheet(self):
        with open("movieproject/screens/mainwindow/mainwindow.qss") as f:
            self.setStyleSheet(f.read())


