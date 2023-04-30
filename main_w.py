from PyQt5.QtWidgets import QPushButton,QApplication,QMainWindow,QLabel,QDesktopWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import QtWidgets
import re
from coding import Coding as cd
import os
class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        
        self.setWindowTitle('3DES')
        self.setFixedSize(600, 400)
        self.background = QLabel(self)
        self.info = QLabel(self)
        self.info.setText("Выберите размер ключа")
        self.info.setGeometry(225,20,200,50)
        self.background.setGeometry(0, 0, 600, 400)
        self.background.setPixmap(QPixmap("icon.jpg").scaled(600,400))

        self.botton_keys = QPushButton('Сгенерировать ключи', self)
        self.botton_keys.setGeometry(200,100,200,50)
        self.botton_keys.clicked.connect(self.cleak_key)
        self.botton_keys.hide()

        self.key_size = QtWidgets.QComboBox(self)
        self.key_size.addItems(["64", "128", "192"])
        self.key_size.setGeometry(200,50,200,50)
        self.key_size.activated[str].connect(self.on_activated)
        #self.key_size.show()

        self.botton_e = QPushButton('Зашифровать текст', self)
        self.botton_e.setGeometry(200,150,200,50)
        self.botton_e.clicked.connect(self.cleak_e)
        self.botton_e.hide()

        self.botton_d = QPushButton('Дешифровать текст', self)
        self.botton_d.setGeometry(200,200,200,50)
        self.botton_d.clicked.connect(self.cleak_d)
        self.botton_d.hide()
  
        self.show()
    

    def on_activated(self, text):
        self.size = re.findall('(\d+)', text)[0]
        self.info.setText("Сгенирируйте ключи")
        self.botton_keys.show()


    def hidden(self):

        self.botton_d.show()
        self.botton_e.show()

    def cleak_key(self):
        key = cd(self.size)
        key.generation_key()
        self.info.setText("Ключи сгенерированы")
        print(self.size)
        self.hidden()

    def cleak_e(self):
        self.info.setText("Текст зашифрован")
    
    def cleak_d(self):
        self.info.setText("Текст расшифрован")

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()