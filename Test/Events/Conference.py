"""conference object used for conference bookings"""


import datetime
import Events.BaseEvent
from Database import dbHelper




class Conference(Events.BaseEvent.BaseEventObj):

    def __init__(self, no_guests, name_of_contact, address, contact_no, event_room_no, date_of_event, date_of_booking,
                 company_name, no_of_days, projector_required, ID):
        super().__init__(no_guests, name_of_contact, address, contact_no, event_room_no, date_of_event, date_of_booking,
                         ID, cost_per_head=0)
        self.companyName = company_name
        self.noOfDays = no_of_days
        self.projectorRequired = projector_required
        self.costPerHead = 20.0

    def guests_cost(self):
        return self.costPerHead * self.noGuests

    def gross_total(self):
        return float(self.costPerHead * self.noGuests) * self.noOfDays

    def vat(self):
        return self.gross_total() / 5

    def net_total(self):
        vat = self.gross_total() / 5
        return self.gross_total() + vat


# method to take data from form and add additional required data in order to create object to save to database
def create_conference(no_of_guest, name_of_contact, address, contact_no, event_room_number, date_of_event, company_name,
                      no_of_days, projector_required):

    date_of_booking = datetime.datetime.now()
    ID = None
    if projector_required == True:
        projector_required = 1
    else:
        projector_required = 0

    new_conference = Conference(int(no_of_guest), name_of_contact, address, contact_no, event_room_number,
                                date_of_event, date_of_booking, company_name, no_of_days, projector_required, ID)
    return dbHelper.insertConference(new_conference)


# method to take data from form and update the selected booking
def update_conference(no_of_guest, name_of_contact, address, contact_no, event_room_number, date_of_event,
                      date_of_booking, company_name, no_of_days, projector_required, ID):

    if projector_required == True:
        projector_required = 1
    else:
        projector_required = 0

    edit_conference = Conference(int(no_of_guest), name_of_contact, address, contact_no, event_room_number,
                                 date_of_event, date_of_booking, company_name, no_of_days, projector_required, ID)
    dbHelper.updateConference(edit_conference)