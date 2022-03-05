class Person:
    #atribut
    __NIK = 0
    __Name = ""
    __Gender = ""
    __Sleep = 0
    
    #constructor
    def __init__(self, nik = 0, name= "",gender="", sleep = 0):
        self.__NIK = nik
        self.__Name = name
        self.__Gender = gender
        self.__Sleep = sleep
    
    #get set methods

    
    def setNIK(self, nik = 0):
        self.__NIK = nik
        
    def getNIK(self):
        return self.__NIK
    
    def setName(self, name = ""):
        self.__Name = name
        
    def getName(self):
        return self.__Name
    
    def setGender(self, gender = ""):
        self.__Gender = gender
        
    def getGender(self):
        return self.__Gender
    
    def setSleep(self, sleep = 0):
        self.__Sleep = sleep
        
    def getSleep(self):
        return self.__Sleep
    
    def output(self):
        print("=================================================")
        print("NIK                      : "+str(self.getNIK()))
        print("Nama                     : "+str(self.getName()))
        print("Jenis Kelamin            : "+str(self.getGender()))
        print("Status(Tidur 1/0)        : "+str(self.getSleep()))
        
        
        
    
    
    
    
    
    