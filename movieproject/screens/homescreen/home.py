from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QLabel,  QVBoxLayout, QWidget
from movieproject.widgets.row.row import Row

class Home (QFrame):
    def __init__(self,parent: Optional[QWidget]=None):
        super().__init__(parent=parent)

        row = Row("Popular movies")
        banner = QLabel()
        banner.setPixmap(QPixmap("movieproject/assets/avatar.avif"))
        banner.setScaledContents(True)
        banner.setFixedSize(600,400)

        homelayout = QVBoxLayout(self)
        homelayout.addWidget(banner,6)
        homelayout.addWidget(row,4)
        homelayout.setContentsMargins(0,0,0,0)
        homelayout.setContentsMargins(0,0,0,0)
        homelayout.setSpacing(20)



