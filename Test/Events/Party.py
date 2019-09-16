import Events.BaseEvent
import datetime
from Database import dbHelper


class Party(Events.BaseEvent.BaseEventobj):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, bandPrice, ID):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking, ID,
                         costPerHead=0)
        self.bandName = bandName
        self.costPerHead = 15.0

        self.bandPrice = Events.BaseEvent.CalbandPrice(bandName)

    def CalTotal(self):
        return self.noGuests * self.costPerHead

    def Totalvat(self):
        return

# method to take data from form and add additional required data in order to create object to save to database
def createParty(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, BandName):
    ID = None
    BandPrice = 0
    DateofBooking = datetime.datetime.now()
    NewParty = Party(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, DateofBooking,
                     BandName, BandPrice, ID)
    return dbHelper.insertParty(NewParty)