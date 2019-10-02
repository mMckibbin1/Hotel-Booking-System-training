import Gui.BaseCreateForm
from tkinter import *
import Events.Party
import Validation
from Gui import DialogBoxes
from Database import dbHelper
from tkinter import messagebox


class bookParty(Gui.BaseCreateForm.BaseEvent):

    bandName = ''

    def __init__(self, master):
        # room options available for event type
        RoomOption = ['D', 'E', 'F', 'G']
        super(bookParty, self).__init__(master)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Book a Party")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        # Labels for Party booking form
        self.lblSubheading.config(text="Please Fill in the Details for the Party")
        self.lblBandName = Label(master, text="Band Name",font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblBandName.grid(row=7, columnspan=2,pady=(25, 0), padx=(10, 10))

        # dropdowns for party form
        self.om_band_name = StringVar()
        self.om_band_name.set("Please Select a date first")
        self.OpmBandName = OptionMenu(master, self.om_band_name, ())
        self.OpmBandName.config(state="disabled")
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        self.OpmEventRoomNumber.config(state="disabled")

        self.display_date.trace('w', lambda name, index, mode: [self.party_room_check(),self.band_name_check()])

        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [self.validation()])

    def band_name_check(self):
        self.OpmBandName.config(state="normal")

        self.band_name_option_menu_menu = self.OpmBandName.children["menu"]
        self.band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set("Pick a band")
        for value in dbHelper.bands_in_use(self.display_date.get()):
            self.band_name_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_band_name.set(v))

    def party_room_check(self):
        self.OpmEventRoomNumber.config(state="normal")

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")

        rooms_free = dbHelper.rooms_in_use("partyTable", self.display_date.get())
        if len(rooms_free) <1:
            self.om_room_val.set("No Rooms Free")
            return
        for value in rooms_free:
            self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    # validation
    def validation(self):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.", parent=self.master)

        elif dbHelper.date_conflict("partyTable", self.display_date.get(), self.om_room_val):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntnumberOfguest.get()]):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have more than one guest.", parent=self.master)

        if valpassed:
            Events.Party.createParty(
                self.EntnumberOfguest.get(),
                self.EntnameOfContact.get(),
                self.EntAddress.get(),
                self.EntContactNumber.get(),
                self.om_room_val.get(),
                self.display_date.get(),
                self.om_band_name.get())

            DialogBoxes.saved(self.master)
            self.master.destroy()

    def savelist(self):
        self.validationTestList = []
        self.validationTestList.append(self.EntnumberOfguest.get())
        self.validationTestList.append(self.EntnameOfContact.get())
        self.validationTestList.append(self.EntAddress.get())
        self.validationTestList.append(self.EntContactNumber.get())
        self.validationTestList.append(self.om_room_val.get())
        self.validationTestList.append(self.display_date.get())
        self.validationTestList.append(self.om_band_name.get())
        return self.validationTestList

