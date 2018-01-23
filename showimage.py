import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 500, 300)
        #self.setGeometry(100, 100, 150, 130)
        self.setWindowTitle("PyQT Show Image")

        openFile = QtGui.QAction("&File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open File")
        openFile.triggered.connect(self.file_open)

        self.statusBar()

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)

        self.lbl = QtGui.QLabel(self)
        self.setCentralWidget(self.lbl)

        self.home()

    def home(self):
        self.show()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')

        pixmap = QtGui.QPixmap(name)
        self.lbl.setPixmap(pixmap.scaled(self.lbl.size()))


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
