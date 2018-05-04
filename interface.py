import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Simulador de Gerência de Memória'
        self.width = 480
        self.height = 650
        self.top = 10
        self.left = 10
        self.paginas = 5
        self.pagemiss = 0
        self.pagehit = 0
        self.initUI()

    def initUI(self):
        # Inicia a Janela
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Texto Páginas
        self.lbl = QLabel(self)
        self.lbl.setText('Páginas')
        self.lbl.move(20, 15)

        # Cria as Caixas de Texto das paginas
        for i in range(self.paginas):
            self.textbox = QLineEdit(self)
            self.textbox.move(20+(i*40)+(i*2), 45)
            #self.textbox.setAlignment(self, AlignHCenter)
            #self.textbox.maxLenght(1)
            self.textbox.resize(40,80)

        # Texto Quadros
        self.lbl = QLabel(self)
        self.lbl.setText('Quadros')
        self.lbl.move(20, 150)

        # Cria as Caixas de Texto dos quadros
        for i in range(self.paginas+3):
            self.textbox = QLineEdit(self)
            self.textbox.move(20+(i*40)+(i*2), 180)
            #self.textbox.maxLenght(4)
            self.textbox.resize(40,80)

        # Texto Processo
        self.lbl = QLabel(self)
        self.lbl.setText('Criar Processo')
        self.lbl.move(20, 285)

        # Cria Botão de Criação De processo
        self.button = QPushButton('Processo 4K', self)
        self.button.move(20, 315)

        self.button = QPushButton('Processo 8K', self)
        self.button.move(130, 315)

        self.button = QPushButton('Processo 12K', self)
        self.button.move(240, 315)

        self.button = QPushButton('Processo 16K', self)
        self.button.move(350, 315)

        # Texto Pular Ciclos
        self.lbl = QLabel(self)
        self.lbl.setText('Pular Ciclo')
        self.lbl.move(20, 380)

        # Cria Botão de Skip cycles
        self.button = QPushButton('Pular 1 Ciclo', self)
        self.button.move(20, 410)

        self.button = QPushButton('Pular 2 Ciclos', self)
        self.button.move(130, 410)

        self.button = QPushButton('Pular 3 Ciclos', self)
        self.button.move(240, 410)

        # Texto Kill Process
        self.lbl = QLabel(self)
        self.lbl.setText('Matar Processo')
        self.lbl.move(20, 475)

        # Texto PID
        self.lbl = QLabel(self)
        self.lbl.setText('Digite o PID do processo')
        self.lbl.move(25, 500)
        self.lbl.resize(300,20)

        # TextBox do PID
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 525)
        self.textbox.resize(160,30)

        # Cria Botão de Matar Processo
        self.button = QPushButton('Matar', self)
        self.button.move(190, 525)
        self.button.resize

        # Cria Botão de Ajuda
        self.button = QPushButton('Ajuda', self)
        self.button.move(350, 15)
        self.button.resize

        self.show()

    def PID(self, pid):
        # Texto PID
        self.lbl = QLabel(self)
        self.lbl.setText('PID: ' + self.pid)
        self.lbl.move(300, 70)
        self.show()

    def PageHit(self):
        # Texto Page Hit
        self.pagehit = self.pagehit + 1
        self.lbl = QLabel(self)
        self.lbl.setText('Page Hit: ' + str(self.pagehit))
        self.lbl.move(20, 120)
        self.show()

    def PageMiss(self):
        # Texto Page Miss
        self.pagemiss = self.pagemiss + 1
        self.lbl = QLabel(self)
        self.lbl.setText('Page Miss: ' + str(self.pagemiss))
        self.lbl.move(100, 120)
        self.show()