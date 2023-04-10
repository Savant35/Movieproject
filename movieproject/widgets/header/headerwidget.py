
from typing import Optional
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QWidget
class Header(QFrame): 
    def __init__(self,parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        frame = QFrame()
        
        
        logoButton = QPushButton("FilmFinder+")
        logoButton.setObjectName("logoButton")
        movieButton = QPushButton("movie")
        seriesButton = QPushButton("series")
        homeButton = QPushButton("Home")

        frameLayout: QHBoxLayout = QHBoxLayout(frame)
        frameLayout.addWidget(logoButton)
        frameLayout.addWidget(homeButton)
        frameLayout.addWidget(movieButton)
        frameLayout.addWidget(seriesButton)

        headerLayout = QHBoxLayout(self)
        """
        headerLayout.addWidget(ticketLabel)
        headerLayout.addWidget(movieButton)
        headerLayout.addWidget(newsButton)
        headerLayout.addWidget(trendingButton)
        headerLayout.addWidget(seriesButton)
        """


        headerLayout.addWidget(frame)
        self.setObjectName("Header")
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,QSizePolicy.Policy.Fixed)
       
       # self.setLayout(headerLayout) alternative way

               
