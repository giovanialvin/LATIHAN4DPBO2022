from Person import Person
from Job import Job

class Driver(Job):
    #atribut
    
    __lisence = 0
    __active = ""
    __vech = ""
    
    #constructor
    def __init__(self, P=Person(), nip=0, company="", pos="", lisence = 0, active = "", vech = ""):
        super().__init__(P, nip, company, pos)
        self.__lisence = lisence
        self.__active = active
        self.__vech = vech
        
    def setPerson(self, p = Person()):
        self.PersonObj = p
    
    
    def getPerson(self):
        return self.PersonObj
    
    
    def setLisence(self, lisence = 0):
        self.__lisence = lisence
    
    
    def getLisence(self) :
        return self.__lisence
    
    
    def setActive(self, active = ""):
        self.__active = active
    
    
    def getActive(self) :
        return self.__active
    
    def setVehicle(self, vech = ""):
        self.__vech = vech
    
    
    def getVehicle(self) :
        return self.__vech
    
    
    def outputDriver(self):
        print("ID SIM                   : "+str(self.getLisence()))
        print("Aktif s.d.               : "+str(self.getActive()))
        print("Jenis Kendaraan          : "+str(self.getVehicle()))
        print("=================================================")
        

    
    
    
        
            