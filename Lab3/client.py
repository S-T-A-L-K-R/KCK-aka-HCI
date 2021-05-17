import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Widgets.circle import *
# VBox
# suwak
# widget z kołem
# pasek menu
    # łączenie z serwerem

class Lab3Client(QMainWindow):
    circleSize = 50
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def circleChange(self, circle1):
        self.circleSize1 = circle1
        self.update()

    def initUI(self): 
        # Menu
        self.menubar = self.menuBar() # Inicjalizowanie menu
        self.dialogsMenu = self.menubar.addMenu('&Połączenie') # Dodanie do menu listy "Połączenie"
        self.connectAction = QAction("Połącz z serwerem", self) # Stworzenie akcji "Połącz z serwerem" # TODO nie hardcodowa nazwa
        self.dialogsMenu.addAction(self.connectAction) # Dodanie do listy "Połączenie" akcji "Połącz z serwerem"
        
        # Suwak
        self.bar = QSlider(Qt.Horizontal)
        self.bar.setMaximum(255)
        self.bar.setMinimum(0)
        self.bar.setValue(self.circleSize)

        self.bar.valueChanged.connect(self.bar_change) # Podpięcie paska pod zmienną odpowiadająca za zmianę wielkości koła

        # Koło
        self.kw = Circle(parent = self)

        # Layout
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.bar) # Dodanie suwaka do layoutu VBOX
        # self.vlayout.addSpacing(1)
        self.vlayout.addWidget(self.kw) # Dodanie koła do layoutu VBOX

        self.cwidget = QWidget() # Stworzenie Widgetu
        self.cwidget.setLayout(self.vlayout) # Ustawienie layoutu VBOX na widgecie
        self.setCentralWidget(self.cwidget) # Ustawienie widgetu jako "centralWidget"

        # Inne
        self.setGeometry(300, 300, 640, 500)
        self.setWindowTitle('Client')    


        self.show()
    def bar_change(self, value):
        self.circleSize = value
def main():
    app = QApplication(sys.argv)
    ex = Lab3Client()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
