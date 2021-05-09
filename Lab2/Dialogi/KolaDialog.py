import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class KolaWidget(QWidget):
    def __init__(self, cs1 = 50, cs2 = 200, parent = None):
    # def __init__(self, parent = None):
        super(KolaWidget, self).__init__(parent)
        # self.resize(200,200)
        
        self.circleSize1 = self.parent().circleSize1
        self.circleSize2 = self.parent().circleSize2
        self.color = '#FF0000'
        # self.setStyleSheet("background: green ")
        self.show()
    def changeBackground(self, color):
        self.color = color
    def paintEvent(self, eventQPaintEvent):
        
        col = QColor(0, 0, 0)
        col.setNamedColor(self.color)

        self.circleSize1 = self.parent().circleSize1
        self.circleSize2 = self.parent().circleSize2
        path = QPainterPath()

        x = self.size().width() // 2 # namierzanie środka okna
        y = self.size().height() // 2 # namierzanie środka okna

        path.addEllipse(x - (self.circleSize1 // 2), y - (self.circleSize1 // 2), self.circleSize1, self.circleSize1)
        path.addEllipse(x - (self.circleSize2 // 2), y - (self.circleSize2 // 2), self.circleSize2, self.circleSize2)
        painter = QPainter()
        painter.begin(self)

        painter.setBrush(col)
        painter.drawRect(0, 0, self.parent().size().width(), self.parent().size().height())

        painter.setBrush(QColor(128, 128, 128))
        painter.drawPath(path)
        painter.end()
        s = max(self.circleSize1, self.circleSize2)
        self.resize(self.parent().size().width(), self.parent().size().height())
        self.update()

class KolaWidgetZweite(QWidget):
    def __init__(self, cs1 = 50, cs2 = 200, parent = None):
    # def __init__(self, parent = None):
        super(KolaWidgetZweite, self).__init__(parent)
        # self.resize(200,200)
        
        self.circleSize1 = self.parent().circleSize1
        self.circleSize2 = self.parent().circleSize2
        # self.setStyleSheet("background: green ")
        self.show()
    def paintEvent(self, eventQPaintEvent):

        self.circleSize1 = self.parent().circleSize1Temp
        self.circleSize2 = self.parent().circleSize2Temp
        path = QPainterPath()

        x = self.size().width() // 2 # namierzanie środka okna
        y = self.size().height() // 2 # namierzanie środka okna

        path.addEllipse(x - (self.circleSize1 // 2), y - (self.circleSize1 // 2), self.circleSize1, self.circleSize1)
        path.addEllipse(x - (self.circleSize2 // 2), y - (self.circleSize2 // 2), self.circleSize2, self.circleSize2)
        painter = QPainter()
        painter.begin(self)

        painter.setBrush(QColor(128, 128, 128))
        painter.drawPath(path)
        painter.end()
        s = max(self.circleSize1, self.circleSize2)
        self.resize(300, 300)
        self.update()
class Kola(QDialog):
    newCircleSignal = pyqtSignal(int, int)
    circleSize1 = 50
    circleSize2 = 200
    circleGirth = circleSize1 - circleSize2

    circleSize1Temp = circleSize1
    circleSize2Temp = circleSize2

    def myAccept(self):
        self.circleSize1 = self.circleSize1Temp
        self.circleSize2 = self.circleSize2Temp
        self.slider_change()
        self.accept()

    def myReject(self):
        self.circleSize1Temp = self.circleSize1
        self.circleSize2Temp = self.circleSize2
        self.reject()

    def __init__(self, parent = None):
        super(Kola, self).__init__(parent)
        
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setMaximum(255)
        self.slider1.setMinimum(0)
        self.slider1.setValue(self.circleSize1Temp)
        
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMaximum(255)
        self.slider2.setMinimum(0)
        self.slider2.setValue(self.circleSize2Temp)
        
        self.slider1Value = QLineEdit(str(self.circleSize1Temp))
        objValidator1 = QIntValidator(self)
        objValidator1.setRange(0, 255)
        self.slider1Value.setValidator(objValidator1)
        self.slider1Value.textChanged.connect(self.le_change1)

        self.slider1.valueChanged.connect(self.value1_change)
        
        self.slider2Value = QLineEdit(str(self.circleSize2Temp))
        objValidator2 = QIntValidator(self)
        objValidator2.setRange(0, 255)
        self.slider2Value.setValidator(objValidator2)
        self.slider2Value.textChanged.connect(self.le_change2)

        self.slider2.valueChanged.connect(self.value2_change)


        layout = QGridLayout(self)
        layout.setSpacing(10)

        layout.addWidget(self.slider1, 1, 0)
        layout.addWidget(self.slider1Value, 2, 0)
        layout.addWidget(self.slider2, 3, 0)
        layout.addWidget(self.slider2Value, 4, 0)
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.myAccept)
        buttons.rejected.connect(self.myReject)
        layout.addWidget(buttons, 5, 0)
        self.kp = KolaWidgetZweite(parent = self)
        layout.addWidget(self.kp, 6, 0)

        self.setGeometry(400, 400, 400, 500)

    # def paintEvent(self, e):
    #     x = self.size().width() // 2
    #     y = self.size().height() // 2
    #     r = min(x,y)- self.circleGirth// 2
        
    #     qp = QPainter()
    #     qp.begin(self)
    #     pen = QPen(QColor(128, 128, 128), self.circleGirth, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawEllipse(x-r, y-r, 2*r, 2*r)
    #     qp.end()
        
    def value1_change(self, value):
        self.circleSize1Temp = value
        self.slider1Value.setText(str(value))
        self.kp.update()
        
        # self.slider_change()
        
    def value2_change(self, value):
        self.circleSize2Temp = value
        self.slider2Value.setText(str(value))
        self.kp.update()
        # self.slider_change()
        

    def slider_change(self):
        self.newCircleSignal.emit(self.circleSize1, self.circleSize2)
    def le_change1(self, value):
        if not value:
            return
        self.slider1.setValue(int(value)) 
    def le_change2(self, value):
        if not value:
            return
        self.slider2.setValue(int(value)) 