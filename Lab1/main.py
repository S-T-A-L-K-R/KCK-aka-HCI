from functools import partial
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
        
        self.setGeometry(300, 300, 640, 500)
        self.setWindowTitle('Main window')    
        self.show()
        

class UserArea(QWidget):
    def __init__(self):
        super(UserArea, self).__init__()
        self.Equation = "0"
        self.IsNegative = False
        self.Memory = "0"
        self.Sign = "\0"
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
        
        
        self.initUI()
    def initDisplay(self):
        self.DisplayEquation = QLineEdit()
        self.DisplayEquation.setAlignment(Qt.AlignRight)
        # self.Display.setFixedHeight(35)
        self.DisplayEquation.setReadOnly(True)

        self.DisplayMemory = QLineEdit()
        self.DisplayMemory.setAlignment(Qt.AlignRight)
        # self.Display.setFixedHeight(35)
        self.DisplayMemory.setReadOnly(True)
        self.DisplayEquation.setText(self.Equation)

    def initKNumbers(self):
        self.KNumbers = QGridLayout() # Klawiatura
        for rownum, row in enumerate(self.KNumbersPattern):
            for columnnum, sign in enumerate(row):
                self.KNumbersButtons[rownum][columnnum] = QPushButton(sign)
                # self.KNumbersButtons[rownum][columnnum].clicked.connect(lambda: self.ClickNumbers(sign)) 
                self.KNumbersButtons[rownum][columnnum].clicked.connect(partial(self.ClickNumbers, sign))
                self.KNumbers.addWidget(self.KNumbersButtons[rownum][columnnum], rownum, columnnum)

    def initKSigns(self):
        self.KSigns = QGridLayout() # Klawiatura
        for rownum, row in enumerate(self.KSignsPattern):
            for columnnum, sign in enumerate(row):
                self.KSignsButtons[rownum][columnnum] = QPushButton(sign)
                self.KSignsButtons[rownum][columnnum].clicked.connect(partial(self.ClickSigns, sign))
                self.KSigns.addWidget(self.KSignsButtons[rownum][columnnum], rownum, columnnum)

    def initUI(self):
        vb = QVBoxLayout()
        self.setLayout(vb)
        vb.addWidget(QLCDNumber(0, self))

        DisplayBox = QGridLayout()

        DisplayBox.addWidget(self.DisplayMemory)
        DisplayBox.addWidget(self.DisplayEquation)
        
        hb = QHBoxLayout()
        vb.addStretch(1)
        vb.addLayout(DisplayBox)
        hb.addStretch(1)
        hb.addLayout(self.KNumbers)
        hb.addStretch(2)
        hb.addLayout(self.KSigns)
        vb.addStretch(1)
        vb.addLayout(hb)
        
    def click(self):
        print(self.sender().text())
    def ClickNumbers(self, sign):
        print(sign)
        if sign not in {'+/-', ','}:
            if self.Equation[0] == '0':
                if len(self.Equation) > 1:
                    self.Equation = self.Equation + sign
                else:
                    self.Equation = sign
            else:
                self.Equation = self.Equation + sign
        elif sign == ',':
            if ',' not in self.Equation:
                self.Equation = self.Equation + sign
        else:
            self.IsNegative = not self.IsNegative
        self.EquationDisplay()

    def ClickSigns(self, sign):
        if sign == '<x]':
            if len(self.Equation) > 1:
                self.Equation = self.Equation[:-1]
            else:
                if self.Equation != '0':
                    self.Equation = '0'
        elif sign == 'C':
            self.Equation = '0'
            self.IsNegative = False
        elif sign == '^2':
            print("todo")
        elif sign == '=':
            print("todo")
        else: # + - * :
            self.Memory = self.Equation
            self.Operation = sign
            self.MemoryDisplay = self.Equation + ' ' + sign

        self.EquationDisplay()
    def EquationDisplay(self):
        if self.IsNegative:
            self.DisplayEquation.setText('-' + self.Equation)
        else:
            self.DisplayEquation.setText(self.Equation)

def main():
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
