import datetime
from tkinter import *

from Gui import DialogBoxes
from addtionalWidgets import CalendarWidget
import Validation
import caltest


class BaseEvent:
    # setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''


    def __init__(self, master, Rooms,):
        # Creation of wedding form set title, size ect..
        self.master = master
        self.master.title("Hotel Booking System - Base booking form")
        self.master.resizable(0, 0)
        self.master.config(background="#70ABAF")


        # defines options for dropdown boxes
        DefaultRoomNo = StringVar(master)
        DefaultRoomNo.set("Please Select A Room")  # default value

        # defines options for dropdown boxes
        DefaultRoomNo = StringVar(master)
        DefaultRoomNo.set("Please Select A Room")  # default value

        # Labels for Wedding booking form

        self.lblSubheading = Label(master,text="Please fill in the details for the wedding event you are booking",
                                   font=("arial", 20,"bold", "underline"), bg="#70ABAF")
        self.lblSubheading.grid(row=0, pady=(35,25), padx=(10, 10), columnspan=4)

        self.lblNoofGuest = Label(master, text="Number of guest", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoofGuest.grid(row=1, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNameofContact = Label(master, text="Name of contact", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNameofContact.grid(row=2,columnspan=2,pady=( 25, 0), padx=(10, 10))

        self.lblAddress = Label(master, text="Address", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblAddress.grid(row=3, columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblContactNumber = Label(master, text="Contact number", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblContactNumber.grid(row=4, columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblEventRoomNo = Label(master, text="Event Room Number", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblEventRoomNo.grid(row=5,columnspan=2,pady=(25, 0),padx=(10,10))

        self.lblDateofEvent = Label(master, text="Date of event", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblDateofEvent.grid(row=6,columnspan=2,pady=(25, 0),padx=(10, 10))


        # Entry boxes, dropdowns and datepicker for wedding form
        self.EntnumberOfguest = Entry(master, font=("arial", 10), width=50)
        self.GuestsVcmd = (self.EntnumberOfguest.register(Validation.callback))  # Validation
        self.EntnumberOfguest.config(validate='all', validatecommand=(self.GuestsVcmd, '%P'))

        self.EntnameOfContact = Entry(master, font=("arial", 10), width=50)
        self.NameVcmd = (self.EntnameOfContact.register(Validation.charOnly))  # Validation
        self.EntnameOfContact.config(validate='all', validatecommand=(self.NameVcmd, '%P'))

        self.EntAddress = Entry(master, font=("arial", 10), width=50)

        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        self.ContactVcmd = (self.EntContactNumber.register(Validation.callback))  # Validation
        self.EntContactNumber.config(validate='all', validatecommand=(self.ContactVcmd, '%P'))

        self.OpmEventRoomNumber = OptionMenu(master, DefaultRoomNo, *Rooms, command=self.getRoomnumber)

        self.CalDateOfEvent = Entry(master, font=("arial", 10), width=50)
        self.CalDateOfEvent.bind("<Button-1>", lambda event: self.popup(event, master))
        self.data = {}



        # Entry boxes, dropdowns and datepicker for wedding form being placed using grid layout
        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.CalDateOfEvent.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the wedding form
        self.btnCloseForm = Button(master, text="Cancel",bg="medium aquamarine",font=("arial", 11, "bold"), width=30,height=3, command=lambda: [master.destroy(), DialogBoxes.not_saved(self)]) # calls destroy and message box
        self.btnAddBooking = Button(master, text="Add Booking", bg="medium aquamarine",font=("arial", 11, "bold"), width=30,height=3)
        # Buttons for Add and Cancel on the wedding form being placed using grid layout
        self.btnAddBooking.grid(row=10, column=1, columnspan=1, pady=(50, 50), padx=(75, 25), sticky="ew")
        self.btnCloseForm.grid(row=10, column=3, columnspan=2, pady=(50, 50), padx=(75, 25), sticky="ew")


    # function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value

    # function to display calendar widget for date of event
    def popup(self, event, master):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        master.grab_release()
        child.grab_set()
        child.wait_window()
        child.grab_release()
        master.grab_set()
        self.Get_selected_date()

    # function to get the selected date from calendar widget and display it as a formatted string
    def Get_selected_date(self):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(year) + "-" + str(Month) + "-" + str(Day)

        FormtDate = datetime.datetime.strptime(Date, "%Y-%m-%d").date()
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], str(FormtDate))