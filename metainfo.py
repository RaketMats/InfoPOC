# -*- coding: utf-8 -*-

import pickle
import pickletools
import sys
import uuid # For the love of all things sacred, it is called uuid...
from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4 import QtCore

# This is a 'BeskrivningeElement' item
class Item:

    def __init__(self, name='tbd', value='tbd', comment='tbd'):
        self.Name = QtCore.QString(name)
        self.Value = QtCore.QString(value)
        self.Comment = QtCore.QString(comment)

    def AddDescription(self, name='tbd', value='tbd', comment='tbd'):
        self.Name = name
        self.Value = value
        self.Comment = comment

    def GetName(self):
        return self.Name

    def GetValue(self):
        return self.Value

    def GetComment(self):
        return self.Comment
        
    def SetName(self, name):
        self.Name = name

    def SetValue(self, value):
        self.Value = value

    def SetComment(self, comment):
        self.Comment = comment

        
# This is the process element of the meta information structure       
class Process:

    # Initialise to either 'h'=Huvudprocess, 's'=Subprocess, '<empty>'=root
    def __init__(self, name, type='root'):
        self.Name = name
        self.Id = str(uuid.uuid4())
        self.SubProcesses = []
        self.Items = []
        if type=='h':
            self.InitialiseHuvudProcessItems()
        elif type=='s':
            self.InitialiseSubProcessItems()
        else:
            self.XInitialiseItems()
            
        # Else it is a root process that does not have any items
        #print 'Constructing Process', self.Name

    # Return name of the process
    def Info(self):
        return self.Name, self.Id

    # Set name of the process
    def SetName(self, name):
        self.Name = name

    # Get name of the process
    def GetName(self):
        return self.Name

    # Get uuid of the process
    def GetId(self): 
        return self.Id

    def XAddSubProcess(self, name):
        
        print 'XAddSubProcess() called. New process:', name       
        self.SubProcesses.append(Process(name))

    def AddSubProcess(self, name, type, index=None):
        
        print 'AddSubProcess', name
        #print 'Subprocesses before add:'
        #for p in self.SubProcesses:
        #    print p.Info()
        
        if index == None:
            print 'index==None', name
            self.SubProcesses.append(Process(name, type))
        else:
            print 'index!=None', name, index
            self.SubProcesses.insert(index, Process(name, type))
        #print 'Process:', self.Name, ' Adding sub process', name

        print 'Subprocesses after add: size=', len(self.SubProcesses)
        for p in self.SubProcesses:
            print p.Info(), p.GetId()

    def GetSubProcesses(self):
        #print 'Getting sub processes'
        return self.SubProcesses

    # Delete subprocess with a certain index
    def XDeleteSubProcessByName(self, name):

        print 'XDeleteSubProcessByName() called. Process to delete:', name       
        index = 0
        for p in self.SubProcesses:
            if p.GetName() == name:
                self.SubProcesses.pop(index) # (.SubProcesses is a list. Always confusing with different type of arrays, lists etc. and what is supported) 
                print 'Process deleted'
                return
            index = index+1
            
        # Ok, we gone through all sub processes and did not find it
        print 'Process not found'

    # Delete subprocess with a certain index
    def DeleteSubProcess(self, index):
        self.SubProcesses.pop(index) # (.SubProcesses is a list. Always confusing with different type of arrays, lists etc. and what is supported) 

    def XInitialiseItems(self):
        # For now, there is a fixed set of ten items corresponding to the ten rows in the table in the GUI
        self.Items.append(Item(u'Namn', u'tbd', u'tbd'))
        self.Items.append(Item(u'Modell', u'tbd.jpg', u'tbd'))
        self.Items.append(Item(u'tbd', u'tbd', u'tbd'))
        self.Items.append(Item(u'tbd', u'tbd', u'tbd'))
        self.Items.append(Item(u'tbd', u'tbd', u'tbd'))
        self.Items.append(Item(u'tbd', u'tbd', u'tbd'))
        self.Items.append(Item(u'tbd', u'tbd', u'tbd'))
        self.Items.append(Item(u'tbd', u'tbd', u'tbd'))
        self.Items.append(Item(u'tbd', u'tbd', u'tbd'))
        self.Items.append(Item(u'tbd', u'tbd', u'tbd'))

    def InitialiseHuvudProcessItems(self):
        self.Items.append(Item(u'Typ av strukturenhet', u'tbd', u'tbd'))
        self.Items.append(Item(u'Klassificering', u'tbd', u'tbd'))
        self.Items.append(Item(u'Namn', u'tbd', u'tbd'))
        self.Items.append(Item(u'Tid', u'tbd', u'tbd'))
        self.Items.append(Item(u'Föregicks av', u'tbd', u'tbd'))
        self.Items.append(Item(u'Modell', u'xyz.jpg', u'tbd'))

    def InitialiseSubProcessItems(self):
        self.Items.append(Item(u'Mal och Uppdrag', u'tbd', u'tbd'))
        self.Items.append(Item(u'Juridisk person', u'tbd', u'tbd'))
        self.Items.append(Item(u'Ansvarig enhet', u'tbd', u'tbd'))
        self.Items.append(Item(u'Historik', u'tbd', u'tbd'))
        self.Items.append(Item(u'Verksamhetsagare', u'tbd', u'tbd'))
        self.Items.append(Item(u'Modell', u'xyz.jpg', u'tbd'))
        
    def AddItem(self, item):
        self.Items.append(item)

    def GetItems(self):
        return self.Items


