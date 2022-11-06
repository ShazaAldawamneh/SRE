import bus import Bus;
import vehicle import Vehicle;


class CS(object):
    def __init__(self, Bus, Vehicle):
        self._bus = Bus()
        self._charging = False 
        self._Vehicle = Vehicle()
        self._NumChargSpots = 5
        self._spotID = 0
        self._listOfSpots = [] #queue for spots 
        self._spotStatus = True # if specific sport with ID is available 

    def getID(self):
        return self._spotID

    def setID(self):
        for i in range(5):
            self._spotID = i+1
            self._listOfSpots.append(self._spotID)

    def getStatus(self):
        return self._spotStatus

    def setStatus(self,spotID, SpotStatus): #set the availability of the spot  
        spotID._spotStatus= SpotStatus
    
    def busDetected(self):
        if self._spotStatus == True:
            return True
        else:
            False
    
    def busNeeded(self):
        if self._spotStatus == True:
            return False
        else:
            return True 
    def charging(self):
        if CS.busDetected():
            return True
        else:
            return False 
    
    def getCableConnect(self):
        if CS.charging():
            return True
        else:
            return False
    
    def errors(self):
        #if statment 
        return "Error"
        
    def __str__(self) -> str:
        pass
