from Vehicle import Vehicle

class Ship(Vehicle):
    __country = ""
    #constructor
    def __init__(self, type="", age=0, typeVech="", fuel="", maxPass=0, moves=0, country = ""):
        super().__init__(type, age, typeVech, fuel, maxPass, moves)
        self.__country = country
    
    def setShip(self, type="", age=0, typeVech="", fuel="", maxPass=0, moves=0, country = ""):
        self.setVech(type, age, typeVech, fuel, maxPass, moves)
        self.__country = country
    
    def setCounty(self, country = "") :
        self.__country = country
        
    def getCountry(self):
        return self.__country
    
    def outputShip(self):
        self.output()
        print("Country              : "+str(self.getCountry()))
        print("=====================================")