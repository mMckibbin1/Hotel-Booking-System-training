"""module contains class used to create the UI for the update Wedding form"""

from tkinter import *
from tkinter import messagebox
import Events.Wedding
import Gui.BaseEditForm
import Validation
from Database import dbHelper
from Gui import DialogBoxes


class EditWedding(Gui.BaseEditForm.BaseEditEvent):
    # setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''
    bandName = ''

    def __init__(self, master, booking, view_booking_self):
        super().__init__(master, booking)
        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Update Selected Wedding")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        self.view_booking_self = view_booking_self
        self.booking = booking

        # Labels for Wedding booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblBandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblBandName.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoOfRoomsRes = Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"),
                                     bg="#70ABAF")
        self.lblNoOfRoomsRes.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes, drop downs and date picker for wedding form
        self.om_band_name = StringVar()
        self.om_band_name.set("Please Select a date first")
        self.OpmBandName = OptionMenu(master, self.om_band_name, ())

        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)

        # Entry boxes, drop downs and date picker for wedding form being placed using grid layout
        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.Beds_VCMD = (self.EntBedroomReserved.register(lambda p: Validation.max_size_50(p, master)))
        self.EntBedroomReserved.config(validate='key', validatecommand=(self.Beds_VCMD, '%P'))

        # Buttons for Add and Cancel on the wedding form
        self.btnUpdateBooking.config(command=lambda: self.validation(booking))  # calls update ,destroy and message box

        self.display_date.trace('w', lambda name, index, mode: [self.wedding_room_check(), self.band_name_check()])

        # Buttons for Add and Cancel on the wedding form being placed using grid layout
        self.populate_form_wedding(booking)

        self.band_name_option_menu_menu = self.OpmBandName.children["menu"]
        self.band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set(booking.bandName)
        for value in dbHelper.bands_in_use_update("Wedding",self.display_date.get(), self.booking.ID):
            self.band_name_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_band_name.set(v))

    def band_name_check(self):
        self.OpmBandName.config(state="normal")

        self.band_name_option_menu_menu = self.OpmBandName.children["menu"]
        self.band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set("Pick a Band")
        for value in dbHelper.bands_in_use_update("Wedding",self.display_date.get(), self.booking.ID):
            self.band_name_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_band_name.set(v))

    def wedding_room_check(self):
        self.OpmEventRoomNumber.config(state="normal")

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")

        rooms_free = dbHelper.rooms_in_use_update(event_type="weddingTable", id=self.booking.ID, date=self.display_date.get())
        if len(rooms_free) <1:
            self.om_room_val.set("No Rooms Free")
            return
        for value in rooms_free :
            self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    def populate_form_wedding(self, booking):
        self.om_band_name.set(booking.bandName)
        self.EntBedroomReserved.insert(0, booking.noBedroomsReserved)

# validation
    def validation(self, booking):
        val_passed = True

        if Validation.string_empty(self.save_list()):
            val_passed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.", parent=self.master)

        elif dbHelper.date_conflict_update("weddingTable", self.display_date.get(), self.om_room_val.get(), booking.ID):
            val_passed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked.\n'
                                       'Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntNumberOfGuest.get()]):
            val_passed = False
            return messagebox.showinfo("Booking Failed", "Must have entered more than one guest.", parent=self.master)

        if val_passed:
            Events.Wedding.update_wedding(self.EntNumberOfGuest.get(),
                                          self.EntNameOfContact.get(),
                                          self.EntAddress.get(),
                                          self.EntContactNumber.get(),
                                          self.om_room_val.get(),
                                          self.display_date.get(), booking.dateOfBooking,
                                          self.om_band_name.get(),
                                          self.EntBedroomReserved.get(),
                                          booking.ID)
            DialogBoxes.updated(self, master=self.master, view_booking=self.view_booking_self)
            self.master.destroy()

    def save_list(self):
        validation_test_list = [self.EntNumberOfGuest.get(), self.EntNameOfContact.get(), self.EntAddress.get(),
                                self.EntContactNumber.get(), self.display_date.get(), self.om_room_val.get(),
                                self.om_band_name.get(), self.EntBedroomReserved.get()]
        return validation_test_list
