class Vehicle:
    #atribut
    __type = ""
    __age = 0
    __typeVech = ""
    __fuel = ""
    __maxPass = 0
    __moves = 0
    
    #constructor
    def __init__(self, type = "",age = 0,typeVech = "", fuel="", maxPass=0, moves=0):
        self.__type = type
        self.__age = age
        self.__typeVech = typeVech
        self.__fuel = fuel
        self.__maxPass = maxPass
        self.__moves = moves
        
    def setVech(self, type = "",age = 0, typeVech = "", fuel="", maxPass=0, moves=0):
        self.__type = type
        self.__age = age
        self.__typeVech = typeVech
        self.__fuel = fuel
        self.__maxPass = maxPass
        self.__moves = moves
        
        
    def setType(self, type = ""):
        self.__type = type
        
    def getType(self):
        return self.__type
    
    def setAge(self, age = 0):
        self.__age = age
        
    def getAge(self):
        return self.__age
    
    def setTypeVech(self, typeVech = ""):
        self.__typeVech = typeVech
        
    def getTypeVech(self):
        return self.__typeVech
    
    def setFuel(self, fuel = ""):
        self.__fuel = fuel
        
    def getFuel(self):
        return self.__fuel
    
    def setMaxPass(self, maxPass = 0):
        self.__maxPass = maxPass
        
    def getMaxPass(self):
        return self.__maxPass
    
    def setMoves(self, moves = 0):
        self.__moves = moves
        
    def getMoves(self):
        return self.__moves
    

    def output(self):
        print("=====================================")
        print("              "+str(self.getType()))
        print("-------------------------------------")
        print("Age (Months)         : "+str(self.getAge()))
        print("Type                 : "+str(self.getTypeVech()))
        print("Fuel                 : "+str(self.getFuel()))
        print("Maximum Passengers   : "+str(self.getMaxPass()))
        print("Moves (0/1)          : "+str(self.getMoves()))
        
        
    
        
        
    
    