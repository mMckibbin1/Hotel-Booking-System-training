"""module contains the base class used to create the UI for the update forms used in the program"""

import datetime
from tkinter import *
from tkinter import messagebox
import Validation
from Events import Wedding, Party, Conference
from addtionalWidgets import CalendarWidget
from Database import dbHelper
from Gui import DialogBoxes


class BaseEditEvent:
    """setting default values for eventRoom and BandName as empty strings"""
    eventRoomNo = ''

    def __init__(self, master, booking):
        """Creation of wedding form set title, size ect..."""
        self.master = master
        self.master.title("Hotel Booking System - Base edit form")
        self.master.resizable(0, 0)
        self.master.config(background="#70ABAF")

        # button hover colour - close update
        def on_enter_close_update():
            """hover colour on enter"""
            self.btnCloseForm['background'] = "aquamarine4"

        def on_leave_close_update():
            """hover colour on leave"""
            self.btnCloseForm['background'] = "medium aquamarine"

        # button hover colour - close update
        def on_enter_update():
            """hover colour on enter"""
            self.btnUpdateBooking['background'] = "aquamarine4"

        def on_leave_update():
            """hover colour on leave"""
            self.btnUpdateBooking['background'] = "medium aquamarine"

        # Labels for Wedding booking form
        self.lblSubheading = Label(master, font=("arial", 20, "bold", "underline"), bg="#70ABAF")
        self.lblSubheading.grid(row=0, pady=(35, 25), padx=(10, 10), columnspan=4)

        self.lblNoOfGuest = Label(master, text="Number of guest", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoOfGuest.grid(row=1, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNameOfContact = Label(master, text="Name of contact", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNameOfContact.grid(row=2, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblAddress = Label(master, text="Address", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblAddress.grid(row=3, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblContactNumber = Label(master, text="Contact number", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblContactNumber.grid(row=4, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblEventRoomNo = Label(master, text="Event Room Number", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblEventRoomNo.grid(row=6, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblDateOfEvent = Label(master, text="Date of event", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblDateOfEvent.grid(row=5, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes, drop downs and date picker for edit form
        self.EntNumberOfGuest = Entry(master, font=("arial", 10), width=50)
        # Validation
        self.Guests_VCMD = (self.EntNumberOfGuest.register(lambda p: Validation.max_size_200(p, master)))
        self.EntNumberOfGuest.config(validate='key', validatecommand=(self.Guests_VCMD, '%P'))

        self.EntNameOfContact = Entry(master, font=("arial", 10), width=50)
        # Validation
        self.Name_VCMD = (self.EntNameOfContact.register(lambda p: Validation.max_character_length_50(p, master)))
        self.EntNameOfContact.config(validate='key', validatecommand=(self.Name_VCMD, '%P'))

        self.EntAddress = Entry(master, font=("arial", 10), width=50)
        self.Address_VCMD = (self.EntAddress.register(lambda p: Validation.max_character_length_150(p, master)))
        self.EntAddress.config(validate='key', validatecommand=(self.Address_VCMD, '%P'))

        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        self.om_room_val = StringVar()
        self.om_room_val.set("Please select a date first")
        self.OpmEventRoomNumber = OptionMenu(master, self.om_room_val, ())

        self.display_date = StringVar()
        self.CalDateOfEvent = Entry(master, font=("arial", 10), width=50,
                                    textvariable=self.display_date, state="readonly")
        self.CalDateOfEvent.bind("<Button-1>", lambda event: self.popup(master))
        self.data = {}

        # Entry boxes, drop downs and date picker for edit form being placed using grid layout
        self.EntNumberOfGuest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntNameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.CalDateOfEvent.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the base edit form
        self.btnUpdateBooking = Button(master, text="Update Booking", bg="medium aquamarine",
                                       font=("arial", 11, "bold"), width=30, height=3)
        self.btnUpdateBooking.bind("<Enter>", lambda e: on_enter_update())
        self.btnUpdateBooking.bind("<Leave>", lambda e: on_leave_update())
        self.btnCloseForm = Button(master, text="Cancel", bg="medium aquamarine", font=("arial", 11, "bold"), width=30,
                                   height=3, command=lambda: [DialogBoxes.not_saved(master),
                                                              master.destroy()])  # calls destroy and message box
        self.btnCloseForm.bind("<Enter>", lambda e: on_enter_close_update())
        self.btnCloseForm.bind("<Leave>", lambda e: on_leave_close_update())

        # Buttons for Add and Cancel on the base edit form being placed using grid layout
        self.btnUpdateBooking.grid(row=10, column=1, columnspan=1,  pady=(50, 50), padx=(75, 25), sticky="ew")
        self.btnCloseForm.grid(row=10, column=3, columnspan=2,  pady=(50, 50), padx=(75, 25), sticky="ew")

        self.populate_form(booking)

        # code to per-populate event room drop down when form loads
        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set(booking.eventRoomNo)
        if type(booking) == Wedding.Wedding:
            event_type = "weddingTable"
            for value in dbHelper.rooms_in_use_update(event_type=event_type, id=booking.ID,
                                                      date=self.display_date.get()):
                self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))
        elif type(booking) == Party.Party:
            event_type = "partyTable"
            for value in dbHelper.rooms_in_use_update(event_type=event_type, id=booking.ID,
                                                      date=self.display_date.get()):
                self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))
        elif type(booking) == Conference.Conference:
            event_type = "conferenceTable"
            for value in dbHelper.rooms_in_use_update(event_type=event_type, id=booking.ID,
                                                      date=self.display_date.get(), number_of_days=booking.noOfDays):
                self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    def popup(self, master):
        """function to display calendar widget for date of event"""
        child = Toplevel()
        CalendarWidget.Calendar(child, self.data)
        master.grab_release()
        child.grab_set()
        child.wait_window()
        child.grab_release()
        master.grab_set()
        self.get_selected_date(master)

    def get_selected_date(self, master):
        """function to get the selected date from calendar widget and display it as a formatted string"""
        day = self.data.get("day_selected", "date error")
        month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        date = str(year) + "-" + str(month) + "-" + str(day)

        if day == "date error":
            return

        format_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

        if format_date < datetime.datetime.now().date():
            return messagebox.showinfo("Invalid Date", "Can not pick a past date.\nPlease pick a new date.",
                                       parent=master)
        else:
            self.display_date.set(format_date)

    def populate_form(self, booking):
        """populates form with booking info for selected booking"""
        self.EntNumberOfGuest.insert(0, booking.noGuests)
        self.EntNameOfContact.insert(0, booking.nameOfContact)
        self.EntAddress.insert(0, booking.address)
        self.EntContactNumber.insert(0, booking.contactNo)
        self.display_date.set(booking.dateOfEvent)
        self.om_room_val.set(booking.eventRoomNo)
