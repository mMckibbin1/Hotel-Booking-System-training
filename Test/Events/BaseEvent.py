class BaseEventobj:
    def __init__(self, noGuests: object, nameOfContact: object, address: object, contactNo: object, eventRoomNo: object, dateOfEvent: object, dateOfBooking: object,ID,
                 costPerHead: object) -> object:
        self.noGuests = noGuests
        self.nameOfContact = nameOfContact
        self.address = address
        self.contactNo = contactNo
        self.eventRoomNo = eventRoomNo
        self.dateOfEvent = dateOfEvent
        self.dateOfBooking = dateOfBooking
        self.costPerHead = costPerHead
        self.ID = ID

def CalbandPrice(bandName):
    if bandName == "Lil\' Febrezey":
        return 100

    elif bandName == "Prawn Mendes":
        return 250

    elif bandName == "AB/CD":
        return 500
    else:
        return 0