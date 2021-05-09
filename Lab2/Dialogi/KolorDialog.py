import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *


class StyledItemDelegate(QStyledItemDelegate):
    def __init__(self, pattern=None, parent=None):
        QStyledItemDelegate.__init__(self, parent=parent)
        self.pattern = pattern
    def paint(self, painter, option, index):
        for i, j in enumerate(self.pattern.values()):
            if index.row() == i:
                painter.save()
                painter.fillRect(option.rect, QBrush(QColor(j)))
                painter.restore()
        QStyledItemDelegate.paint(self, painter, option, index)

class Kolor(QDialog):
    newColorSignal = pyqtSignal(str)

    def closeEvent(self, event):
        event.ignore()
    def sendColor(self, text):
        self.newColorSignal.emit(self.pattern[text])

    def __init__(self, parent = None):
        super(Kolor, self).__init__(parent)
        # self.modal = False
        self.pattern = {"Czerwony"  : "#FF0000",
                        "Zielony"   : "#00FF00",
                        "Niebieski" : "#0000FF",
                        "Żółty"     : "#FFFF00"}

        self.colorList = QComboBox()
        for x, y in self.pattern.items():
            self.colorList.addItem(x)
        self.colorList.activated[str].connect(self.sendColor)
        # combo = QComboBox()
        # model = QSqlTableModel()
        # model.setTable("table")
        # combo.setModel(model)
        self.colorList.setItemDelegate(StyledItemDelegate(self.pattern))

        # self.colorList.setStyleSheet("""
        # background-color:red;""")
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(self.colorList)

        self.setGeometry(400, 400, 50, 50)
