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
    meta = None # This holds the root-process, which in turn then holds the first level processes ('Strukturenheter') and all their sub-processes
    foundProcess = None
    _foundProcess = None
    processInFocus = None

    def PopulateDefaultMetainformation(self):
        print 'PopulateDefaultMetainformation called'
        #self.meta = metainfo.Process('root') # Add the root process manually
        self.XAddProcessToParentByName(None, 'root') # Add the root process
        self.XAddProcessToParentByName('root', '1')        
        self.XAddProcessToParentByName('root', '2')        
        self.XAddProcessToParentByName('1', '11')        
        self.XAddProcessToParentByName('1', '12')        
        self.XAddProcessToParentByName('2', '21')        
        self.XAddProcessToParentByName('2', '22')        
        self.XAddProcessToParentByName('11', '111')        
        self.XAddProcessToParentByName('11', '112')        
        self.XAddProcessToParentByName('22', '221')        
        self.XAddProcessToParentByName('22', '222')        
        '''
        found = self.XFindProcessByName(self.meta, 'root')
        found.AddSubProcess('1', 'h')
        found.AddSubProcess('2', 'h')
        found = self.XFindProcessByName(self.meta, '1')
        found.AddSubProcess('11', 'h')
        found.AddSubProcess('12', 'h')
        found = self.XFindProcessByName(self.meta, '2')
        found.AddSubProcess('21', 'h')
        found.AddSubProcess('22', 'h')
        found = self.XFindProcessByName(self.meta, '11')
        found.AddSubProcess('111', 'h')
        found.AddSubProcess('112', 'h')
        found = self.XFindProcessByName(self.meta, '22')
        found.AddSubProcess('221', 'h')
        found.AddSubProcess('222', 'h')
        '''
        '''
        root.AddSubProcess('1', 'h')
        root.AddSubProcess('2', 'h')
        a = root.GetSubProcesses()
        a[0].AddSubProcess('11', 's')
        a[0].AddSubProcess('12', 's')
        a[1].AddSubProcess('21', 's')
        a[1].AddSubProcess('22', 's')
        b = a[0].GetSubProcesses()
        b[0].AddSubProcess('111', 's')
        b[0].AddSubProcess('112', 's')
        c = a[1].GetSubProcesses()
        c[0].AddSubProcess('211', 's')
        c[0].AddSubProcess('212', 's')
        self.meta = root
        '''

    def PopulateDefaultMetainformationOld2(self):
        self.meta.append(metainfo.Process('root'))
        self.meta[0].AddSubProcess('1', 'h')
        self.meta[0].AddSubProcess('2', 'h')
        self.meta[0].AddSubProcess('3', 'h')
        l1 = self.meta[0].GetSubProcesses()
        l1[0].AddSubProcess('11', 's')
        l1[0].AddSubProcess('12', 's')
        l1[0].AddSubProcess('13', 's')
        l1[1].AddSubProcess('21', 's')
        l1[1].AddSubProcess('22', 's')
        l1[1].AddSubProcess('23', 's')
        l1[2].AddSubProcess('31', 's')
        l1[2].AddSubProcess('32', 's')
        l1[2].AddSubProcess('33', 's')
        #l1 = self.meta[0].GetSubProcesses()
        #l1[0].AddSubProcess('20', 's')
        #l1[0].AddSubProcess('21', 's')
        

    def PopulateDefaultMetainformationOld(self):
        self.meta.append(metainfo.Process('root'))
        self.meta[0].AddSubProcess('Information(0)', 'h')
        self.meta[0].AddSubProcess('Program(1)', 'h')
        self.meta[0].AddSubProcess('Litteraturformedling(2)', 'h')
        self.meta[0].AddSubProcess('Uppsokande verksamhet(3)', 'h')
        self.meta[0].AddSubProcess('Barn & Ungdom(4)', 'h')

        l1 = self.meta[0].GetSubProcesses()
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
        l1[2].AddSubProcess('Katalogisering(20)', 's')
        l1[2].AddSubProcess('Utlån(21)', 's')
        l1[2].AddSubProcess('Gallring(22)', 's')
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
            print 'FindProcess. Id:', p.GetId()
            if (p.GetId() == id):
                self.foundProcess = p                
            x = p.GetSubProcesses()
            if len(x) == 0:
                return
            else:
                self.FindProcess(x, id)


    # DeleteProcess: Deletes a process.
    # Usage: self.DeleteProcess(self.meta, index.data(1).toString())
    # Note, when deleting it is the clicked process parent that must be the start. Thus, start with meta[0] i.e. 'root' and go through it's subprocesses to find the clicked one    
    def DeleteProcess(self, pn, id):

        for p in pn:
            x = p.GetSubProcesses() # Get the subprocesses, i.e. processes one level down
            n = 0 # Count index, since this is used when pop'ing the process from SubProcesses list
            for y in x: # Go through all sub processes and check for id, i.e. iterate through the children
                if (y.GetId() == id):
                    print 'Debug: Deleting process ', id
                    p.DeleteSubProcess(n)
            if len(x) == 0:
                return
            else:
                self.DeleteProcess(x, id)


    # AddProcess: Adds a process to metainfo. The new process name is given. The location will be after the process with the given process id.
    # Usage: self.AddProcess(self.meta, self.foundProcess.GetId(), name) # Note, when adding it is the clicked process parent that must be the start. Thus, start with meta[0] i.e. 'root' and go through it's subprocesses to find the clicked one
    def AddProcess(self, pn, id, newProcessName):
        print 'AddProcess called' # !!!
        for p in pn:
            x = p.GetSubProcesses() # Get the subprocesses, i.e. processes one level down
            n = 0 # Count index, since this is used when pop'ing the process from SubProcesses list
            for y in x: # Go through all sub processes and check for id, i.e. iterate through the children
                print 'SubProcesses', y.GetId()
                if (y.GetId() == id):
                    print 'Debug: Adding process ', id
                    p.AddSubProcess(newProcessName, 'h', n+1) # Default to adding 'Huvudprocesser'. Will be changed later when populating a test set of processes is not needed anymore.
                    return # This is needed since x is a reference and will have increased after adding the process, thus will never end the for-loop
            if len(x) == 0:
                return
            else:
                self.AddProcess(x, id, newProcessName)

    # AddChildProcess: Adds a child process to metainfo. The new process name is given. The location will be as a child process to the process with given process id.
    # Usage: self.AddProcess(self.meta, self.foundProcess.GetId(), name) # Note, when adding it is the clicked process parent that must be the start. Thus, start with meta[0] i.e. 'root' and go through it's subprocesses to find the clicked one
    def AddChildProcess(self, pn, id, newProcessName):
        print 'AddChildProcess called' # !!!
        for p in pn:
            x = p.GetSubProcesses() # Get the subprocesses, i.e. processes one level down
            n = 0 # Count index, since this is used when pop'ing the process from SubProcesses list
            for y in x: # Go through all sub processes and check for id, i.e. iterate through the children
                print 'SubProcesses', y.GetId()
                if (y.GetId() == id):
                    print 'Debug: Adding child process ', id
                    y.AddSubProcess(newProcessName, 's', n) # Note the 's' type that initializes a sub process
                    return # This is needed since x is a reference and will have increased after adding the process, thus will never end the for-loop
            if len(x) == 0:
                return
            else:
                self.AddChildProcess(x, id, newProcessName)


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
                self.RenameProcess(x, id)


    '''
    def PopulateTreeview(self, pn, node):
        
        # parent = QtGui.QTreeWidgetItem(self.treeProcesses)
        # parent.setText(0, p.Info())
        # parent.setData(0, 1, p.GetId())
        for p in pn:
            print 'PopulateTreeView', p.Info()
            x = p.GetSubProcesses()
            if len(x) == 0:
                parent = QtGui.QTreeWidgetItem(node)
                parent.setText(0, p.Info())
                parent.setData(0, 1, p.GetId())
                #print 'PopulateTreeView len(x)==0 adding', p.Info()
                return
            else:
                parent = QtGui.QTreeWidgetItem(node)
                parent.setText(0, p.Info())
                parent.setData(0, 1, p.GetId())
                #print 'PopulateTreeView len(x)!=0 adding', p.Info()
                self.PopulateTreeview(x, parent)
    '''

    def PopulateTreeView(self, pn, node):
        
        y = pn.GetSubProcesses()
        for x in y:
            parent = QtGui.QTreeWidgetItem(node)
            parent.setText(0, x.Info())
            parent.setData(0, 1, x.GetId())
            z = x.GetSubProcesses()
            if len(z) != 0:
                self.PopulateTreeView(x, parent)
        return

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
        # self.PopulateTreeView(self.meta[0], self.treeProcesses)
            

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
        #print "Handle treeProcess changed"
        dummy = 0

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
        pickle.dump(self.meta[0], pickle_file)

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
        self.meta = [] # Clear the metainfo before loading from file
        self.meta.append(pickle.load(pickle_file))
        self.treeProcesses.clear()
        #self.PopulateTreeview(self.meta[0].GetSubProcesses(), self.treeProcesses)
        self.PopulateTreeView(self.meta[0], self.treeProcesses)
        
        #debugText = 'Processes'
        #for p in self.processes:
        #    debugText += p.get_name()
        #self.txtDebug.setText(debugText)
                
            
    # Handler for the table view
    def tableCellClick(self, row, col):
        #print "Click on table: " + str(row) + " " + str(col) + " data: " + self.m_table.item(row,col).text()
        print "Click on table: " + str(row) + " " + str(col) + " data: " + unicode(QtCore.QString(self.m_table.item(1,1).text()))

    # XAddProcessToParentByName: Search the tree and adds process with name 'name' to the parent with name given in 'parent'.
    # First finds the parent to the process with the required name. Then simply deletes the process from the subprocess list
    def XAddProcessToParentByName(self, parent, name):

        print 'XAddProcessToParentByName called. Parent:', parent, ' New process: ', name      

        # Adding the root process is a special case
        if name == 'root':
            self.meta = metainfo.Process('root')
            print 'root process added'
            return
            
        found = self.XFindProcessByName(self.meta, parent)
        if found != None:
            found.XAddSubProcess(name)
            print 'Process added'
        else:
            print 'Parent not found'
        return

    # XDeleteProcessByName: Search the tree and delete process 'name'
    # First finds the parent to the process with the required name. Then simply deletes the process from the subprocess list
    def XDeleteProcessByName(self, name):

        print 'XDeleteProcessByName called. Process to delete:', name      

        parent = self.XFindParentToProcessByName(self.meta, name)
        if parent != None:
            print 'Parent found, name is', parent.GetName(), 'now deleting the process'
            parent.XDeleteSubProcessByName(name)

        return

    # _XFindParentToProcessByName: Helper function that does the heavy lifting in finding a parent to a process with a given name
    def _XFindParentToProcessByName(self, process, name, parent=None):

        # Action part. Check whether the process is found. If so, return, unwinding the search
        #print '_XFindParentToProcessByName called. Process:', process.Info(), ' Name:', name
        if (process.GetName() == name):
            self._foundProcess = parent
            return
        # The evaluation part. Whether to recurse further into the tree or return to unwind          
        subProcesses = process.GetSubProcesses()
        if len(subProcesses) != 0:
            for p in subProcesses:
                self._XFindParentToProcessByName(p, name, process)
            return
        else:
            return


    # XFindParentToProcessByName: Search the tree for a parent to a process with a given name.
    #                    This is the entry point, a wrapper around the _XFindParentToProcessByName() that does the actual search
    # Usage: self.FindParent(self.meta.GetSubProcesses(), 'parent name')
    #        Stores result in global variable self.foundProcess, should be made more nice but do not have time...
    def XFindParentToProcessByName(self, process, name):

        print 'XFindParentToProcessByName called. Process:', process.Info(), ' Name:', name
        self._foundProcess = None
        self._XFindParentToProcessByName(process, name)
        return self._foundProcess            


    # _findProcessByID: Helper function that does the heavy lifting in finding a process with a given id
    def _XfindProcessByID(self, process, id):

        # Action part. Check whether the process is found. If so, return, unwinding the search
        #print '_findProcessByName called. Process:', process.Info(), ' Name:', name
        if (process.GetId() == id):
            self._foundProcess = process
            return
        # The evaluation part. Whether to recurse further into the tree or return to unwind          
        subProcesses = process.GetSubProcesses()
        if len(subProcesses) != 0:
            for p in subProcesses:
                self._XfindProcessByID(p, id)
            return
        else:
            return


    # FindProcessByID: Search the tree for a process with a given id
    #                    This is the entry point, a wrapper around the _findProcessByID() that does the actual search
    # Usage: self.FindProcess(self.meta.GetSubProcesses(), 'process id')
    #        Stores result in global variable self.foundProcess, should be made more nice but do not have time...
    def XFindProcessByID(self, process, id):

        print 'FindProcessByID called. Process:', process.Info(), ' ID:', id
        self._foundProcess = None
        self._XfindProcessByID(process, id)
        return self._foundProcess


    # _findProcessByName: Helper function that does the heavy lifting in finding a process with a given name
    def _XfindProcessByName(self, process, name):

        # Action part. Check whether the process is found. If so, return, unwinding the search
        #print '_findProcessByName called. Process:', process.Info(), ' Name:', name
        if (process.GetName() == name):
            self._foundProcess = process
            return
        # The evaluation part. Whether to recurse further into the tree or return to unwind          
        subProcesses = process.GetSubProcesses()
        if len(subProcesses) != 0:
            for p in subProcesses:
                self._XfindProcessByName(p, name)
            return
        else:
            return


    # FindProcessByName: Search the tree for a process with a given name.
    #                    This is the entry point, a wrapper around the _findProcessByName() that does the actual search
    # Usage: self.FindProcess(self.meta.GetSubProcesses(), 'process name')
    #        Stores result in global variable self.foundProcess, should be made more nice but do not have time...
    def XFindProcessByName(self, process, name):

        print 'FindProcessByName called. Process:', process.Info(), ' Name:', name
        self._foundProcess = None
        self._XfindProcessByName(process, name)
        return self._foundProcess

    # RenderProcessesInTreeView: Visualizes the meta information process tree in the tree view
    # Usage: self.RenderProcesses(self.meta)
    def _XRenderProcessesInTreeView(self, process, parent):
        
        # Action part. Render the process name and id
        print '_XRenderProcessesInTreeView called. Process:', process.Info()
        child = QtGui.QTreeWidgetItem(parent)
        child.setText(0, process.GetName())
        child.setData(0, 1, process.GetId())
        subProcesses = process.GetSubProcesses()
        # The evaluation part. Whether to recurse further into the tree or return to unwind
        if len(subProcesses) != 0:
            for p in subProcesses:
                self._XRenderProcessesInTreeView(p, child)
            return
        else:
            return

    # RenderProcessesInTreeView: Visualizes the meta information process tree in the tree view
    # Usage: self.RenderProcessesInTreeView(self.meta)
    def XRenderProcessesInTreeView(self, process):

        # Action part. Render the process name and id
        print 'XRenderProcessesInTreeView called. Process:', process.Info()
        self._XRenderProcessesInTreeView(process, self.treeProcesses) # Call helper function with reference to the tree view

        return


    # RenderProcessesInTreeView: Visualizes the meta information process tree in the tree view
    # Usage: self.RenderProcesses(self.meta)
    #def XRenderProcessesInTreeView(self, process, parent):

        # Action part. Render the process name and id
    #    print 'XRenderProcessesInTreeView called. Process:', process.Info()
    #    child = QtGui.QTreeWidgetItem(parent)
    #    child.setText(0, process.GetName())
    #    child.setData(0, 1, process.GetId())
    #    subProcesses = process.GetSubProcesses()
        # The evaluation part. Whether to recurse further into the tree or return to unwind
    #    if len(subProcesses) != 0:
    #        for p in subProcesses:
    #            self.XRenderProcessesInTreeView(p, child)
    #        return
    #    else:
    #        return

        '''
        y = pn.GetSubProcesses()
        for x in y:
            parent = QtGui.QTreeWidgetItem(node)
            parent.setText(0, x.Info())
            parent.setData(0, 1, x.GetId())
            z = x.GetSubProcesses()
            if len(z) != 0:
                self.PopulateTreeView(x, parent)
        return
        '''

        '''
        print 'XRenderProcessesInTreeView called'
        parent = QtGui.QTreeWidgetItem(self.treeProcesses)
        parent.setText(0, 'root')
        parent.setData(0, 1, '1234')
        child = QtGui.QTreeWidgetItem(parent)
        child.setText(0, 'child 1')
        child.setData(0, 1, '1234')
        child = QtGui.QTreeWidgetItem(parent)
        child.setText(0, 'child 2')
        child.setData(0, 1, '1234')
        '''
            

    # RenderProcesses: Visualizes the meta information process tree on command line
    # Usage: self.RenderProcesses(self.meta)
    def XRenderProcesses(self, process):

        # Action part. Render the process name and id and all items
        print 'RenderProcesses called. Process:', process.Info()
        items = process.GetItems()
        for item in items:
            print 'Item - Name:', item.GetName(), 'Value:', item.GetValue(), 'Comment:', item.GetComment()

        subProcesses = process.GetSubProcesses() 
        # The evaluation part. Whether to recurse further into the tree or return to unwind
        if len(subProcesses) != 0:
            for p in subProcesses:
                self.XRenderProcesses(p)
            return
        else:
            return


    # Test Unicode
    def test_unicode(self):
        self.XRenderProcesses(self.meta)
        self.treeProcesses.clear()       
        self.XRenderProcessesInTreeView(self.meta)
        print 'Find process 11'
        found = self.XFindProcessByName(self.meta, '11')
        print 'Result: ', found.Info()
        print 'Find parent to process 11'
        found = self.XFindParentToProcessByName(self.meta, '11')
        print 'Result: ', found.Info()
        print 'Find process 221'
        found = self.XFindProcessByName(self.meta, '221')
        print 'Result: ', found.Info()
        print 'Find parent to process 221'
        found = self.XFindParentToProcessByName(self.meta, '221')
        print 'Result: ', found.Info()
        print 'Deleting process 22 and showing the resulting tree'
        self.XDeleteProcessByName('22')
        self.XRenderProcesses(self.meta)
        self.treeProcesses.clear()       
        self.XRenderProcessesInTreeView(self.meta)


    # Handler for the 'Ok'-button saving the table view information
    def cmdOkTableViewClick(self):
        print 'Ok button clicked - Saving changes'
        table = QtGui.QTableWidget(self.tableWidget)
        #print unicode(QtCore.QString(self.m_table.item(1,1).text()))

        # Get the table data and save into the data structure
        if (self.processInFocus != None):
            print 'Process in focus: Name:', self.processInFocus.GetName(), 'Id:', self.processInFocus.GetId()
            items = self.processInFocus.GetItems()
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
        found = self.XFindProcessByID(self.meta, index.data(1).toString())
        
        #self.foundProcess = None # Initialise the result
        #self.FindProcess(self.meta[0].GetSubProcesses(), index.data(1).toString())
        if (found != None):
            
            items = found.GetItems()
            print 'Found process! Name:', found.GetName(), 'Id:', found.GetId(), 'Items:', items

            # Set the process in focus
            self.processInFocus = found

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
        # There are no difference in handling levels within the process tree
        # This code is left 'just in case...'
        if level == 0:
            Action = menu.addAction(self.tr("Add new process (same level)"))
            Action.triggered.connect(self.treeProcessAddProcess)
            Action = menu.addAction(self.tr("Add new child process"))
            Action.triggered.connect(self.treeProcessAddChildProcess)
            Action = menu.addAction(self.tr("Delete process"))
            Action.triggered.connect(self.treeProcessDeleteProcess)
            Action = menu.addAction(self.tr("Rename process"))
            Action.triggered.connect(self.treeProcessRenameProcess)

        else:
            Action = menu.addAction(self.tr("Add new process (same level)"))
            Action.triggered.connect(self.treeProcessAddProcess)
            Action = menu.addAction(self.tr("Add new child process"))
            Action.triggered.connect(self.treeProcessAddChildProcess)
            Action = menu.addAction(self.tr("Delete process"))
            Action.triggered.connect(self.treeProcessDeleteProcess)
            Action = menu.addAction(self.tr("Rename process"))
            Action.triggered.connect(self.treeProcessRenameProcess)
  
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
            self.AddProcess(self.meta, self.foundProcess.GetId(), newProcessName)
            self.treeProcesses.clear()
            #self.PopulateTreeview(self.meta[0].GetSubProcesses(), self.treeProcesses)
            self.PopulateTreeView(self.meta[0], self.treeProcesses)
            print 'Process added:', newProcessName

        else:
            print 'No new process added'

    # Context menu action for adding a new child process, i.e. a process is added as a child to the process being clicked at
    # This function is called as result of click on context menu, created in opentreeProcessContextMenu() above
    # The process selected in the tree is communicated via global variable self.foundProcess, which in turn is populated from the
    # function on_treeView_clicked(), which is also called when the right click happens.
    def treeProcessAddChildProcess(self):
        newProcessName, ok = QtGui.QInputDialog.getText(self, u'Lägg till ny process', u'Processnamn:')
        if ok:
            print 'New child process name: ', unicode(newProcessName)
            # Add the process
            self.AddChildProcess(self.meta, self.foundProcess.GetId(), newProcessName)
            self.treeProcesses.clear()
            #self.PopulateTreeview(self.meta[0].GetSubProcesses(), self.treeProcesses)
            self.PopulateTreeView(self.meta[0], self.treeProcesses)
            print 'Child process added:', newProcessName

        else:
            print 'No new child process added'

    # Context menu action for deleting a process
    def treeProcessDeleteProcess(self):
        text, ok = QtGui.QInputDialog.getText(self, u'Tag bort process', u'Ok att process raderas?')
        if ok:
            self.DeleteProcess(self.meta, self.foundProcess.GetId()) # Note, when deleting it is the clicked process parent that must be the start. Thus, start with meta[0] i.e. 'root' and go through it's subprocesses to find the clicked one
            self.treeProcesses.clear()
            #self.PopulateTreeview(self.meta[0].GetSubProcesses(), self.treeProcesses)
            self.PopulateTreeView(self.meta[0], self.treeProcesses)
            print 'Process deleted'
        else:
            print 'Process not deleted'


    # Context menu for renaming a process in the tree view
    def treeProcessRenameProcess(self):
        newProcessName, ok = QtGui.QInputDialog.getText(self, u'Byt namn på process', u'Processnamn:', QtGui.QLineEdit.Normal, self.foundProcess.Info())
        if ok:
            print 'New process name: ', unicode(newProcessName)
            # Add the process
            self.RenameProcess(self.meta[0].GetSubProcesses(), self.foundProcess.GetId(), newProcessName)
            self.treeProcesses.clear()
            #self.PopulateTreeview(self.meta[0].GetSubProcesses(), self.treeProcesses)
            self.PopulateTreeView(self.meta[0], self.treeProcesses)

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
