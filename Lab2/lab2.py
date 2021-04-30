import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from Dialogi.IkonaDialog import *
from Dialogi.KolaDialog import *
from Dialogi.KolorDialog import *

class Lab2(QMainWindow):
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
    def colorChange(self, text):
        self.frame.setStyleSheet("background:%s }" % str(text))
        
    def closeEvent(self, event):
        self.colorWindow.done(0)
        event.accept()

    def initUI(self): 
        
        self.frame = QFrame()
        self.setCentralWidget(self.frame)
        # self.setLayout(frame)
        self.frame.setStyleSheet("""
                           background-color:red;""")
        menubar = self.menuBar() # Inicjalizowanie menu
        dialogsMenu = menubar.addMenu('&Dialogi') # Dodanie do menu listy "Dialogi"

        self.colorWindow = Kolor() # Tworzenie okna "Kolory"
        self.colorWindow.newColorSignal.connect(self.colorChange)

        self.colorsAction = QAction('Kolory', self, checkable = True) # Stworzenie akcji "Kolory"
        self.colorsAction.triggered.connect(self.launchColors) # Podpięcie "Kolorów" pod przycisk
        dialogsMenu.addAction(self.colorsAction) # Dodanie do listy pozycji "Kolory"
        
        
        self.setGeometry(300, 300, 640, 500)
        self.setWindowTitle('Main window')    
        self.show()
        #sposob 1
        #d = Dialogi.IkonaDialog.Ikona()
    


def main():
    app = QApplication(sys.argv)
    ex = Lab2()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
