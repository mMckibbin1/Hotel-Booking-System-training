"""module contains class used to create the UI for the update Party form"""

from tkinter import messagebox
import Gui.BaseEditForm
from tkinter import *
import Events.Party
import Validation
from Database import dbHelper
from Gui import DialogBoxes


class EditParty(Gui.BaseEditForm.BaseEditEvent):
    def __init__(self, master, booking, view_booking_self):
        super().__init__(master, booking)
        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Update Selected Party")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        self.view_booking_self = view_booking_self
        self.booking = booking

        # Labels for Party booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblBandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblBandName.grid(row=7, columnspan=2,pady=(25, 0), padx=(10, 10))

        # Entry boxes, drop downs and date picker for party form
        self.om_band_name = StringVar()
        self.om_band_name.set("Please Select a date first")
        self.OpmBandName = OptionMenu(master, self.om_band_name, ())

        # Entry boxes, drop downs and date picker for party form being placed using grid layout
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        self.display_date.trace('w', lambda name, index, mode: [self.party_room_check(), self.band_name_check()])

        # Buttons for Add and Cancel on the party form
        self.btnUpdateBooking.config(command=lambda: self.validation(booking))  # calls update ,destroy and message box

        self.band_name_option_menu_menu = self.OpmBandName.children["menu"]
        self.band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set(booking.bandName)
        for value in dbHelper.bands_in_use_update("Party", self.display_date.get(), self.booking.ID):
            self.band_name_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_band_name.set(v))

    def band_name_check(self):
        self.OpmBandName.config(state="normal")

        self.band_name_option_menu_menu = self.OpmBandName.children["menu"]
        self.band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set("Pick a Band")
        for value in dbHelper.bands_in_use_update("Party", self.display_date.get(), self.booking.ID):
            self.band_name_option_menu_menu.add_command(label=value,
                                                        command=lambda v=value: self.om_band_name.set(v))

    def party_room_check(self):
        self.OpmEventRoomNumber.config(state="normal")

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")

        rooms_free = dbHelper.rooms_in_use_update(event_type="partyTable", date=self.display_date.get(),
                                                  id=self.booking.ID)
        if len(rooms_free) < 1:
            self.om_room_val.set("No Rooms Free")
            return
        for value in rooms_free:
            self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    def validation(self, booking):
        val_passed = True

        if Validation.string_empty(self.save_list()):
            val_passed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.", parent=self.master)
        elif dbHelper.date_conflict_update("partyTable", self.display_date.get(), self.om_room_val, booking.ID):
            val_passed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked.\n'
                                       'Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntNumberOfGuest.get()]):
            val_passed = False
            return messagebox.showinfo("Booking Failed", "Must have more than one guest.", parent=self.master)
        elif not Validation.contact_number_val(self.EntContactNumber.get(), self.EntContactNumber, self.master):
            val_passed = False
            return

        if val_passed:
            Events.Party.update_party(self.EntNumberOfGuest.get(),
                                      self.EntNameOfContact.get(),
                                      self.EntAddress.get(),
                                      self.EntContactNumber.get(), self.om_room_val.get(),
                                      self.display_date.get(), booking.dateOfBooking,
                                      self.om_band_name.get(), booking.ID)

            DialogBoxes.updated(self, master=self.master, view_booking=self.view_booking_self)
            self.master.destroy()

    def save_list(self):
        validation_test_list = [self.EntNumberOfGuest.get(), self.EntNameOfContact.get(), self.EntAddress.get(),
                                self.EntContactNumber.get(), self.om_room_val.get(), self.display_date.get(),
                                self.om_band_name.get()]
        return validation_test_list
