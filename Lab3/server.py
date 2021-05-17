# VBox
# status serwera
# widget z kołem
# pasek menu
    # włączanie/wyłączanie serwera - checked

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Widgets.circle import *

class Lab3Server(QMainWindow):
    circleSize = 50
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def launchServer(self):
        if self.connectAction.isChecked():
            self.bar.setText('Serwer jest włączony')
            self.connectAction.setText('Wyłącz serwer')
        else:
            self.bar.setText('Serwer jest wyłączony')
            self.connectAction.setText('Uruchom serwer')
        
        self.update()
    def initUI(self): 
        # Menu
        self.menubar = self.menuBar() # Inicjalizowanie menu
        self.dialogsMenu = self.menubar.addMenu('&Serwer') # Dodanie do menu listy "Serwer"
        self.connectAction = QAction("Uruchom serwer", self, checkable = True) # Stworzenie akcji "Uruchom serwer"
        self.connectAction.triggered.connect(self.launchServer)

        self.dialogsMenu.addAction(self.connectAction) # Dodanie do listy "Serwer" akcji "Uruchom serwer"
        
        # Status
        self.bar = QLabel()
        self.bar.setText('Serwer jest wyłączony')
        self.bar.setFixedHeight(20)
        # self.bar.valueChanged.connect(self.bar_change) # Podpięcie paska pod zmienną odpowiadająca za zmianę wielkości koła

        # Koło
        self.kw = Circle(parent = self)

        # Layout
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.bar) # Dodanie QLabela do layoutu VBOX
        self.vlayout.addWidget(self.kw) # Dodanie koła do layoutu VBOX
        

        self.cwidget = QWidget() # Stworzenie Widgetu
        self.cwidget.setLayout(self.vlayout) # Ustawienie layoutu VBOX na widgecie
        self.setCentralWidget(self.cwidget) # Ustawienie widgetu jako "centralWidget"

        # Inne
        self.setGeometry(300, 300, 640, 500)
        self.setWindowTitle('Client')

        self.show()
def main():
    app = QApplication(sys.argv)
    ex = Lab3Server()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()