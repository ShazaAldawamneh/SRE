class Bus:
    def __init__(self, id):
        self.id = id
        self.charge = 100
        self.status = "parked"
        self.routeID = None
        self.endOfJourney = False

    def getID(self):
        return self.id

    def setCharge(self,newCharge) -> int:
        self.charge = newCharge

    def getCharge(self):
        return self.charge

    def setStatus(self,newStatus) -> str:
        self.status = newStatus
    
    def getStatus (self):
        return self.status
    def setRouteID(self,newRoute) -> str:
        self.routeID = newRoute
    
    def getRouteID(self):
        return self.routeID
    
    def getEndOfJourney(self):
        return self.endOfJourney
    def endOfJourneyFalse(self):
        self.endOfJourney = False
    def endOfJourneyTrue(self):
        self.endOfJourney = True

    def __str__(self):
        return (str(self.id)+str(self.charge)+str(self.status)+str(self.routeID)+str(self.endOfJourney))

