# -*- coding: utf-8 -*-

from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4 import QtCore
import uuid # For the love of all things sacred, it is called uuid...
import sys  # We need sys so that we can pass argv to QApplication

import docplanwindow

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


# A class definition
# Create a new process and add to collection
# p = Process(self.txtTryMe.text())
# self.processes.append(p)
# for pP in self.processes:
#    pP.SayHi('Mats')
# Show the new process



class DocPlanClass(QtGui.QMainWindow, docplanwindow.Ui_MainWindow):

    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined

        #self.txtDebug.setStyleSheet("color: blue;"
        #                "background-color: white;"
        #                "selection-color: yellow;"
        #                "selection-background-color: blue;"
        #                "border: 2px solid grey;"
        #                "border-radius: 10px;")

        # Initialise the buttons
        self.cmdTryMe.clicked.connect(self.try_me)
              
    # Handler for the table view
    def try_me(self):
        u = u'Tried me'
        self.txtOut.setText(u)

        print "Clicked the try me-button"
        



    
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    
    # Set all QLineEdit's to yellow background
    #app.setStyleSheet("QLineEdit { background-color: yellow }") 

    form = DocPlanClass()  # We set the form to be our design
    form.show()  # Show the form

    app.exec_()  # and execute the app
    #form.populate_main_processes()


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
