
from typing import Optional
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QWidget
class Header(QFrame): 
    def __init__(self,parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        netflixLabel = QLabel()
        netflixLabel.setPixmap(QPixmap("movieproject/widgets/header/assets/netflixlogo.png"))
        
        movieButton = QPushButton("movie")
        newsButton = QPushButton("news")
        trendingButton = QPushButton("trending")
        seriesButton = QPushButton("series")

        headerLayout = QHBoxLayout(self)
        headerLayout.addWidget(netflixLabel)
        headerLayout.addWidget(movieButton)
        headerLayout.addWidget(newsButton)
        headerLayout.addWidget(trendingButton)
        headerLayout.addWidget(seriesButton)

        self.setObjectName("Header")

       
       # self.setLayout(headerLayout) alternative way

               
