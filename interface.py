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
        self.paginas = 7
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

        self.show()
    