# Save the current metainformation to disk
def save_state(self):
    pickle_file = file('save.pickle', 'w')
    pickle.dump(self.processes, pickle_file)

# Load the last metainformation from disk
def load_state(self):
    print 'Hi from load state'
    pickle_file = file('save.pickle')
    self.processes = pickle.load(pickle_file)
    #debugText = 'Processes'
    #for p in self.processes:
    #    debugText += p.get_name()
    #self.txtDebug.setText(debugText)

# Recursive generator through the process tree
# Input is an array of processes, which in turn has sub processes etc. 
def GeneratorProcesses(pn):
   
    for p in pn:
        x = p.GetSubProcesses()
        if len(x) == 0:
            print 'Name:', p.Info(), 'Id:', p.GetId()
            items = p.GetItems()
            for i in items:
                print 'Information: ', unicode(i.GetName()), '=', unicode(i.GetValue()), 'Comment:', unicode(i.GetComment())
            return
        else:
            print 'Name:', p.Info(), 'Id:', p.GetId()
            items = p.GetItems()
            for i in items:
                print 'Information: ', unicode(i.GetName()), '=', unicode(i.GetValue()), 'Comment:', unicode(i.GetComment())
            IterateProcesses(x)


# Recursive iteration through the process tree
# Input is an array of processes, which in turn has sub processes etc. 
def IterateProcesses(pn):

    '''
    for p in pn:
        x = p.GetSubProcesses()
        print 'Name:', p.Info(), ' and subprocesses is', len(x)
    '''
    
    for p in pn:
        x = p.GetSubProcesses()
        if len(x) == 0:
            print 'Name:', p.Info(), 'Id:', p.GetId()
            items = p.GetItems()
            for i in items:
                print 'Information: ', unicode(i.GetName()), '=', unicode(i.GetValue()), 'Comment:', unicode(i.GetComment())
            return
        else:
            print 'Name:', p.Info(), 'Id:', p.GetId()
            items = p.GetItems()
            for i in items:
                print 'Information: ', unicode(i.GetName()), '=', unicode(i.GetValue()), 'Comment:', unicode(i.GetComment())
            IterateProcesses(x)
    

    # the main routine    
