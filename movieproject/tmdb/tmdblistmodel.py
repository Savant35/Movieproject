from PyQt6.QtCore import QAbstractListModel


class TMDBListModel(QAbstractListModel):
    def __init(self,tmdb = None, batch: int = 30, parent = None):
        super().__init__(parent=parent)


