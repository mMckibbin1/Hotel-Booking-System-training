from tkinter import *
from addtionalWidgets import CalendarWidget
from Database import dbHelper
from Gui import viewbooking, DialogBoxes


class BaseEditEvent:
    #setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''
    def __init__(self, master, Rooms, object):
        #Creation of wedding form set title, size ect..
        self.master = master
        self.master.title("Hotel Booking System - Base edit form")
        self.master.resizable(0, 0)
        self.master.config(background="#70ABAF")

        #defines options for dropdown boxes

        self.DefaultRoomNo = StringVar(master)
        self.DefaultRoomNo.set(object.eventRoomNo)  # default value set as what is stored already


        #Labels for Wedding booking form
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
        self.lblEventRoomNo.grid(row=5, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblDateofEvent = Label(master, text="Date of event", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblDateofEvent.grid(row=6, columnspan=2, pady=(25, 0), padx=(10, 10))

        #Entry boxes, dropdowns and datepicker for edit form
        self.EntnumberOfguest = Entry(master, font=("arial", 10), width=50)
        self.EntnameOfContact = Entry(master, font=("arial", 10), width=50)
        self.EntAddress = Entry(master, font=("arial", 10), width=50)
        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        self.OpmEventRoomNumber = OptionMenu(master, self.DefaultRoomNo, *Rooms, command=self.getRoomnumber)
        self.CalDateOfEvent = Entry(master, font=("arial", 10), width=50)
        self.CalDateOfEvent.bind("<Button-1>", lambda event: self.popup(event, master))
        self.data = {}

        # Entry boxes, dropdowns and datepicker for edit form being placed using grid layout
        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.CalDateOfEvent.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        #Buttons for Add and Cancel on the base edit form
        self.btnUpdateBooking = Button(master, text="Update Booking", bg="medium aquamarine",font=("arial", 11, "bold"), width=30, height=3)
        self.btnCloseForm = Button(master, text="Cancel", bg="medium aquamarine",font=("arial", 11, "bold"), width=30, height=3, command=lambda: [master.destroy(), DialogBoxes.not_saved(self)]) # calls destroy and message box

        ##Buttons for Add and Cancel on the base edit form being placed using grid layout
        self.btnUpdateBooking.grid(row=10, column=1, columnspan=1,  pady=(50, 50), padx=(75, 25), sticky="ew")
        self.btnCloseForm.grid(row=10, column=3, columnspan=2,  pady=(50, 50), padx=(75, 25), sticky="ew")

        self.populateform(object)

    #function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value

    # function to display calander widget for date of event
    def popup(self, event, master):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        master.grab_release()
        child.grab_set()
        child.wait_window()
        child.grab_release()
        master.grab_set()
        self.Get_selected_date()

    #function to get the selected date from calander widget and display it as a formatted string
    def Get_selected_date(self):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(Day) + "/" + str(Month) + "/" + str(year)
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], Date)

    def populateform(self, object):
        self.EntnumberOfguest.insert(0, object.noGuests)
        self.EntnameOfContact.insert(0, object.nameOfContact)
        self.EntAddress.insert(0, object.address)
        self.EntContactNumber.insert(0, object.contactNo)
        self.CalDateOfEvent.insert(0, object.dateOfEvent)

