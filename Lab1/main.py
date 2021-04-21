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
        self.Equation_1 = "0"
        self.Equation_2 = ""
        self.Operation = ""
        self.IsNegative = False
        
        self.CBoxesPattern_1 = [['Hex','Dec','Oct','Bin']]
        self.CBoxes_1 = [[QCheckBox() for y in self.CBoxesPattern_1[0]] for x in self.CBoxesPattern_1]
        self.CBoxesPattern_2 = [['Stopnie','Gradiany','Radiusy']]
        self.CBoxes_2 = [[QCheckBox() for y in self.CBoxesPattern_2[0]] for x in self.CBoxesPattern_2]
        self.KNumbersPattern = [['7','8','9'],
                                ['4','5','6'],
                                ['1','2','3'],
                                ['+/-','0','.']]
        self.KNumbersButtons = [[QPushButton() for y in self.KNumbersPattern[0]] for x in self.KNumbersPattern]
        # Matrix = [[0 for x in range(w)] for y in range(h)] 
        self.KSignsPattern = [['/','<x]'],
                              ['*','C'],
                              ['-','^2'],
                              ['+','=']]
        self.KSignsButtons = [[QPushButton() for y in self.KSignsPattern[0]] for x in self.KSignsPattern]

        self.KPPattern_0 = [['Sta'],
                               ['Ave'],
                               ['Sum'],
                               ['s'],
                               ['Dat']]
        self.KPButtons_0 = [[QPushButton() for y in self.KPPattern_0[0]] for x in self.KPPattern_0]

        self.KPPattern_1 = [['F-E','[',']'],
                               ['dms','Exp','ln'],
                               ['sin','x^y','log'],
                               ['cos','x^3','n!'],
                               ['tan','x^2','1/x']]
        self.KPButtons_1 = [[QPushButton() for y in self.KPPattern_1[0]] for x in self.KPPattern_1]

        self.KPPattern_2 = [['MC'],
                            ['MR'],
                            ['MS'],
                            ['M+']]
        self.KPButtons_2 = [[QPushButton() for y in self.KPPattern_2[0]] for x in self.KPPattern_2]

        self.KPPattern_top = [['A','B','C','D','E','F']]
        self.KPButtons_top = [[QPushButton() for y in self.KPPattern_top[0]] for x in self.KPPattern_top]
        
        self.initDisplay() # Add Display
        self.initKNumbers() # Add numeric keyboard
        self.initKSigns() # Add special keyboard
        self.initKP() # Add placeholders
        self.initCBoxes() # Add CheckBoxes
        
        
        self.initUI()
    def initCBoxes(self):
        self.CBLayout_1 = QGridLayout()
        self.CBGroup_1 = QButtonGroup()
        for rownum, row in enumerate(self.CBoxesPattern_1):
            for columnnum, sign in enumerate(row):
                self.CBoxes_1[rownum][columnnum] = QCheckBox(sign)
                self.CBLayout_1.addWidget(self.CBoxes_1[rownum][columnnum], rownum, columnnum, Qt.AlignLeft)
                self.CBGroup_1.addButton(self.CBoxes_1[rownum][columnnum])
                self.CBoxes_1[rownum][columnnum].setStyleSheet("""
                    background-color: white;
                """)
                if sign == 'Dec':
                    self.CBoxes_1[rownum][columnnum].setChecked(True)
        
        self.CBLayout_2 = QGridLayout()
        self.CBGroup_2 = QButtonGroup()
        for rownum, row in enumerate(self.CBoxesPattern_2):
            for columnnum, sign in enumerate(row):
                self.CBoxes_2[rownum][columnnum] = QCheckBox(sign)
                self.CBoxes_2[rownum][columnnum].setStyleSheet("""
                    background-color: green;
                """)
                self.CBLayout_2.addWidget(self.CBoxes_2[rownum][columnnum], rownum, columnnum)
                self.CBGroup_2.addButton(self.CBoxes_2[rownum][columnnum], Qt.AlignJustify)
                if sign == 'Stopnie':
                    self.CBoxes_2[rownum][columnnum].setChecked(True)
        # self.CBLayout_2.setStyleSheet("""
        #             border: solid;
        #             """)

    def initKP(self):
        self.KP_0 = QGridLayout()
        for rownum, row in enumerate(self.KPPattern_0):
            for columnnum, sign in enumerate(row):
                self.KPButtons_0[rownum][columnnum] = QPushButton(sign)
                # self.KNumbersButtons[rownum][columnnum].clicked.connect(partial(self.ClickNumbers, sign))
                self.KP_0.addWidget(self.KPButtons_0[rownum][columnnum], rownum, columnnum)
                self.KPButtons_0[rownum][columnnum].setStyleSheet("""
                        color: gray;
                    """)

        self.KP_1 = QGridLayout()
        for rownum, row in enumerate(self.KPPattern_1):
            for columnnum, sign in enumerate(row):
                self.KPButtons_1[rownum][columnnum] = QPushButton(sign)
                # self.KNumbersButtons[rownum][columnnum].clicked.connect(partial(self.ClickNumbers, sign))
                self.KP_1.addWidget(self.KPButtons_1[rownum][columnnum], rownum, columnnum)
                self.KPButtons_1[rownum][columnnum].setStyleSheet("""
                        color: gray;
                    """)

        self.KP_2 = QGridLayout()
        for rownum, row in enumerate(self.KPPattern_2):
            for columnnum, sign in enumerate(row):
                self.KPButtons_2[rownum][columnnum] = QPushButton(sign)
                # self.KNumbersButtons[rownum][columnnum].clicked.connect(partial(self.ClickNumbers, sign))
                self.KP_2.addWidget(self.KPButtons_2[rownum][columnnum], rownum, columnnum)
                self.KPButtons_2[rownum][columnnum].setStyleSheet("""
                    color: magenta;
                """)



        self.KP_top = QGridLayout()
        for rownum, row in enumerate(self.KPPattern_top):
            for columnnum, sign in enumerate(row):
                self.KPButtons_top[rownum][columnnum] = QPushButton(sign)
                # self.KNumbersButtons[rownum][columnnum].clicked.connect(partial(self.ClickNumbers, sign))
                self.KP_top.addWidget(self.KPButtons_top[rownum][columnnum], rownum, columnnum)
                self.KPButtons_top[rownum][columnnum].setStyleSheet("""
                    background-color: grey;
                """)
    def initDisplay(self):
        self.Display_2 = QLineEdit()
        self.Display_2.setAlignment(Qt.AlignRight)
        # self.Display.setFixedHeight(35)
        self.Display_2.setReadOnly(True)
        self.Display_2.setStyleSheet("""
            background: transparent;
            border: none;
        """)

        
        self.Display_1 = QLineEdit()
        self.Display_1.setAlignment(Qt.AlignRight)
        # self.Display.setFixedHeight(35)
        self.Display_1.setReadOnly(True)
        self.Display_1.setText(self.Equation_1)

    def initKNumbers(self):
        self.KNumbers = QGridLayout() # Klawiatura
        for rownum, row in enumerate(self.KNumbersPattern):
            for columnnum, sign in enumerate(row):
                self.KNumbersButtons[rownum][columnnum] = QPushButton(sign)
                self.KNumbersButtons[rownum][columnnum].clicked.connect(partial(self.ClickNumbers, sign))
                self.KNumbers.addWidget(self.KNumbersButtons[rownum][columnnum], rownum, columnnum)
                self.KNumbersButtons[rownum][columnnum].setStyleSheet("""
                background-color: white;
                color: blue;
                font-family: 'sans-serif';
                """)

    def initKSigns(self):
        self.KSigns = QGridLayout() # Klawiatura
        for rownum, row in enumerate(self.KSignsPattern):
            for columnnum, sign in enumerate(row):
                self.KSignsButtons[rownum][columnnum] = QPushButton(sign)
                self.KSignsButtons[rownum][columnnum].clicked.connect(partial(self.ClickSigns, sign))
                self.KSigns.addWidget(self.KSignsButtons[rownum][columnnum], rownum, columnnum)
                if sign == '^2':
                    self.KSignsButtons[rownum][columnnum].setStyleSheet("""
                        color: gray;
                    """)
                else:
                    self.KSignsButtons[rownum][columnnum].setStyleSheet("""
                        color: red;
                    """)

    def initUI(self):
        vb = QVBoxLayout()
        self.setLayout(vb)

        DisplayBox = QGridLayout()

        DisplayBox.addWidget(self.Display_2)
        DisplayBox.addWidget(self.Display_1)
        
        
        vb.addStretch(1)
        vb.addLayout(DisplayBox)
        temp = QHBoxLayout()
        temp.addStretch(1)
        temp.addLayout(self.CBLayout_1)
        temp.addStretch(1)
        temp.addLayout(self.CBLayout_2)

        vb.addStretch(1)
        vb.addLayout(temp)

        vb.addStretch(1)
        vb.addLayout(self.KP_top)

        hb = QHBoxLayout()
        hb.addStretch(2)
        hb.addLayout(self.KP_0)
        hb.addStretch(2)
        hb.addLayout(self.KP_1)
        hb.addStretch(2)
        hb.addLayout(self.KP_2)
        hb.addStretch(1)
        hb.addLayout(self.KNumbers)
        hb.addStretch(2)
        hb.addLayout(self.KSigns)
        
        vb.addStretch(1)
        vb.addLayout(hb)
        
    def ClickNumbers(self, sign):
        print(sign)
        if sign not in {'+/-', '.'}:
            if self.Equation_1[0] == '0':
                if len(self.Equation_1) > 1:
                    self.Equation_1 = self.Equation_1 + sign
                else:
                    self.Equation_1 = sign
            else:
                self.Equation_1 = self.Equation_1 + sign
        elif sign == '.':
            if '.' not in self.Equation_1:
                self.Equation_1 = self.Equation_1 + sign
        else:
            self.IsNegative = not self.IsNegative
        self.EquationDisplay()

    def ClickSigns(self, sign):
        if sign == '<x]':
            if len(self.Equation_1) > 1:
                self.Equation_1 = self.Equation_1[:-1]
            else:
                if self.Equation_1 != '0':
                    self.Equation_1 = '0'
        elif sign == 'C':
            self.Equation_1 = '0'
            self.Equation_2 = ''
            self.Operation = ''
            self.IsNegative = False
        elif sign == '^2':
            print("todo")
        elif sign == '=':
            self.EquationFinish()
        else: # + - * :
            self.Equation_2 = self.Equation_1
            if self.IsNegative:
                self.Equation_2 = '-' + self.Equation_2
                self.IsNegative = False
            self.Operation = sign
            self.Equation_1 = '0'
            self.MemoryDisplay()
        self.EquationDisplay()
        self.MemoryDisplay()
    def EquationDisplay(self):
        if self.IsNegative:
            self.Display_1.setText('-' + self.Equation_1)
        else:
            self.Display_1.setText(self.Equation_1)
    def MemoryDisplay(self):
        self.Display_2.setText(self.Equation_2 + ' ' + self.Operation)
    def EquationFinish(self):
        if self.IsNegative:
            self.Equation_1 = '-' + self.Equation_1
            self.IsNegative = False
        result = eval(self.Equation_2 + self.Operation + self.Equation_1)
        self.Equation_1 = str(result)
        self.Equation_2 = ''
        self.Operation = ''

def main():
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
