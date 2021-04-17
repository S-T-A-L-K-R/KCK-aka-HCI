import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.initUI()
        

    def initUI(self):               
        self.setCentralWidget(UserArea())
        # menubar = self.menuBar()
        # editMenu = menubar.addMenu('&Edycja')
        # viewMenu = menubar.addMenu('&Widok')
        # helpMenu = menubar.addMenu('Pomo&c')
        
        self.setGeometry(300, 300, 640, 500)
        self.setWindowTitle('Main window')    
        self.show()
        

class UserArea(QWidget):
    def __init__(self):
        super(UserArea, self).__init__()
        self.Display = QLineEdit()
        self.Display.setAlignment(Qt.AlignRight)
        self.KNumbers = QGridLayout() # Klawiatura
        self.Equation = "0"
        self.initUI()


    def initUI(self):
        vb = QVBoxLayout()
        self.setLayout(vb)
        vb.addWidget(QLCDNumber(0, self))
        

        number7 = QPushButton("7") 
        number7.clicked.connect(self.sieben)
        self.KNumbers.addWidget(number7  , 0, 0)
        self.KNumbers.addWidget(QPushButton("8")  , 0, 1)
        self.KNumbers.addWidget(QPushButton("9")  , 0, 2)
        self.KNumbers.addWidget(QPushButton("4")  , 1, 0)
        self.KNumbers.addWidget(QPushButton("5")  , 1, 1)
        self.KNumbers.addWidget(QPushButton("6")  , 1, 2)
        self.KNumbers.addWidget(QPushButton("1")  , 2, 0)
        self.KNumbers.addWidget(QPushButton("2")  , 2, 1)
        self.KNumbers.addWidget(QPushButton("3")  , 2, 2)
        self.KNumbers.addWidget(QPushButton("+/-"), 3, 0)
        self.KNumbers.addWidget(QPushButton("0")  , 3, 1)
        self.KNumbers.addWidget(QPushButton(",")  , 3, 2)
        
        KSigns = QGridLayout() # Klawiatura - symbole
        KSigns.addWidget(QPushButton(":")  , 0, 0)
        KSigns.addWidget(QPushButton("x")  , 1, 0)
        KSigns.addWidget(QPushButton("-")  , 2, 0)
        KSigns.addWidget(QPushButton("+")  , 3, 0)
        KSigns.addWidget(QPushButton("DEL"), 0, 1)
        KSigns.addWidget(QPushButton("C")  , 1, 1)
        KSigns.addWidget(QPushButton("^2") , 2, 1)
        KSigns.addWidget(QPushButton("=")  , 3, 1)

        DisplayBox = QGridLayout()
        
        
        # self.Display.setFixedHeight(35)
        # Display.setAlignment(Qt.AlignRight)
        self.Display.setReadOnly(True)
        DisplayBox.addWidget(self.Display)

        hb = QHBoxLayout()
        vb.addStretch(1)
        vb.addLayout(DisplayBox)
        hb.addStretch(1)
        hb.addLayout(self.KNumbers)
        hb.addStretch(2)
        hb.addLayout(KSigns)
        vb.addStretch(1)
        vb.addLayout(hb)
        
    def click(self):
        print(self.sender().text())
    def sieben(self):
        print("xd")
        self.Display.setText("xd")
    

def main():
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
