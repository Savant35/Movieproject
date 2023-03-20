from typing import Optional
from PyQt6.QtWidgets import QFrame, QPushButton, QWidget


class Sidebar(QFrame): 
    def __init__(self,parent: Optional[QWidget]) -> None:
        super().__init__(parent=parent)

        playbutton = QPushButton()
        
