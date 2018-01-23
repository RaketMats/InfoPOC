import pickle


# This is the meta info
class MetaInformation:

    Name = ''
    Processes = []

    def __init__(self, name):
        self.Name = name
        print 'Constructing MetaInformation', self.Name
        self.Processes = [] # This seemingly unecessary initialisation is needed to pickle the object list.
                            # If not present, the pickle will not contain objects in the list

    def AddProcess(self, name, subName):
        print 'Adding process', name
        self.Processes.append(Process(name, subName))    

    def ShowProcesses(self):
        for p in self.Processes:
            print 'Hi from', p.Name
            p.Info()

    def FindProcess(self, name):
        for p in Processes:
            if (p.Name == name):
                print 'Found process', name


# This is the process        
class Process:

    Name = ''
    #DescriptionElement = {'Typ av strukturenhet': 'null', 'Klassificering': 'null', 'Namn': 'null'}
    DescriptionElement = {}

    def SayHi(self):
        print "DescriptionElement['Name']: ", self.DescriptionElement['Namn']
        print 'Length: ', len(self.DescriptionElement)
        for i in self.DescriptionElement:
            print i
        for i in self.DescriptionElement.items():
            print i[1]

    def Info(self):
        #for i in self.DescriptionElement:
        #    print i
        for i in self.DescriptionElement.items():
            print i[0], i[1]

    def __init__(self, name, subName):
        self.Name = name
        self.DescriptionElement['Typ av strukturenhet'] = 'null'
        self.DescriptionElement['Klassificering'] = 'null'
        self.DescriptionElement['Namn'] = subName
        print 'Constructing Process', self.Name


    '''
    # 1 Typ och identitet
    TypAvStrukturEnhet = ''
    Klassificering = ''
    Namn = ''
    Tid = ''
    ForegicksAv = ''
    # 2 Verksamhet och organisation
    MalOchUppdrag = ''
    JuridiskPerson = ''
    AnsvarigEnhet = ''
    Historik = ''
    VerksamhetsAgara = ''
    # 3 Relation till andra verksamhetsfunktioner
    Relation = ''
    Historik = ''
    # 4 Kontroll
    Identifierare = ''
    Beskrivningsstandard = ''
    BeskrivningStatus = ''
    Ansvarig = ''
    # 5 Dokumentationskrav
    Typ = ''
    Beskrivning = ''
    Ansvarig = ''
    # 6 Sakerhetsklassning
    SakerhetsKlass = ''
    Datum = ''
    Beskrivning = ''
    Ansvarig = ''
    # 7 Varderingsbevarande
    BevarandeMotiv = ''
    SelektivtBevarande = ''
    KontrollPunkt = ''
    Ansvarig = ''
    # 8 Koppling till sysmteforvaltning och arkitektur
    ForvaltningsObjekt = ''
    SystemEllerApplikation = ''
    Arkitektur = ''
    '''

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


    # the main routine    
if __name__ == '__main__':

    
    m = MetaInformation('Root')
    m.AddProcess('Huvudprocess 0', 'Abc')
    m.AddProcess('Huvudprocess 1', 'Def')
    m.AddProcess('Huvudprocess 2', 'Ghi')
    m.AddProcess('Huvudprocess 3', 'Jkl')
    m.AddProcess('Huvudprocess 4', 'Mno')
    
    #m.ShowProcesses()

    
    print 'Saving...'
    pickle_file = file('save.pickle', 'w')
    pickle.dump(m, pickle_file)
    
    '''
    print 'Loading...'
    pickle_file = file('save.pickle')
    m = pickle.load(pickle_file)
    '''
    print 'Showing...'
    m.ShowProcesses()

    '''
    m.Processes[0].DescriptionElement['Name'] = 'Abc'
    m.Processes[1].DescriptionElement['Name'] = 'Def'
    m.Processes[2].DescriptionElement['Name'] = 'Ghi'
    m.ShowProcesses()
    '''

