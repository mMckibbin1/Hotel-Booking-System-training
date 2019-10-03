"""module contains class used to create the UI for the update Conference form"""

from tkinter import *
from tkinter import messagebox
import Events.Conference
import Gui.BaseEditForm
import Validation
from Database import dbHelper
from Gui import DialogBoxes


class EditConference(Gui.BaseEditForm.BaseEditEvent):

    def __init__(self, master, booking, view_booking_self):
        super().__init__(master, booking)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Update Selected Conference")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        self.view_booking_self = view_booking_self
        self.booking = booking

        # defines options for drop down boxes

        # Labels for Conference booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

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
                                                bg="#70ABAF")

        # Entry boxes, drop downs and date picker for conference form being placed using a grid layout
        self.EntCompanyName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntNoOfDays.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # checkbox
        self.chxProjectorRequired.grid(row=9, column=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the conference form
        self.btnUpdateBooking.config(command=lambda: self.validation(booking))  # calls update ,destroy and message box

        self.populate_form_conference(self.booking)

        self.display_date.trace('w', lambda name, index, mode: self.conference_room_check())
        self.number_of_days.trace('w', lambda name, index, mode: self.conference_room_check())

    # functions
    def conference_room_check(self):
        """ensures room cannot be double booked"""
        if not self.number_of_days.get() or not self.display_date.get():
            self.om_room_val.set("Pick a date and duration first")
            self.OpmEventRoomNumber.config(state="disabled")
            return

        self.OpmEventRoomNumber.config(state="normal")

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")

        rooms_free = dbHelper.rooms_in_use_update("conferenceTable", self.display_date.get(), id=self.booking.ID,
                                                  number_of_days=int(self.number_of_days.get()))
        if len(rooms_free) < 1:
            self.om_room_val.set("No Rooms Free")
            return
        for value in rooms_free:
            self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    def populate_form_conference(self, booking):
        """populates form with booking info from selected booking"""
        self.EntCompanyName.insert(0, booking.companyName)
        self.EntNoOfDays.insert(0, booking.noOfDays)

        value = booking.projectorRequired

        if value == "Yes":
            self.chxProjectorRequired.select()
        elif value == "No":
            self.chxProjectorRequired.deselect()

# validation
    def validation(self, booking):
        """checks validation is passed and calls a dialog box if it fails"""
        val_passed = True

        if Validation.string_empty(self.save_list()):
            val_passed = False
            return messagebox.showinfo("Booking Failed",
                                       "All fields are required to be filled in.", parent=self.master)

        elif dbHelper.con_date_conflict_update("conferenceTable", self.CalDateOfEvent.get(), self.EntNoOfDays.get(),
                                               self.eventRoomNo, booking.ID):
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
            Events.Conference.update_conference(self.EntNumberOfGuest.get(),
                                                self.EntNameOfContact.get(),
                                                self.EntAddress.get(),
                                                self.EntContactNumber.get(), self.om_room_val.get(),
                                                self.display_date.get(), booking.dateOfBooking,
                                                self.EntCompanyName.get(),
                                                self.EntNoOfDays.get(),
                                                self.CheckVar1.get(), booking.ID)

            DialogBoxes.updated(self, master=self.master, view_booking=self.view_booking_self)
            self.master.destroy()

    def save_list(self):
        """saves entries to a list that is used for validation"""
        validationTestList = [self.EntNumberOfGuest.get(), self.EntNameOfContact.get(), self.EntAddress.get(),
                              self.EntContactNumber.get(), self.om_room_val.get(), self.display_date.get(),
                              self.EntCompanyName.get(), self.EntNoOfDays.get()]
        return validationTestList
