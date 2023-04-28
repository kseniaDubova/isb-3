from PyQt5.QtWidgets import QPushButton,QApplication,QMainWindow,QLabel,QDesktopWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import QtWidgets

class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        
        self.setWindowTitle('3DES')
        self.setFixedSize(600, 400)
        self.background = QLabel(self)
        self.info = QLabel(self)
        self.background.setGeometry(0, 0, 600, 400)
        self.background.setPixmap(QPixmap("icon.jpg").scaled(600,400))

        self.botton_keys = QPushButton('Сгенерировать ключи', self)
        self.botton_keys.setGeometry(200,100,200,50)
        self.botton_keys.clicked.connect(self.cleak_key)

        self.botton_e = QPushButton('Зашифровать текст', self)
        self.botton_e.setGeometry(200,150,200,50)
        self.botton_e.clicked.connect(self.cleak_e)
        self.botton_e.hide()

        self.botton_d = QPushButton('Дешифровать текст', self)
        self.botton_d.setGeometry(200,200,200,50)
        self.botton_d.clicked.connect(self.cleak_d)
        self.botton_d.hide()
  
        self.show()
    
    def hidden(self):

        self.botton_d.show()
        self.botton_e.show()

    def cleak_key(self):
        self.info.setText("Ключи сгенерированы")
        self.info.setGeometry(225,250,200,50)
        self.info.show()
        self.hidden()

    def cleak_e(self):
        self.info.setText("Текст зашифрован")
        self.info.setGeometry(225,250,200,50)
        self.info.show()
    
    def cleak_d(self):
        self.info.setText("Текст расшифрован")
        self.info.setGeometry(225,250,200,50)
        self.info.show()

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()