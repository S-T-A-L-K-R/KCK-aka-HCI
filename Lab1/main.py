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
        self.KNumbersPattern = [['7','8','9'],
                                ['4','5','6'],
                                ['1','2','3'],
                                ['+/-','0',',']]
        self.KNumbersButtons = [[QPushButton() for y in self.KNumbersPattern[0]] for x in self.KNumbersPattern]
        # Matrix = [[0 for x in range(w)] for y in range(h)] 
        self.KSignsPattern = [[':','<x]'],
                              ['*','C'],
                              ['-','^2'],
                              ['+','=']]
        self.KSignsButtons = [[QPushButton() for y in self.KSignsPattern[0]] for x in self.KSignsPattern]
        self.initDisplay() # Add Display
        self.initKNumbers() # Add numeric keyboard
        self.initKSigns() # Add special keyboard
        
        self.Equation = "0"
        self.initUI()
    def initDisplay(self):
        self.Display = QLineEdit()
        self.Display.setAlignment(Qt.AlignRight)

    def initKNumbers(self):
        self.KNumbers = QGridLayout() # Klawiatura
        for rownum, row in enumerate(self.KNumbersPattern):
            for columnnum, sign in enumerate(row):
                self.KNumbersButtons[rownum][columnnum] = QPushButton(sign)
                self.KNumbersButtons[rownum][columnnum].clicked.connect(self.sieben) # TODO Sieben na normalną funkcję
                self.KNumbers.addWidget(self.KNumbersButtons[rownum][columnnum], rownum, columnnum)

    def initKSigns(self):
        self.KSigns = QGridLayout() # Klawiatura
        for rownum, row in enumerate(self.KSignsPattern):
            for columnnum, sign in enumerate(row):
                self.KSignsButtons[rownum][columnnum] = QPushButton(sign)
                self.KSignsButtons[rownum][columnnum].clicked.connect(self.sieben) # TODO Sieben na inną funkcję
                self.KSigns.addWidget(self.KSignsButtons[rownum][columnnum], rownum, columnnum)

    def initUI(self):
        vb = QVBoxLayout()
        self.setLayout(vb)
        vb.addWidget(QLCDNumber(0, self))
        
        
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
