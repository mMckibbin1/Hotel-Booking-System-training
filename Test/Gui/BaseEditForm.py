from tkinter import *
from addtionalWidgets import CalendarWidget


class BaseEditEvent:
    #setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''
    def __init__(self, master, Rooms, object):
        #Creation of wedding form set title, size ect..
        self.master = master
        self.master.title("base edit bookings")
        self.master.resizable(0, 0)
        self.master.config(background="powder blue")

        #defines options for dropdown boxes

        DefaultRoomNo = StringVar(master)
        DefaultRoomNo.set("Please Select A Room")  # default value


        #Labels for Wedding booking form
        self.lblSubheading = Label(master, text="Please update any details that you want to change", font=("arial", 15, "bold"), bg="powder blue")
        self.lblSubheading.grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=4)

        self.lblNoofGuest = Label(master, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue")
        self.lblNoofGuest.grid(row=1, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNameofContact = Label(master, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue")
        self.lblNameofContact.grid(row=2,columnspan=2,pady=( 25, 0), padx=(10, 10))

        self.lblAddress = Label(master, text="Address", font=("arial", 10, "bold"), bg="powder blue")
        self.lblAddress.grid(row=3, columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblContactNumber = Label(master, text="Contact number", font=("arial", 10, "bold"), bg="powder blue")
        self.lblContactNumber.grid(row=4, columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblEventRoomNo = Label(master, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue")
        self.lblEventRoomNo.grid(row=5,columnspan=2,pady=(25, 0),padx=(10,10))

        self.lblDateofEvent = Label(master, text="Date of event", font=("arial", 10, "bold"), bg="powder blue")
        self.lblDateofEvent.grid(row=6,columnspan=2,pady=(25, 0),padx=(10, 10))

        #Entry boxes, dropdowns and datepicker for edit form
        self.EntnumberOfguest = Entry(master, font=("arial", 10), width=50)
        self.EntnameOfContact = Entry(master, font=("arial", 10), width=50)
        self.EntAddress = Entry(master, font=("arial", 10), width=50)
        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        self.OpmEventRoomNumber = OptionMenu(master, DefaultRoomNo, *Rooms, command=self.getRoomnumber)
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
        self.btnAddBooking = Button(master, text="Add Booking")
        self.btnCloseForm = Button(master, text="Cancel", command=master.destroy)

        ##Buttons for Add and Cancel on the base edit form being placed using grid layout
        self.btnAddBooking.grid(row=10, column=1, columnspan=1, pady=(25, 50), padx=(0, 25), sticky="ew")
        self.btnCloseForm.grid(row=10, column=3, columnspan=2, pady=(25, 50), padx=(0, 50), sticky="ew")

        self.populateform(self,object)

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
        self.EntContactNumber.insert(0, object.contactNo)
        self.EntAddress.insert(0, object.address)
        self.EntnameOfContact.insert(0, object.nameOfContact)
        self.EntnumberOfguest.insert(0, object.noGuests)
        self.CalDateOfEvent.insert(0, object.dateOfEvent)