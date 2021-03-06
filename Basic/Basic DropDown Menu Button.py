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



        self.styleChoice = QtGui.QLabel("Windows Vista", self)
        self.styleChoice.move(50, 150)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.move(50, 250)


        comboBox.activated[str].connect(self.style_choice)

        
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
        checkBox.toggle()
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
        sys.exit()


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))




def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())



run()





##import sys
##from PyQt4 import QtGui, QtCore
##
##class Window(QtGui.QMainWindow):
##
##    def __init__(self):
##        super(Window, self).__init__()
##        self.setGeometry(50, 50, 500, 300)
##        self.setWindowTitle("PyQT tuts!")
##        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
##
##        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
##        extractAction.setShortcut("Ctrl+Q")
##        extractAction.setStatusTip('Leave The App')
##        extractAction.triggered.connect(self.close_application)
##
##        self.statusBar()
##
##        mainMenu = self.menuBar()
##        fileMenu = mainMenu.addMenu('&File')
##        fileMenu.addAction(extractAction)
##        
##        self.home()
##
##    def home(self):
##        btn = QtGui.QPushButton("Quit", self)
##        btn.clicked.connect(self.close_application)
##        btn.resize(btn.minimumSizeHint())
##        btn.move(0,100)
##
##        extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
##        extractAction.triggered.connect(self.close_application)
##        
##        self.toolBar = self.addToolBar("Extraction")
##        self.toolBar.addAction(extractAction)
##
##        checkBox = QtGui.QCheckBox('Shrink Window', self)
##        checkBox.move(100, 25)
##        checkBox.stateChanged.connect(self.enlarge_window)
##
##        self.progress = QtGui.QProgressBar(self)
##        self.progress.setGeometry(200, 80, 250, 20)
##
##        self.btn = QtGui.QPushButton("Download",self)
##        self.btn.move(200,120)
##        self.btn.clicked.connect(self.download)
##
##        print(self.style().objectName())
##        self.styleChoice = QtGui.QLabel("Windows Vista", self)
##
##        comboBox = QtGui.QComboBox(self)
##        comboBox.addItem("motif")
##        comboBox.addItem("Windows")
##        comboBox.addItem("cde")
##        comboBox.addItem("Plastique")
##        comboBox.addItem("Cleanlooks")
##        comboBox.addItem("windowsvista")
##        comboBox.move(50, 250)
##        
##        self.styleChoice.move(50,150)
##        comboBox.activated[str].connect(self.style_choice)
##
##        self.show()
##
##
##    def style_choice(self, text):
##        self.styleChoice.setText(text)
##        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
##
##
##    def download(self):
##        self.completed = 0
##
##        while self.completed < 100:
##            self.completed += 0.0001
##            self.progress.setValue(self.completed)
##        
##        
##
##    def enlarge_window(self, state):
##        if state == QtCore.Qt.Checked:
##            self.setGeometry(50,50, 1000, 600)
##        else:
##            self.setGeometry(50, 50, 500, 300)
##        
##
##    def close_application(self):
##        choice = QtGui.QMessageBox.question(self, 'Extract!',
##                                            "Get into the chopper?",
##                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
##        if choice == QtGui.QMessageBox.Yes:
##            print("Extracting Naaaaaaoooww!!!!")
##            sys.exit()
##        else:
##            pass
##        
##
##    
##def run():
##    app = QtGui.QApplication(sys.argv)
##    GUI = Window()
##    sys.exit(app.exec_())
##
##
##run()