if __name__ == '__main__':

    loadFile = ''
    saveFile = ''

    '''
    p = Process('HuvudProcess0', 's')
    #p.InitialiseHuvudProcessItems()
    #i = Item('Typ av strukturenhet', 'Bibliotek', 'No comments')
    #p.AddItem(i)
    #i = Item('Klassificering', 'Supersecure', 'No comments')
    #p.AddItem(i)
    print 'Process', p.Info()
    items = p.GetItems()
    for i in items:
        print 'Information: ', i.GetName(), '=', i.GetValue(), 'Comment:', i.GetComment()
    
    sys.exit(0)
    '''

    # Get filename to pickle
    if len(sys.argv) != 3:
        print 'Missing arguments (load/save, <filename>)'
        sys.exit(0)

    if sys.argv[1] == 'load':
        loadFile = sys.argv[2]
        #loadFile += '.pickle'
        print 'Opening', loadFile
    elif sys.argv[1] == 'save':
        saveFile = sys.argv[2]
        #saveFile += '.pickle'
        print 'Saving to', saveFile
    elif sys.argv[1] == 'debug':        
        print 'Debugging:', sys.argv[2]
        debug_file = file(sys.argv[2])
        pickletools.dis(debug_file)
        sys.exit(0)

    else:
        print 'Unknown command. Arguments are (load/save, <filename>)'

    if loadFile != '':
        print 'Loading...'
        pickle_file = file(loadFile)
        meta = pickle.load(pickle_file)
    
    else:

        meta = Process('root')    
        meta.AddSubProcess('Huvudprocess0', 'h')
        meta.AddSubProcess('Huvudprocess1', 'h')
        meta.AddSubProcess('Huvudprocess2', 'h')
        meta.AddSubProcess('Huvudprocess3', 'h')
        meta.AddSubProcess('Huvudprocess4', 'h')

        l1 = meta.GetSubProcesses()
        # Huvudprocess0
        l1[0].AddSubProcess('Underprocess00', 's')
        l1[0].AddSubProcess('Underprocess01', 's')
        l2 = l1[0].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess000', 's')
        l2[0].AddSubProcess('Underprocess001', 's')
        l2[1].AddSubProcess('Underprocess010', 's')
        l2[1].AddSubProcess('Underprocess011', 's')
        
        # Huvudprocess1
        l1[1].AddSubProcess('Underprocess10', 's')
        l1[1].AddSubProcess('Underprocess11', 's')
        l2 = l1[1].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess100', 's')
        l2[0].AddSubProcess('Underprocess101', 's')
        l2[1].AddSubProcess('Underprocess110', 's')
        l2[1].AddSubProcess('Underprocess111', 's')
        # Huvudprocess2
        l1[2].AddSubProcess('Underprocess20', 's')
        l1[2].AddSubProcess('Underprocess21', 's')
        l2 = l1[2].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess200', 's')
        l2[0].AddSubProcess('Underprocess201', 's')
        l2[1].AddSubProcess('Underprocess210', 's')
        l2[1].AddSubProcess('Underprocess211', 's')
        # Huvudprocess3
        l1[3].AddSubProcess('Underprocess30', 's')
        l1[3].AddSubProcess('Underprocess31', 's')
        l2 = l1[3].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess300', 's')
        l2[0].AddSubProcess('Underprocess301', 's')
        l2[1].AddSubProcess('Underprocess310', 's')
        l2[1].AddSubProcess('Underprocess311', 's')
        # Huvudprocess4
        l1[4].AddSubProcess('Underprocess40', 's')
        l1[4].AddSubProcess('Underprocess41', 's')
        l2 = l1[4].GetSubProcesses()
        l2[0].AddSubProcess('Underprocess400', 's')
        l2[0].AddSubProcess('Underprocess401', 's')
        l2[1].AddSubProcess('Underprocess410', 's')
        l2[1].AddSubProcess('Underprocess411', 's')
        

    # Show processes
    IterateProcesses(meta.GetSubProcesses())

    # Save if requested
    if saveFile != '':
   
        print 'Saving...'
        pickle_file = file(saveFile, 'w')
        pickle.dump(meta, pickle_file)

    
    '''
    print 'Showing...'
    m.ShowProcesses()
    '''
    '''
    m.Processes[0].DescriptionElement['Name'] = 'Abc'
    m.Processes[1].DescriptionElement['Name'] = 'Def'
    m.Processes[2].DescriptionElement['Name'] = 'Ghi'
    m.ShowProcesses()
    '''

