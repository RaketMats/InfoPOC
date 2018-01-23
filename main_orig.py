# -*- coding: utf-8 -*-

from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

import uuid # For the love of all things sacred, it is called uuid...
import sys  # We need sys so that we can pass argv to QApplication

import design  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods

import pickle

import metainfo
import docplan 

# A class definition
# Create a new process and add to collection
# p = Process(self.txtTryMe.text())
# self.processes.append(p)
# for pP in self.processes:
#    pP.SayHi('Mats')
# Show the new process



class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):

    id = '0'
    m_table = None
    meta = None
    foundProcess = None

    def PopulateDefaultMetainformation(self):
        self.meta = metainfo.Process('root')    
        self.meta.AddSubProcess('Information(0)', 'h')
        self.meta.AddSubProcess('Program(1)', 'h')
        self.meta.AddSubProcess('Litteraturformedling(2)', 'h')
        self.meta.AddSubProcess('Uppsokande verksamhet(3)', 'h')
        self.meta.AddSubProcess('Barn & Ungdom(4)', 'h')

        l1 = self.meta.GetSubProcesses()
        # Huvudprocess0
        l1[0].AddSubProcess('Bibliotekets webb(00)', 's')
        l1[0].AddSubProcess('Information vid disk(01)', 's')
        l2 = l1[0].GetSubProcesses()
        l2[0].AddSubProcess('Underprocesså(000)', 's')
        l2[0].AddSubProcess('Underprocess(001)', 's')
        l2[1].AddSubProcess('Underprocess(010)', 's')
        l2[1].AddSubProcess('Underprocess(011)', 's')
        
        # Huvudprocess1
        l1[1].AddSubProcess('Underprocess(10)', 's')
        l1[1].AddSubProcess('Underprocess(11)', 's')
        l2 = l1[1].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess(100)', 's')
        l2[0].AddSubProcess('Underprocess(101)', 's')
        l2[1].AddSubProcess('Underprocess(110)', 's')
        l2[1].AddSubProcess('Underprocess(111)', 's')
        # Huvudprocess2 Litteraturförmedling
        l1[2].AddSubProcess('Katalogisering', 's')
        l1[2].AddSubProcess('Utlån', 's')
        l1[2].AddSubProcess('Gallring', 's')
        l2 = l1[2].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess(200)', 's')
        l2[0].AddSubProcess('Underprocess(201)', 's')
        l2[1].AddSubProcess('Underprocess(210)', 's')
        l2[1].AddSubProcess('Underprocess(211)', 's')
        # Huvudprocess3
        l1[3].AddSubProcess('Underprocess(30)', 's')
        l1[3].AddSubProcess('Underprocess(31)', 's')
        l2 = l1[3].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess(300)', 's')
        l2[0].AddSubProcess('Underprocess(301)', 's')
        l2[1].AddSubProcess('Underprocess(310)', 's')
        l2[1].AddSubProcess('Underprocess(311)', 's')
        # Huvudprocess4
        l1[4].AddSubProcess('Underprocess(40)', 's')
        l1[4].AddSubProcess('Underprocess(41)', 's')
        l2 = l1[4].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess(400)', 's')
        l2[0].AddSubProcess('Underprocess(401)', 's')
        l2[1].AddSubProcess('Underprocess(410)', 's')
        l2[1].AddSubProcess('Underprocess(411)', 's')

    # FindProcess: Finds process in metainfo given the process id. Return result in global variable
    # Usage: self.FindProcess(self.meta.GetSubProcesses(), index.data(1).toString())
    #        Stores result in global variable self.foundProcess, should be made more nice but do not have time...
    def FindProcess(self, pn, id):

        for p in pn:
            if (p.GetId() == id):
                self.foundProcess = p                
            x = p.GetSubProcesses()
            if len(x) == 0:
                return
            else:
                self.FindProcess(x, id)


    # DeleteProcess: Deletes a process.
    # Usage: tbd
    def DeleteProcess(self, pn, id):

        print 'DeleteProcess called. Process id:', id
        print 'pn is', pn, ' with id', pn.GetId()

        x = pn.GetSubProcesses()
        for y in x:
            print 'y is', y, ' with id', y.GetId()

        '''
        for p in pn:
            x = p.GetSubProcesses()
            for y in x:
                if (y.GetId() == id):
                #self.foundProcess = p                
                    print 'Debug: Deleting process ', id, ' with name', x.GetInfo()
            if len(x) == 0:
                return
            else:
                self.FindProcess(x, id)
        '''

    # AddProcess: Adds a process to metainfo. The new process name is given. The location will be after the process with the given process id.
    # Usage: self.AddProcess(self.meta.GetSubProcesses(), index.data(1).toString())
    def AddProcess(self, pn, id, newProcessName):

        for p in pn:
            if (p.GetId() == id):
                #self.foundProcess = p                
                print 'Debug: Adding new process ', newProcessName, ' after process named ', p.Info()
            x = p.GetSubProcesses()
            if len(x) == 0:
                return
            else:
                self.FindProcess(x, id)

    # RenameProcess: Rename a process. The new name for the process is given and the process to renam given via the process id.
    # Usage: self.RenameProcess(self.meta.GetSubProcesses(), index.data(1).toString())
    def RenameProcess(self, pn, id, newProcessName):

        for p in pn:
            if (p.GetId() == id):
                #self.foundProcess = p                
                print 'Debug: Renaming process ', p.Info(), ' to', newProcessName
                p.SetName(newProcessName)
            x = p.GetSubProcesses()
            if len(x) == 0:
                return
            else:
                self.FindProcess(x, id)


    def PopulateTreeview(self, pn, node):
        
        # parent = QtGui.QTreeWidgetItem(self.treeProcesses)
        # parent.setText(0, p.Info())
        # parent.setData(0, 1, p.GetId())

        for p in pn:
            x = p.GetSubProcesses()
            if len(x) == 0:
                parent = QtGui.QTreeWidgetItem(node)
                parent.setText(0, p.Info())
                parent.setData(0, 1, p.GetId())
                return
            else:
                parent = QtGui.QTreeWidgetItem(node)
                parent.setText(0, p.Info())
                parent.setData(0, 1, p.GetId())
                self.PopulateTreeview(x, parent)


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
        self.cmdSaveState.clicked.connect(self.save_state)
        self.cmdLoadState.clicked.connect(self.load_state)
        self.cmdTestUnicode.clicked.connect(self.test_unicode)
        self.cmdDocPlan.clicked.connect(self.open_docplan)

        # Initialise the tree widget
        '''
        self.treeProcesses.setStyleSheet("color: blue;"
                        "background-color: white;"
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "border: 2px solid grey;"
                        "border-radius: 5px;")
        '''
        self.treeProcesses.setStyleSheet("border: 2px solid grey;"
                        "border-radius: 5px;")
        
        self.treeProcesses.itemChanged.connect (self.handletreeProcessChanged)
        #self.treeProcesses.clicked.connect(self.handletreeProcessClicked)
        self.treeProcesses.clicked.connect(self.on_treeView_clicked)
        self.treeProcesses.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeProcesses.customContextMenuRequested.connect(self.opentreeProcessesContextMenu)

        # Build the mockup metainformation
        self.PopulateDefaultMetainformation()
        
        # Populate the treeview
        self.PopulateTreeview(self.meta.GetSubProcesses(), self.treeProcesses)
            
        # Populate the treeview
        
        '''        
        for i in xrange(5):
            parent = QtGui.QTreeWidgetItem(self.treeProcesses)
            #parent.setText(0, "Parent {}".format(str(uuid.uuid4())))
            parent.setText(0, "Huvudprocess {}".format(i))

            # From http://stackoverflow.com/questions/1076208/what-is-a-role-in-a-qtreewidgetitem
            #QList<QVariant> dataList;
            #dataList.append("data 1");
            #dataList.append("data 2");
            #QVariant data(dataList);
            #item->setData(0, Qt::UserRole, data);
            id = str(uuid.uuid4())
            #parent.setData(0, 1, str(uuid.uuid4())) # First parameter is Column, second is Role, if 0 it replaces the text, last is any type of data
            parent.setData(0, 1, id) # First parameter is Column, second is Role, if 0 it replaces the text, last is any type of data

            #parent.setFlags(parent.flags() | QtGui.Qt.ItemIsTristate | QtGui.Qt.ItemIsUserCheckable)

            for x in xrange(5):
                child = QtGui.QTreeWidgetItem(parent)
                #child.setFlags(child.flags() | QtGui.Qt.ItemIsUserCheckable)
                child.setText(0, "Underprocess {}.{}".format(i, x))
                #child.setData(0, 1, str(uuid.uuid4())) # First parameter is Column, second is Role, if 0 it replaces the text, last is any type of data
                #child.setCheckState(0, QtCore.Qt.Unchecked) # Add checkbox, or not
                id = str(uuid.uuid4())
                child.setData(0, 1, id) # First parameter is Column, second is Role, if 0 it replaces the text, last is any type of data

                for y in xrange(5):
                    child2 = QtGui.QTreeWidgetItem(child)
                    #child.setFlags(child.flags() | QtGui.Qt.ItemIsUserCheckable)
                    child2.setText(0, "Underprocess {}.{}.{}".format(i, x, y))
                    #child2.setData(0, 1, str(uuid.uuid4())) # First parameter is Column, second is Role, if 0 it replaces the text, last is any type of data
                    # child2.setCheckState(0, QtCore.Qt.Unchecked) # Add checkbox, or not
                    id = str(uuid.uuid4())
                    child2.setData(0, 1, id) # First parameter is Column, second is Role, if 0 it replaces the text, last is any type of data

                    for z in xrange(5):
                        child3 = QtGui.QTreeWidgetItem(child2)
                        #child.setFlags(child.flags() | QtGui.Qt.ItemIsUserCheckable)
                        child3.setText(0, "Underprocess {}.{}.{}.{}".format(i, x, y, z))
                        #child3.setData(0, 1, str(uuid.uuid4())) # First parameter is Column, second is Role, if 0 it replaces the text, last is any type of data
                        # child3.setCheckState(0, QtCore.Qt.Unchecked) # Add checkbox or not
                        id = str(uuid.uuid4())
                        child3.setData(0, 1, id) # First parameter is Column, second is Role, if 0 it replaces the text, last is any type of data
        '''

        # Initialise the QWidget Table, from here https://pythonspot.com/en/qt4-table/
        '''
        self.tableWidget.setStyleSheet("color: blue;"
                        "background-color: white;"
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "border: 2px solid grey;"
                        "border-radius: 5px;")
        '''
        self.tableWidget.setStyleSheet("border: 2px solid grey;"
                        "border-radius: 5px;")
        
        table = QtGui.QTableWidget(self.tableWidget)
        
        # Getting a table value
        # table = QtGui.QTableWidget(self.tableWidget)
        # t = table.itemAt(10,10)
        
        #table.setWindowTitle('Hello world') # Does not work
        '''
        table.setRowCount(15)
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(QtCore.QString("Name;Value;").split(";"))
        #table.setVerticalHeaderLabels(QtCore.QString("V1;V2;V3;V4").split(";"))
        '''

        # Sizing columns: https://stackoverflow.com/questions/38098763/pyside-pyqt-how-to-make-set-qtablewidget-column-width-as-proportion-of-the-a
        # And: https://stackoverflow.com/questions/35663512/pyqt4-qtablewidget-set-row-width-and-column-height-to-fill-parent-widget
        table.resize(750, 500)
        table.setRowCount(10)
        table.setColumnCount(3)
        tableHeader = table.horizontalHeader()
        #tableHeader.setResizeMode(QtGui.QHeaderView.Fixed)
        table.setColumnWidth(0, 250)
        table.setColumnWidth(1, 250)
        table.setColumnWidth(2, 200)
        table.setHorizontalHeaderLabels(QtCore.QString("Name;Value;Comment;").split(";"))

        table.setItem(0,0, QtGui.QTableWidgetItem('Name'))
        table.setItem(0,1, QtGui.QTableWidgetItem('Value'))
        table.setItem(0,2, QtGui.QTableWidgetItem('Comment'))
        table.setItem(1,0, QtGui.QTableWidgetItem('Item 1.3'))
        table.setItem(1,1, QtGui.QTableWidgetItem('Item 1.4'))
        table.setItem(1,2, QtGui.QTableWidgetItem('Comment 1.4'))
        table.setItem(2,0, QtGui.QTableWidgetItem('Item 2.1'))
        table.setItem(2,1, QtGui.QTableWidgetItem('Item 2.2'))
        table.setItem(2,2, QtGui.QTableWidgetItem('Comment '))
        table.setItem(3,0, QtGui.QTableWidgetItem('Item 2.3'))
        table.setItem(3,1, QtGui.QTableWidgetItem('Item 2.4'))
        table.setItem(3,2, QtGui.QTableWidgetItem('Comment'))
        
        print "Initialized table"
        print table.item(2,1).text()
        self.m_table = table # By some strange reason it is impossible to access the table object from the click-event, therefore, share via global variable
        print self.m_table.item(2,1).text()

        # Initialise the table click function
        table.cellClicked.connect(self.tableCellClick)

        # Set tooltip
        table.horizontalHeaderItem(0).setToolTip("Name")
        table.horizontalHeaderItem(1).setToolTip("Value")
        table.horizontalHeaderItem(2).setToolTip("Comment")

        # Initialise the table view 'Ok'-button
        self.cmdOkTableView.clicked.connect(self.cmdOkTableViewClick)
        
        # Show image on the image label
        pixmap = QtGui.QPixmap('information.jpg')
        self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.size()))

        
    # Populate the process tree view
    def addTreeProcessesItems(self, parent):
        column = 0
        clients_item = self.addTreeProcessParent(parent, column, 'Clients', 'data Clients')
        vendors_item = self.addTreeProcessParent(parent, column, 'Vendors', 'data Vendors')
        time_period_item = self.addTreeProcessParent(parent, column, 'Time Period', 'data Time Period')

        self.addTreeProcessChild(clients_item, column, 'Type A', 'data Type A')
        self.addTreeProcessChild(clients_item, column, 'Type B', 'data Type B')

        self.addTreeProcessChild(vendors_item, column, 'Mary', 'data Mary')
        self.addTreeProcessChild(vendors_item, column, 'Arnold', 'data Arnold')

        self.addTreeProcessChild(time_period_item, column, 'Init', 'data Init')
        self.addTreeProcessChild(time_period_item, column, 'End', 'data End')

    # When the tree view is changed, i.e. checkbox changed
    def handletreeProcessChanged(self, item, column):
        print "Handle treeProcess changed"

    # Tree view clicked, replaced by other function below
    def handletreeProcessClicked(self, item):
        i = 42
        print "Handle treeProcess clicked: ", item
        #print "Handle treeProcess clicked: ", item.text()
    

    # Save the current metainformation to disk
    # Getting a filename: https://www.tutorialspoint.com/pyqt/pyqt_qfiledialog_widget.htm
    def save_state(self):
        #fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        dlg.setFilter("Save files (*.sav)")
        filenames = QtCore.QStringList()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        #fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '',"Pickle files (*.pickle)")
        print 'Saving to file', filenames[0]
        pickle_file = file(filenames[0], 'w')
        pickle.dump(self.meta, pickle_file)

    # Load the last metainformation from disk
    def load_state(self):
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        dlg.setFilter("Save files (*.sav)")
        filenames = QtCore.QStringList()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        #fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        print 'Loading from file', filenames[0]
        pickle_file = file(filenames[0])
        self.meta = pickle.load(pickle_file)
        self.treeProcesses.clear()
        self.PopulateTreeview(self.meta.GetSubProcesses(), self.treeProcesses)
        
        #debugText = 'Processes'
        #for p in self.processes:
        #    debugText += p.get_name()
        #self.txtDebug.setText(debugText)
                
            
    # Handler for the table view
    def tableCellClick(self, row, col):
        #print "Click on table: " + str(row) + " " + str(col) + " data: " + self.m_table.item(row,col).text()
        print "Click on table: " + str(row) + " " + str(col) + " data: " + unicode(QtCore.QString(self.m_table.item(1,1).text()))
               

    # Test Unicode
    def test_unicode(self):
        #uni = QtCore.QString()
        uni = QtCore.QString(self.m_table.item(0,0).text())
        uni2 = QtCore.QString(u'abcåäö')
        #table.setHorizontalHeaderLabels(QtCore.QString("Name;Value;").split(";"))
        #print unicode(u'Testing Unicode...åäö')
        print u'Testing Unicode...åäö. From datagrid: ', unicode(uni), ' and hard code: ', unicode(uni2)

        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.ControlModifier:
            print('ctrl+click')

    # Handler for the 'Ok'-button saving the table view information
    def cmdOkTableViewClick(self):
        print 'Ok button clicked - Saving changes'
        table = QtGui.QTableWidget(self.tableWidget)
        #print unicode(QtCore.QString(self.m_table.item(1,1).text()))

        # Get the table data and save into the data structure
        if (self.foundProcess != None):
            print 'Found process! Name:', self.foundProcess.Info(), 'Id:', self.foundProcess.GetId()
            items = self.foundProcess.GetItems()
            #self.m_table.clear() # Clear the data grid
            # Get the values from the table
            n = 0
            for i in items:
                #print 'Information: ', i.GetName(), '=', i.GetValue(), 'Comment:', i.GetComment()
                #self.m_table.setItem(n,0, QtGui.QTableWidgetItem(i.GetName()))
                #self.m_table.setItem(n,1, QtGui.QTableWidgetItem(i.GetValue()))
                u = QtCore.QString(self.m_table.item(n,0).text())
                i.SetName(u)
                u = QtCore.QString(self.m_table.item(n,1).text())
                i.SetValue(u)
                u = QtCore.QString(self.m_table.item(n,2).text())
                i.SetComment(u)
                print 'Name', unicode(i.GetName())
                print 'Value', unicode(i.GetValue())
                print 'Comment', unicode(i.GetComment())
                n = n + 1
        


    #@QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        
        #if QtGui.qApp.mouseButtons() & QtCore.Qt.RightButton:
        if QtGui.qApp.mouseButtons() == QtCore.Qt.RightButton:
            print "Right click!"

        # A dialog
        # A messagebox with 'Ok'-button connected to function in this class, here. https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm
        if QtGui.qApp.keyboardModifiers() & QtCore.Qt.ControlModifier:
            print "Ctrl key pressed!"
            '''
            d = QtGui.QDialog()
            b1 = QtGui.QPushButton("Ok",d)
            b1.move(50, 50)
            d.setWindowTitle('Dialog')
            d.exec_()
            '''
            '''
            d = QtGui.QInputDialog()
            d.setWindowTitle(u'Lägg till process')
            d.exec_()
            u = QtCore.QString(d.getText())
            print 'New process name: ', unicode(u)
            '''
            text, ok = QtGui.QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
            if ok:
                print 'New process name: ', unicode(text)

        # Print data with role = 0, i.e. the text, and role 1 i.e. own defined role containing uuid
        print 'selected item index found at %s with data: %s and uuid: %s' % (index.row(), index.data().toString(), index.data(1).toString())
        debugText = '<strong>Process tree clicked.</strong>'
        debugText += '<p style="background:#ccc; color:#000; border: solid black 1px;">Additional info here</p><table><tr><td>Alfa</td><td>Beta</td></tr></table>'
        #self.txtDebug.setText(debugText)
        #self.txtDebug.setToolTip('This is a tooltip for the list-textbox')

        # Find the clicked process in the metainformation data model
        #metainfo.FindProcess(index.data(1).toString())
        self.foundProcess = None # Initialise the result
        self.FindProcess(self.meta.GetSubProcesses(), index.data(1).toString())
        if (self.foundProcess != None):
            print 'Found process! Name:', self.foundProcess.Info(), 'Id:', self.foundProcess.GetId()
            items = self.foundProcess.GetItems()
            self.m_table.clear() # Clear the data grid
            n = 0
            # Populate process item information into the 'Beskrivning' and show model picture
            for i in items:
                print 'Beskrivning: Information: ', unicode(i.GetName()), '=', unicode(i.GetValue()), 'Comment:', unicode(i.GetComment())
                self.m_table.setItem(n,0, QtGui.QTableWidgetItem(unicode(i.GetName())))
                self.m_table.setItem(n,1, QtGui.QTableWidgetItem(unicode(i.GetValue())))
                self.m_table.setItem(n,2, QtGui.QTableWidgetItem(unicode(i.GetComment())))
                
                # Check for model image and render if found
                #if (QtGui.QTableWidgetItem(unicode(i.GetName())) == 'Modell'):
                if (unicode(i.GetName()) == u'Modell'):
                    print 'Rendering model image:', unicode(i.GetValue())
                    # Show image on the image label
                    pixmap = QtGui.QPixmap(unicode(i.GetValue()))
                    self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.size()))
                n = n + 1

            

        #self.id = index.data(1).toString()

    # Open context menu for the process treeview
    def opentreeProcessesContextMenu(self, position):

        indexes = self.treeProcesses.selectedIndexes()
        if len(indexes) > 0:
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1
  
        menu = QtGui.QMenu()
        if level == 0:
            Action = menu.addAction(self.tr("Edit level 0 process"))
            Action.triggered.connect(self.treeProcessLevel0Edit)
            Action = menu.addAction(self.tr("Add new process"))
            Action.triggered.connect(self.treeProcessAddProcess)
            Action = menu.addAction(self.tr("Delete process"))
            Action.triggered.connect(self.treeProcessDeleteProcess)
            Action = menu.addAction(self.tr("Rename process"))
            Action.triggered.connect(self.treeProcessRenameProcess)
            
        elif level == 1:
            Action = menu.addAction(self.tr("Edit level 1 process"))
            Action.triggered.connect(self.treeProcessLevel1Edit)
        else:
            Action = menu.addAction(self.tr("Edit all other levels for process"))
            Action.triggered.connect(self.treeProcessLevelXEdit)
  
        menu.exec_(self.treeProcesses.viewport().mapToGlobal(position))

    # Context menu action for adding a new process
    # This function is called as result of click on context menu, created in opentreeProcessContextMenu() above
    # The process selected in the tree is communicated via global variable self.foundProcess, which in turn is populated from the
    # function on_treeView_clicked(), which is also called when the right click happens.
    def treeProcessAddProcess(self):
        newProcessName, ok = QtGui.QInputDialog.getText(self, u'Lägg till ny process', u'Processnamn:')
        if ok:
            print 'New process name: ', unicode(newProcessName)
            # Add the process
            self.AddProcess(self.meta.GetSubProcesses(), self.foundProcess.GetId(), newProcessName)

        else:
            print 'No new process added'

    # Context menu action for deleting a process
    def treeProcessDeleteProcess(self):
        text, ok = QtGui.QInputDialog.getText(self, u'Tag bort process', u'Ok att process raderas?')
        if ok:
            self.DeleteProcess(self.meta, self.foundProcess.GetId())
            #self.treeProcesses.clear()
            #self.PopulateTreeview(self.meta.GetSubProcesses(), self.treeProcesses)
            print 'Process deleted: '
        else:
            print 'Process not deleted'


    # Context menu for renaming a process in the tree view
    def treeProcessRenameProcess(self):
        newProcessName, ok = QtGui.QInputDialog.getText(self, u'Byt namn på process', u'Processnamn:', QtGui.QLineEdit.Normal, self.foundProcess.Info())
        if ok:
            print 'New process name: ', unicode(newProcessName)
            # Add the process
            self.RenameProcess(self.meta.GetSubProcesses(), self.foundProcess.GetId(), newProcessName)
            self.treeProcesses.clear()
            self.PopulateTreeview(self.meta.GetSubProcesses(), self.treeProcesses)

        else:
            print 'No change of name done'

    # Context menu for level 0 process right click
    def treeProcessLevel0Edit(self):
        print 'Edit process level 0'


    # Context menu for level 0 process right click
    def treeProcessLevel1Edit(self):
        print 'Edit process level 1'


    # Context menu for level 0 process right click
    def treeProcessLevelXEdit(self):
        print 'Edit all other process levels'


    def open_docplan(self):
        print 'Opening document plan'
        self.d = docplan.DocPlanClass()  # We set the form to be our design. Must be class variable, otherwise d is immediatly destroyed
        self.d.show()  # Show the form

    
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    
    # Set all QLineEdit's to yellow background
    #app.setStyleSheet("QLineEdit { background-color: yellow }") 

    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form

    app.exec_()  # and execute the app
    #form.populate_main_processes()


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
