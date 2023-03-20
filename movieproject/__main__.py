from PyQt6.QtWidgets import QApplication
from movieproject.screens.mainwindow.mainwindow import MainWindow
import sys

def __movieproject__():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    __movieproject__()

