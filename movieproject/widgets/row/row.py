from typing import Optional
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QListView, QPushButton, QSizePolicy, QVBoxLayout, QWidget


class Row(QFrame):
    def __init__(self,title: str,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        navFrame = QFrame()
        titelLabel = QLabel(title)
        rowview = QListView()

        leftNavButton = QPushButton()
        leftNavButton.setIcon(QIcon("movieproject/widgets/row/assets/back.png"))
        leftNavButton.setIconSize(QSize(24,24))
        leftNavButton.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        
        rightNavButton = QPushButton()
        rightNavButton.setIcon(QIcon("movieproject/widgets/row/assets/back-rotated.png"))
        rightNavButton.setIconSize(QSize(24,24))
        rightNavButton.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)




        navFrameLayout = QHBoxLayout(navFrame)
        navFrameLayout.addWidget(titelLabel)
        navFrameLayout.addWidget(leftNavButton)
        navFrameLayout.addWidget(rightNavButton)
        navFrameLayout.setContentsMargins(0,0,0,0)
        navFrameLayout.setSpacing(0)
        
        rowLayout = QVBoxLayout(self)
        rowLayout.addWidget(navFrame)
        rowLayout.addWidget(rowview)
        rowLayout.setSpacing(10)
        rowLayout.setContentsMargins(0,0,0,0)









