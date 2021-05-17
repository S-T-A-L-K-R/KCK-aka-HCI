import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Circle(QWidget):
    def __init__(self, parent = None):
        super(Circle, self).__init__(parent)
        self.resize(100, 100)
        self.show()

    def paintEvent(self, eventQPaintEvent):

        circleSize = self.parent().parent().circleSize
        path = QPainterPath()

        x = self.size().width() // 2 # namierzanie środka okna
        y = self.size().height() // 2 # namierzanie środka okna
        # x = 20
        # y = 20
        path.addEllipse(x - (circleSize // 2), y - (circleSize // 2), circleSize, circleSize)
        # path.addEllipse(40, 40, 20, 20)
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(128, 128, 128))
        painter.drawPath(path)
        painter.end()
        self.resize(self.parent().size().width(), self.parent().size().height())
        
        self.update()
        