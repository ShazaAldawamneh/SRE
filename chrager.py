class Charger:
    def __init__(self):
        self._busID = None
        self._chargetime = None
        

    def getbusID(self):
        return self._busID
    
    def serbusId(self, busID):
        self._busID = busID
        
    def getchargetime(self):
        return self._chargetime
    
    def setchargetime(self, chargetime):
        self._chargetime = chargetime
        