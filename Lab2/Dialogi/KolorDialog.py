import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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

        # self.colorList.setStyleSheet("""
        # background-color:red;""")
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(self.colorList)

        self.setGeometry(400, 400, 50, 50)
