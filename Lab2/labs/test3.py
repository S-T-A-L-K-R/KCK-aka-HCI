from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt 
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.gr = 30

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.setStyleSheet("background-color:#00FF80")
        self.show()

    def paintEvent(self, e):
        x = self.size().width() // 2
        y = self.size().height() // 2
        r = min(x,y)- self.gr// 2
        
        qp = QPainter()
        qp.begin(self)
        pen = QPen(QColor(128, 128, 128), self.gr, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawEllipse(x-r, y-r, 2*r, 2*r)
        qp.end()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()