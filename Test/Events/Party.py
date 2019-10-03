"""Party object used for Party bookings"""

import Events.BaseEvent
import datetime
from Database import dbHelper


class Party(Events.BaseEvent.BaseEventObj):

    bandPrice = 0

    def __init__(self, no_guests, name_of_contact, address, contact_no, event_room_no, date_of_event, date_of_booking,
                 band_name, band_price, ID):
        super().__init__(no_guests, name_of_contact, address, contact_no, event_room_no, date_of_event, date_of_booking,
                         ID, cost_per_head=0)
        self.bandName = band_name
        self.costPerHead = 15.0

        self.bandPrice = Events.BaseEvent.cal_band_price(band_name)

    def guests_cost(self):
        """calculates the cost for guests"""
        return self.costPerHead * self.noGuests

    def vat(self):
        """calculates the VAT"""
        return self.gross_total() / 5

    def gross_total(self):
        """calculates the gross total"""
        return float(self.costPerHead * self.noGuests) + self.bandPrice

    def net_total(self):
        """calculates the overall total"""
        return self.gross_total() + self.vat()


def create_party(no_of_guest, name_of_contact, address, contact_no, event_room_number, date_of_event, band_name):
    """method to take data from form and add additional required data in order to create object to save to database"""
    ID = None
    band_price = 0
    date_of_booking = datetime.datetime.now()
    new_party = Party(int(no_of_guest), name_of_contact, address, contact_no, event_room_number, date_of_event,
                      date_of_booking, band_name, band_price, ID)
    return dbHelper.insertParty(new_party)


def update_party(no_of_guest, name_of_contact, address, contact_no, event_room_number, date_of_event, date_of_booking,
                 band_name, ID):
    """method to take data from form and update the selected booking"""

    band_price = 0

    edit_party = Party(int(no_of_guest), name_of_contact, address, contact_no, event_room_number, date_of_event,
                       date_of_booking, band_name, band_price, ID)
    dbHelper.updateParty(edit_party)
