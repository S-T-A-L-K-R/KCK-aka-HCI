import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


#sposob 1
#import Dialogi.IkonaDialog

#sposob 2
from Dialogi.IkonaDialog import *
from Dialogi.KolaDialog import *
from Dialogi.KolorDialog import *

class Lab2(QMainWindow):
 def __init__(self):
  super(Lab2, self).__init__()
  self.initUI()

 def initUI(self):               
  menubar = self.menuBar()
  editMenu = menubar.addMenu('&Edycja')
  viewMenu = menubar.addMenu('&Widok')
  helpMenu = menubar.addMenu('Pomo&c')
  
  self.setGeometry(300, 300, 640, 500)
  self.setWindowTitle('Main window')    
  self.show()
  #sposob 1
  #d = Dialogi.IkonaDialog.Ikona()
  #sposob2
  d = Ikona()
  d.exec_()


def main():
  app = QApplication(sys.argv)
  ex = Lab2()
  sys.exit(app.exec_())

if __name__ == '__main__':
 main()
