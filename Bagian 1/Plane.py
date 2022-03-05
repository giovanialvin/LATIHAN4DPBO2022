from Vehicle import Vehicle

class Plane(Vehicle):
    __wingsLength = ""
    #constructor
    def __init__(self, type="", age=0, typeVech="", fuel="", maxPass=0, moves=0, wingsLength = ""):
        super().__init__(type, age, typeVech, fuel, maxPass, moves)
        self.__wingsLength = wingsLength
    
    def setPlane(self, type="", age=0, typeVech="", fuel="", maxPass=0, moves=0, wingsLength = ""):
        self.setVech(type, age, typeVech, fuel, maxPass, moves)
        self.__wingsLength = wingsLength
    
    def setWingsLength(self, wingsLength = "") :
        self.__wingsLength = wingsLength
        
    def getwingsLength(self):
        return self.__wingsLength
    
    def outputPlane(self):
        self.output()
        print("Length of Wings(m)   : "+str(self.getwingsLength()))
        print("=====================================")