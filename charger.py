class Charger:
    def __init__(self):
        self.bus = None
        self.chargetime = None
        

    def getBus(self):
        return self.bus
    
    def setBus(self, bus):
        self.bus = bus
        
    def getChargeTime(self):
        return self.chargetime
    
    def setChargeTime(self, chargetime):
        self.chargetime = chargetime

    def reduceChargeTime(self):
        self.chargetime +=1