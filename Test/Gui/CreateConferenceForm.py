"""module used to create UI for create conference form"""

from tkinter import *
import Events.Conference
import Gui.BaseCreateForm
import Validation
from Gui import DialogBoxes
from Database import dbHelper
from tkinter import messagebox


class BookConference(Gui.BaseCreateForm.BaseEvent):
    def __init__(self, master):

        super().__init__(master)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Book a Conference")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        def ch_box_sel():
            """method to get value of checkbutton"""
            print(self.CheckVar1.get())

        # Labels for Conference booking form
        self.lblSubheading.config(text="Please Fill in the Details for the Conference")

        self.lblCompanyName = Label(master, text="Company Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblCompanyName.grid(row=7, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoOfDays = Label(master, text="Number of Days", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoOfDays.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblProjectorReq = Label(master, text="Projector Required", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblProjectorReq.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes, drop downs and date picker for conference form
        self.EntCompanyName = Entry(master, font=("arial", 10), width=50)
        self.CompanyName_VCMD = (self.EntCompanyName.register(lambda p: Validation.max_character_length_150(p, master)))
        self.EntCompanyName.config(validate='key', validatecommand=(self.CompanyName_VCMD, '%P'))

        self.number_of_days = StringVar()
        self.EntNoOfDays = Entry(master, font=("arial", 10), width=50, textvariable=self.number_of_days)
        self.Days_VCMD = (self.EntNoOfDays.register(lambda p: Validation.max_size_31(p, master)))
        self.EntNoOfDays.config(validate='key', validatecommand=(self.Days_VCMD, '%P'))

        # checkbox
        self.CheckVar1 = IntVar()
        self.chxProjectorRequired = Checkbutton(master, text='', variable=self.CheckVar1, onvalue=True, offvalue=False,
                                                bg="#70ABAF", command=ch_box_sel)

        # Entry boxes
        self.EntCompanyName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntNoOfDays.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # checkbox
        self.chxProjectorRequired.grid(row=9, column=2, pady=(25, 0), padx=(0, 25))

        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [self.validation()])

        self.display_date.trace('w', lambda name, index, mode: self.conference_room_check())
        self.number_of_days.trace('w', lambda name, index, mode: self.conference_room_check())

        self.OpmEventRoomNumber.config(state="disabled")
        self.om_room_val.set("Pick a date and duration first")

    def conference_room_check(self):
        """ensures rooms cannot be double booked"""
        if not self.number_of_days.get() or not self.display_date.get():
            self.om_room_val.set("Pick a date and duration first")
            self.OpmEventRoomNumber.config(state="disabled")
            return

        self.OpmEventRoomNumber.config(state="normal")

        room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")

        rooms_free = dbHelper.rooms_in_use("conferenceTable", self.display_date.get(), int(self.number_of_days.get()))
        if len(rooms_free) < 1:
            self.om_room_val.set("No Rooms Free")
            return
        for value in rooms_free:
            room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    # validation
    def validation(self):
        """checks validation is passed and calls a dialog box if it fails"""
        val_passed = True

        if Validation.string_empty(self.save_list()):
            val_passed = False
            return messagebox.showinfo("Booking Failed",
                                       "All fields are required to be filled in.", parent=self.master)

        elif dbHelper.con_date_conflict("conferenceTable", self.display_date.get(), self.EntNoOfDays.get(),
                                        self.om_room_val.get()):
            val_passed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked.\n'
                                       'Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntNumberOfGuest.get(), self.EntNoOfDays.get()]):
            val_passed = False
            return messagebox.showinfo("Booking Failed", "Must have more than one guest.\n"
                                                         "The duration of the event must be at least one day.",
                                       parent=self.master)
        elif not Validation.contact_number_val(self.EntContactNumber.get(), self.EntContactNumber, self.master):
            val_passed = False
            return

        if val_passed:
            Events.Conference.create_conference(
                self.EntNumberOfGuest.get(),
                self.EntNameOfContact.get(),
                self.EntAddress.get(),
                self.EntContactNumber.get(),
                self.om_room_val.get(),
                self.display_date.get(),
                self.EntCompanyName.get(),
                self.EntNoOfDays.get(),
                self.CheckVar1.get())

            DialogBoxes.saved(self.master)
            self.master.destroy()

    def save_list(self):
        """saves entries to a list that is used for validation"""
        validation_test_list = [self.EntNumberOfGuest.get(), self.EntNameOfContact.get(), self.EntAddress.get(),
                                self.EntContactNumber.get(), self.om_room_val.get(), self.display_date.get(),
                                self.EntCompanyName.get(), self.EntNoOfDays.get()]
        return validation_test_list
