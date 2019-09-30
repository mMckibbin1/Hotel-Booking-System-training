import datetime
from tkinter import *
from tkinter import messagebox

import Validation
from Events import Wedding, Party, Conference
from addtionalWidgets import CalendarWidget
from Database import dbHelper
from Gui import viewbooking, DialogBoxes


class BaseEditEvent:
    # setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''

    def __init__(self, master, object):
        # Creation of wedding form set title, size ect..
        self.master = master
        self.master.title("Hotel Booking System - Base edit form")
        self.master.resizable(0, 0)
        self.master.config(background="#70ABAF")

        # button hover colour - close update
        def on_enterCloseUpdate(e):
            self.btnCloseForm['background'] = "aquamarine4"

        def on_leaveCloseUpdate(e):
            self.btnCloseForm['background'] = "medium aquamarine"

        # button hover colour - close update
        def on_enterUpdate(e):
            self.btnUpdateBooking['background'] = "aquamarine4"

        def on_leaveUpdate(e):
            self.btnUpdateBooking['background'] = "medium aquamarine"

        # Labels for Wedding booking form
        self.lblSubheading = Label(master, font=("arial", 20, "bold", "underline"), bg="#70ABAF")
        self.lblSubheading.grid(row=0, pady=(35, 25), padx=(10, 10), columnspan=4)

        self.lblNoofGuest = Label(master, text="Number of guest", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoofGuest.grid(row=1, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNameofContact = Label(master, text="Name of contact", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNameofContact.grid(row=2, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblAddress = Label(master, text="Address", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblAddress.grid(row=3, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblContactNumber = Label(master, text="Contact number", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblContactNumber.grid(row=4, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblEventRoomNo = Label(master, text="Event Room Number", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblEventRoomNo.grid(row=6, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblDateofEvent = Label(master, text="Date of event", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblDateofEvent.grid(row=5, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes, dropdowns and datepicker for edit form
        self.EntnumberOfguest = Entry(master, font=("arial", 10), width=50)
        self.GuestsVcmd = (self.EntnumberOfguest.register(lambda P: Validation.max_size_200(P,master)))  # Validation
        self.EntnumberOfguest.config(validate='key', validatecommand=(self.GuestsVcmd, '%P'))

        self.EntnameOfContact = Entry(master, font=("arial", 10), width=50)
        self.NameVcmd = (self.EntnameOfContact.register(lambda P:Validation.max_character_length_50(P,master)))  # Validation
        self.EntnameOfContact.config(validate='key', validatecommand=(self.NameVcmd, '%P'))

        self.EntAddress = Entry(master, font=("arial", 10), width=50)
        self.addressVcmd = (self.EntAddress.register(lambda P: Validation.max_character_length_150(P,master)))
        self.EntAddress.config(validate='key', validatecommand=(self.addressVcmd, '%P'))

        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        self.ContactVcmd = (self.EntContactNumber.register(Validation.digits_only))  # Validation
        self.EntContactNumber.config(validate='all', validatecommand=(self.ContactVcmd, '%P'))

        self.om_room_val = StringVar()
        self.om_room_val.set("Please select a date first")
        self.OpmEventRoomNumber = OptionMenu(master, self.om_room_val, ())

        self.display_date = StringVar()
        self.CalDateOfEvent = Entry(master, font=("arial", 10), width=50, textvariable=self.display_date, state="readonly")
        self.CalDateOfEvent.bind("<Button-1>", lambda event: self.popup(event, master))
        self.data = {}

        # Entry boxes, dropdowns and datepicker for edit form being placed using grid layout
        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.CalDateOfEvent.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the base edit form
        self.btnUpdateBooking = Button(master, text="Update Booking", bg="medium aquamarine",font=("arial", 11, "bold"), width=30, height=3)
        self.btnUpdateBooking.bind("<Enter>", on_enterUpdate)
        self.btnUpdateBooking.bind("<Leave>", on_leaveUpdate)
        self.btnCloseForm = Button(master, text="Cancel", bg="medium aquamarine",font=("arial", 11, "bold"), width=30,
                                   height=3, command=lambda: [DialogBoxes.not_saved(master),
                                                              master.destroy()])  # calls destroy and message box
        self.btnCloseForm.bind("<Enter>", on_enterCloseUpdate)
        self.btnCloseForm.bind("<Leave>", on_leaveCloseUpdate)

        # Buttons for Add and Cancel on the base edit form being placed using grid layout
        self.btnUpdateBooking.grid(row=10, column=1, columnspan=1,  pady=(50, 50), padx=(75, 25), sticky="ew")
        self.btnCloseForm.grid(row=10, column=3, columnspan=2,  pady=(50, 50), padx=(75, 25), sticky="ew")

        self.populateform(object)

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set(object.eventRoomNo)
        if type(object) == Wedding.Wedding:
            event_type = "weddingTable"
            for value in dbHelper.rooms_in_use_update(event_type=event_type, id=object.ID,
                                                      date=self.display_date.get()):
                self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))
        elif type(object) == Party.Party:
            event_type = "partyTable"
            for value in dbHelper.rooms_in_use_update(event_type=event_type, id=object.ID,
                                                      date=self.display_date.get()):
                self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))
        elif type(object) == Conference.Conference:
            event_type = "conferenceTable"
            for value in dbHelper.rooms_in_use_update(event_type=event_type, id=object.ID,
                                                      date=self.display_date.get(), number_of_days=object.noOfDays):
                self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))


    # function to display calander widget for date of event
    def popup(self, event, master):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        master.grab_release()
        child.grab_set()
        child.wait_window()
        child.grab_release()
        master.grab_set()
        self.Get_selected_date(master)

    # function to get the selected date from calander widget and display it as a formatted string
    def Get_selected_date(self, master):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(year) + "-" + str(Month) + "-" + str(Day)

        if Day == "date error":
            return

        FormtDate = datetime.datetime.strptime(Date, "%Y-%m-%d").date()

        if FormtDate < datetime.datetime.now().date():
            return messagebox.showinfo("Invalid Date", "Can not pick a past date.\nPlease pick a new date.",
                                       parent=master)
        else:
            self.display_date.set(FormtDate)

    def populateform(self, object):
        self.EntnumberOfguest.insert(0, object.noGuests)
        self.EntnameOfContact.insert(0, object.nameOfContact)
        self.EntAddress.insert(0, object.address)
        self.EntContactNumber.insert(0, object.contactNo)
        self.display_date.set(object.dateOfEvent)
        self.om_room_val.set(object.eventRoomNo)
