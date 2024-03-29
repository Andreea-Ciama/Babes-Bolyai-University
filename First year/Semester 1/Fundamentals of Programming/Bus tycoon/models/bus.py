class Bus:
    
    def __init__(self,id,routeCode,model,timesUsed):
        self.__id = id
        self.__routeCode = routeCode
        self.__model = model
        self.__timesUsed = timesUsed
        
    def __str__(self):
        return "ID: " + str(self.__id) + "   Route Code: " + str(self.__routeCode) + "   Model: " + self.__model + "   Times Used: " + str(self.__timesUsed)

    @property
    def getID(self):
        return self.__id

    @property
    def getRouteCode(self):
        return self.__routeCode

    @property
    def getTimesUsed(self):
        return self.__timesUsed

    @property
    def getModel(self):
        return self.__model