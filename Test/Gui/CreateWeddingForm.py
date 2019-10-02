"""module used to create UI for create Wedding form"""

from tkinter import *
import Events.Wedding
import Gui.BaseCreateForm
import Validation
from Database import dbHelper
from Gui import DialogBoxes
from tkinter import messagebox


class BookWedding(Gui.BaseCreateForm.BaseEvent):
    def __init__(self, master):
        # Creation of wedding form set title, size ect..
        super().__init__(master)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Book a Wedding")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        # Labels for Wedding booking form
        self.lblSubheading.config(text="Please Fill in the Details for the Wedding")

        self.lblBandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblBandName.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoOfRoomsRes = Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"),
                                     bg="#70ABAF")
        self.lblNoOfRoomsRes.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes and drop downs

        self.om_band_name = StringVar()
        self.om_band_name.set("Please Select a date first")
        self.OpmBandName = OptionMenu(master, self.om_band_name, ())
        self.OpmBandName.config(state="disabled")

        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)
        self.Beds_VCMD = (self.EntBedroomReserved.register(lambda p: Validation.max_size_50(p, master)))
        self.EntBedroomReserved.config(validate='key', validatecommand=(self.Beds_VCMD, '%P'))

        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the wedding form
        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [self.validation()])

        self.OpmEventRoomNumber.config(state="disabled")
        self.display_date.trace('w', lambda name, index, mode: [self.wedding_room_check(), self.band_name_check()])

    def band_name_check(self):
        self.OpmBandName.config(state="normal")

        band_name_option_menu_menu = self.OpmBandName.children["menu"]
        band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set("Pick a Band")
        for value in dbHelper.bands_in_use(self.display_date.get()):
            band_name_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_band_name.set(v))

    def wedding_room_check(self):
        self.OpmEventRoomNumber.config(state="normal")

        room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")

        rooms_free = dbHelper.rooms_in_use("weddingTable", self.display_date.get())
        if len(rooms_free <1):
            self.om_room_val.set("No Rooms Free")
            return
        for value in rooms_free:
            room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    # validation
    def validation(self):
        val_passed = True

        if Validation.string_empty(self.save_list()):
            val_passed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.", parent=self.master)

        elif dbHelper.date_conflict("weddingTable", self.display_date.get(), self.om_room_val):
            val_passed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked.\n'
                                       'Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntNumberOfGuest.get()]):
            val_passed = False
            return messagebox.showinfo("Booking Failed", "Must have entered more than one guest.", parent=self.master)

        if val_passed:
            Events.Wedding.create_wedding(
                self.EntNumberOfGuest.get(),
                self.EntNameOfContact.get(),
                self.EntAddress.get(),
                self.EntContactNumber.get(),
                self.om_room_val.get(),
                self.CalDateOfEvent.get(),
                self.om_band_name.get(),
                self.EntBedroomReserved.get())

            DialogBoxes.saved(self.master)
            self.master.destroy()

    def save_list(self):
        validation_test_list = [self.EntNumberOfGuest.get(), self.EntNameOfContact.get(), self.EntAddress.get(),
                                self.EntContactNumber.get(), self.om_room_val.get(), self.display_date.get(),
                                self.om_band_name.get(), self.EntBedroomReserved.get()]
        return validation_test_list
