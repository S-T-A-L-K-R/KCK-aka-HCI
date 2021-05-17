import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from Lab2.Dialogi.IkonaDialog import *
from Lab2.Dialogi.KolaDialog import *
from Lab2.Dialogi.KolorDialog import *

class Lab2(QMainWindow):
    circleSize1 = 50
    circleSize2 = 200
    def __init__(self):
        super().__init__()
        self.initUI()

    def launchIcon(self):
        d = Ikona()
        d.exec_()
    def launchColors(self):
        if self.colorsAction.isChecked():
            self.colorWindow.show()
        else:
            self.colorWindow.hide()
    def launchCircles(self):
        self.circlesWindow.show()
    def colorChange(self, text):
        self.kw.changeBackground(str(text))
        
    def closeEvent(self, event):
        self.colorWindow.done(0)
        event.accept()
    
    def circleChange(self, circle1, circle2):
        self.circleSize1 = circle1
        self.circleSize2 = circle2
        self.update()

    def initUI(self): 
        # TODO - kolor: brak koloru w podglądzie
        self.kw = KolaWidget(parent = self)
        
        # self.setCentralWidget(self.kw)

        # self.setCentralWidget(KolaWidget(self.circleSize1, self.circleSize2))
        # self.frame = QFrame()
        # self.setCentralWidget(self.frame)
        # self.ico = QIcon("img/emoji.png")
        self.setWindowIcon(QIcon('img/emoji.png'))
        # self.setStyleSheet("""background-color:red;""")
        menubar = self.menuBar() # Inicjalizowanie menu
        dialogsMenu = menubar.addMenu('&Dialogi') # Dodanie do menu listy "Dialogi"

        self.colorWindow = Kolor() # Tworzenie okna "Kolory"
        self.circlesWindow = Kola() # Tworzenie okna "Kola"
        self.colorWindow.newColorSignal.connect(self.colorChange) # Podpięcie tła pod sygnał z "Kolory"
        self.circlesWindow.newCircleSignal.connect(self.circleChange) # Podpięcie kół pod sygnał z "Kola"

        self.colorsAction = QAction('Kolory', self, checkable = True) # Stworzenie akcji "Kolory"
        self.colorsAction.triggered.connect(self.launchColors) # Podpięcie "Kolorów" pod przycisk
        dialogsMenu.addAction(self.colorsAction) # Dodanie do listy pozycji "Kolory"
        
        self.circlesAction = QAction('Koła', self) # Stworzenie akcji "Koła"
        self.circlesAction.triggered.connect(self.launchCircles) # Podpięcie "Koła" pod przycisk
        dialogsMenu.addAction(self.circlesAction) # Dodanie do listy pozycji "Koła"
        
        # xd = KolaWidget()
        # self.setCentralWidget(xd)
        self.setGeometry(300, 300, 640, 500)
        # self.setWindowTitle('Main window')    
        self.setWindowTitle('<----- ! ----->')    
        self.show()
        #sposob 1
        #d = Dialogi.IkonaDialog.Ikona()
    """
    def paintEvent(self, e):
        # x = self.circleSize1 // 2
        # y = self.circleSize2 // 2
        x = self.size().width() // 2 # namierzanie środka okna
        y = self.size().height() // 2 # namierzanie środka okna
        # r = min(self.circleSize1,self.circleSize2) - self.circleGirth // 2
        r = (self.circleSize1 + self.circleSize2) // 2 # obliczanie promienia elipsy
        
        qp = QPainter()
        qp.begin(self)
        pen = QPen(QColor(128, 128, 128), self.circleGirth, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawEllipse(x-(r//2), y-(r//2), r, r)
        # qp.drawRect(x-(r/2), y-(r/2), r, r)
        qp.end()
    """
    """
    def paintEvent(self, e):
        path = QPainterPath()
        path.addRect(200, 200, 60, 60)

        # path.moveTo(0, 0)
        path.cubicTo(99, 0,  50, 50,  99, 99)
        path.cubicTo(0, 99,  50, 50,  0, 0)

        painter = QPainter()
        painter.begin(self)
        painter.fillRect(0, 0, 100, 100, Qt.white)
        painter.setPen(QPen(QColor(79, 106, 25), 1, Qt.SolidLine,
                            Qt.FlatCap, Qt.MiterJoin))
        painter.setBrush(QColor(122, 163, 39))

        painter.drawPath(path)
        painter.end()
    """
    """
    def paintEvent(self, e):
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
    """
    # def paintEvent(self, e):
        # self.kw.move((self.size().width() - max(self.circleSize1, self.circleSize2)) // 2, (self.size().height() - max(self.circleSize1, self.circleSize2)) // 2)

def main():
    app = QApplication(sys.argv)
    ex = Lab2()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
