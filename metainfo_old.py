import pickle

arrProcesses = []

# Test of inheritance. This is the base class        
class cProcess:

    Names = ['Typ av strukturenhet', 'Klassificering', 'Namn', 'Tid', 'Foregicks av']
    m_strName = ''
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
    



    def __init__(self, a_strName):
        self.m_strName = a_strName
        print 'Constructing cProcess', self.m_strName
     
    def sayHi(self):
        print 'This is a process named: ', self.m_strName

    def getName(self):
        return self.m_strName

    def getStrukturEnhet(self):
        return self.TypAvStrukturEnhet

    def addInfo(self, strukturEnhet):
        print 'Adding type of strukturenhet ', strukturEnhet 
        self.typAvStrukturEnhet = strukturEnhet  

def AddProcess(a_strName):
    print 'Hi from AddProcess'
    arrProcesses.append(cProcess(a_strName))    

def ShowProcesses():
    for p in arrProcesses:
        print 'Hi from: ', p.getName(), ' Strukturenhet: ', p.getStrukturEnhet()

def FindProcess(id):
    for p in arrProcesses:
        if (p.getName() == id):
            print 'Found process', id

def AddInformation(id, typAvStrukturEnhet):
    for p in arrProcesses:
        if (p.getName() == id):
            print 'Found process', id


def SaveProcesses():
    print 'Hi from SaveProcesses'

def LoadProcesses():
    print 'Hi from LoadProcesses'