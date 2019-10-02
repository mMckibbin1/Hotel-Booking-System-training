"""
Wedding object used for wedding bookings
"""

import Events.BaseEvent
import datetime
from Database import dbHelper




class Wedding(Events.BaseEvent.BaseEventObj):

    bandPrice = 0

    def __init__(self, no_guests, name_of_contact, address, contact_no, event_room_no, date_of_event, date_of_booking,
                 band_name, no_bedrooms_reserved, band_price, ID):
        super().__init__(no_guests, name_of_contact, address, contact_no, event_room_no, date_of_event, date_of_booking,
                         ID, cost_per_head=0)

        self.bandName = band_name
        self.costPerHead = 30.0
        self.noBedroomsReserved = no_bedrooms_reserved
        self.bandPrice = Events.BaseEvent.cal_band_price(band_name)

    def guests_cost(self):
        return self.costPerHead * self.noGuests

    def vat(self):
        return self.gross_total() / 5

    def gross_total(self):
        return float(self.costPerHead * self.noGuests) + self.bandPrice

    def net_total(self):
        return self.gross_total() + self.vat()


# method to take data from form and add additional required data in order to create object to save to database
def create_wedding(no_of_guest, name_of_contact, address, contact_no, event_room_number, date_of_event, band_name,
                   bedrooms_res):

    ID = None
    band_price = 0
    date_of_booking = datetime.datetime.now()

    new_wedding = Wedding(int(no_of_guest), name_of_contact, address, contact_no, event_room_number, date_of_event,
                          date_of_booking, band_name, bedrooms_res, band_price, ID)
    return dbHelper.insertwedding(new_wedding)


# method to take data from form and update the selected booking
def update_wedding(no_of_guest, name_of_contact, address, contact_no, event_room_number, date_of_event, date_of_booking,
                   band_name, bedrooms_res, ID):

    band_price = 0

    edit_wedding = Wedding(no_guests=int(no_of_guest), name_of_contact=name_of_contact, address=address,
                           contact_no=contact_no, event_room_no=event_room_number, date_of_event=date_of_event,
                           date_of_booking=date_of_booking, band_name=band_name, band_price=band_price,
                           no_bedrooms_reserved=bedrooms_res, ID=ID)
    dbHelper.updateWedding(edit_wedding)
