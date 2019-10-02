"""
Event object used as base for all other event objects in the program
It contains the attributes shared by all event objects
"""


class BaseEventObj:
    def __init__(self, no_guests: object, name_of_contact: object, address: object, contact_no: object,
                 event_room_no: object, date_of_event: object, date_of_booking: object, ID,
                 cost_per_head: object) -> object:
        self.noGuests = no_guests
        self.nameOfContact = name_of_contact
        self.address = address
        self.contactNo = contact_no
        self.eventRoomNo = event_room_no
        self.dateOfEvent = date_of_event
        self.dateOfBooking = date_of_booking
        self.costPerHead = cost_per_head
        self.ID = ID


# method used to set band price depending on what band is selected by user
def cal_band_price(band_name):
    if band_name == "Lil\' Febrezey":
        return 100

    elif band_name == "Prawn Mendes":
        return 250

    elif band_name == "AB/CD":
        return 500
    else:
        return 0
