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
        button.clicked.connect(self.close_application)
        button.resize(button.minimumSizeHint())
        button.move(0, 0)
        self.show()




    def close_application(self):
        print("Hey There!")
        sys.exit()




def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())



run()
             
