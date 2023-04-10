from typing import Optional
from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QFrame,  QListView, QPushButton, QVBoxLayout, QWidget
from ..row.row import Row

class Sidebar(QFrame): 
    def __init__(self,parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        navFrame = QFrame()
        amodel = QStringListModel()
        amodel.setStringList(["hello","how are you","john"])



        sidebarLayout = QVBoxLayout(self)
        trendingView = QListView()
        trendingView.setModel(amodel)
        continueView = QListView()
        continueView.setModel(amodel)
        newView = QListView()
        newView.setModel(amodel)

        trendingRow = Row("Trending")
        continueRow = Row("Continue")
        newRow = Row("NEW")



        



        """
        sidebarLayout.addWidget(trendingView)
        sidebarLayout.addWidget(continueView)
        """
        sidebarLayout.addWidget(trendingRow)
        sidebarLayout.addWidget(continueRow)
        sidebarLayout.addWidget(newRow)


        self.setObjectName("Sidebar")

