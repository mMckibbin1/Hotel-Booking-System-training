import datetime
import Events.BaseEvent
from Database import dbHelper
from Gui import EditConferenceForm


class Conference(Events.BaseEvent.BaseEventobj):

    def __init__(self, noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking,
                 companyName, noOfDays, projectorRequired, ID):
        super().__init__(noGuests, nameOfContact, address, contactNo, eventRoomNo, dateOfEvent, dateOfBooking, ID,
                         costPerHead=0)
        self.companyName = companyName
        self.noOfDays = noOfDays
        self.projectorRequired = projectorRequired
        self.costPerHead = 20.0

    def guestsCost(self):
        return self.costPerHead * self.noGuests

    def grosstotal(self):
        return float(self.costPerHead * self.noGuests) * self.noOfDays

    def VAT(self):
        return self.grosstotal() / 5

    def netTotal(self):
        VAT = self.grosstotal() / 5
        return self.grosstotal() + VAT

# method to take data from form and add additional required data in order to create object to save to database
def createConference(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, CompanyName, NoOfDays, projectorRequired):

    dateofBooking = datetime.datetime.now()
    ID=None
    if projectorRequired == True:
        projectorRequired = 1
    else:
        projectorRequired = 0

    newconference = Conference(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, dateofBooking, CompanyName, NoOfDays, projectorRequired, ID)
    return dbHelper.insertConference(newconference)


# method to take data from form and update the selected booking
def updateConference(noOfGuest, nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, dateofBooking, CompanyName, NoOfDays, projectorRequired, ID):



    if projectorRequired == True:
        projectorRequired = 1
    else:
        projectorRequired = 0

    editConference = Conference(int(noOfGuest), nameOfContact, address, contactNo, eventRoomNumber, DateofEvent, dateofBooking, CompanyName, NoOfDays, projectorRequired, ID)
    dbHelper.updateConference(editConference)