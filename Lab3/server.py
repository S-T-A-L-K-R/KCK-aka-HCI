import sys
import socket, pickle

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Widgets.circle import *

HOST = '127.0.0.1'
PORT = 6666

class ServerThread(QThread):
    signal1 = pyqtSignal(int)
    signal2 = pyqtSignal(str)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        QThread.__init__(self)
    def run(self):
            self.server.bind((HOST, PORT))
            self.signal2.emit("Czekam na połączenie")
            self.server.listen()
            conn, addr = self.server.accept()
            self.signal2.emit("Połączono")
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                        # TODO rozpoczęcie pętli od nowa, aktualizacja LABELa
                    print("Data received: " + str(pickle.loads(data)))
                    self.signal1.emit(pickle.loads(data))


class Lab3Server(QMainWindow):
    circleSize = 50
    def __init__(self):
        super().__init__()
        self.connection = ServerThread()
        self.connection.signal1.connect(self.circleChange)
        self.connection.signal2.connect(self.labelChange)
        self.initUI()

    def launchServer(self):
        if self.connectAction.isChecked():
            # Wątek servera/socketa
            self.connection.start()
            print("Thread started")
            # Labele
            self.bar.setText('Serwer jest włączony')
            self.connectAction.setText('Zatrzymaj serwer')
        else:
            # Wątek servera/socketa
            self.connection.quit() # TODO poprawić/sprecyzować QUIT
            print("Server killed")
            # Labele
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
        self.setWindowTitle('Server')

        self.show()

    def circleChange(self, value):
        self.circleSize = value
    def labelChange(self, value):
        self.bar.setText(value)
def main():
    app = QApplication(sys.argv)
    ex = Lab3Server()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()