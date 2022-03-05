from Person import Person
#composition
class Job:
    #atribut
    PersonObj = Person()
    __NIP = 0
    __Company = ""
    __Position = ""
    
    def __init__(self, P = Person(), nip = 0, company = "", pos=""):
        self.PersonObj = P
        self.__NIP = nip
        self.__Company = company
        self.__Position = pos
        
    def setPerson(self, P = Person()):
        self.PersonObj = P
    
    def getPerson(self):
        return self.PersonObj
    
    def setNIP(self, nip = 0):
        self.__NIP = nip
        
    def getNIP(self):
        return self.__NIP
    
    def setCompany(self, comp = ""):
        self.__Company = comp
        
    def getCompany(self):
        return self.__Company
    
    def setPosition(self, pos = ""):
        self.__Position = pos
        
    def getPosition(self):
        return self.__Position
    
    def outputJob(self):
        self.PersonObj.output()
        print("NIP                      : "+str(self.getNIP()))
        print("Perusahaan               : "+str(self.getCompany()))
        print("Jabatan                  : "+str(self.getPosition()))
        

    