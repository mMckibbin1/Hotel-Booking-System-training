import Events.BaseEvent
import datetime
from Database import dbHelper


class Wedding(Events.BaseEvent.BaseEventobj):

    bandPrice = 0

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 bandName, noBedroomsReserved, bandPrice, ID):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking, ID,
                         costPerHead=0)

        self.bandName = bandName
        self.costPerHead = 30.0
        self.noBedroomsReserved = noBedroomsReserved
        self.bandPrice = Events.BaseEvent.CalbandPrice(bandName)

    def guestsCost(self):
        return self.costPerHead * self.noGuests

    def VAT(self):
        return self.grosstotal() / 5

    def grosstotal(self):
        return float (self.costPerHead * self.noGuests) + self.bandPrice

    def netTotal(self):
        return self.grosstotal() + self.VAT()


# method to take data from form and add additional required data in order to create object to save to database
def createwedding(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, BandName, bedRoomsRes):

    ID = None
    bandPrice = 0
    DateofBooking = datetime.datetime.now()

    Newwedding = Wedding(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, DateofBooking,
                         BandName, bedRoomsRes, bandPrice, ID)
    return dbHelper.insertwedding(Newwedding)

# method to take data from form and update the selected booking
def updateWedding(noOfGuest, nameOfContact, address, contactNo, DateofEvent, eventRoomNumber, CompanyName, NoOfDays, projectorRequired):

  print("not yet working :)")