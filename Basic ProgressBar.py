import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT Tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))


        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Q")
        extractAction.setStatusTip("Leave The App")
        extractAction.triggered.connect(self.close_application)


        self.button = QtGui.QPushButton("Download!", self)
        self.button.move(200, 120)
        self.button.clicked.connect(self.download)


        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)


        
        self.home()


    def home(self):
        button = QtGui.QPushButton("Quit", self)
        button.clicked.connect(self.close_application)
        button.resize(button.minimumSizeHint())
        button.move(0, 100)


        extractAction = QtGui.QAction(QtGui.QIcon("todachoppa.png"), "Flee the Scene", self)
        extractAction.triggered.connect(self.close_application)


        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)



        checkBox = QtGui.QCheckBox("Enlarge Window", self)
        checkBox.move(100, 25)
##        checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)
        checkBox.toggle()
        self.show()




    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
              self.setGeometry(50, 50, 1000, 600)
        else:
              self.setGeometry(50, 50, 500, 300)
        


    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Extract!", "Get Into The Chopper?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaooow!!!!")
            sys.exit()

        else:
            pass

        
        print("Hey There!")
##        sys.exit()


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)




def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())



run()
             
