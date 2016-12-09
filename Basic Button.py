import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT Tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.home()


    def home(self):
        button = QtGui.QPushButton("Quit", self)
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        button.resize(100,100)
        button.move(100, 100)
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())



run()
             
