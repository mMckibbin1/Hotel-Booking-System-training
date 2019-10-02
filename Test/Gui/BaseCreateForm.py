import datetime
from tkinter import *
from tkinter import messagebox
from Gui import DialogBoxes
from addtionalWidgets import CalendarWidget
import Validation


class BaseEvent:
    # setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''

    def __init__(self, master):
        # Creation of wedding form set title, size ect..
        self.master = master
        self.master.title("Hotel Booking System - Base booking form")
        self.master.resizable(0, 0)
        self.master.config(background="#70ABAF")

        # button hover colour - close
        def on_enter_close(e):
            self.btnCloseForm['background'] = "aquamarine4"

        def on_leave_close(e):
            self.btnCloseForm['background'] = "medium aquamarine"

        # button hover colour - add booking
        def on_enter_add_booking(e):
            self.btnAddBooking['background'] = "aquamarine4"

        def on_leave_add_booking(e):
            self.btnAddBooking['background'] = "medium aquamarine"

        # Labels for Wedding booking form

        self.lblSubheading = Label(master,text="Please fill in the details for the wedding event you are booking",
                                   font=("arial", 20, "bold", "underline"), bg="#70ABAF")
        self.lblSubheading.grid(row=0, pady=(35, 25), padx=(10, 10), columnspan=4)

        self.lblNoOfGuest = Label(master, text="Number of guest", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoOfGuest.grid(row=1, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNameOfContact = Label(master, text="Name of contact", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNameOfContact.grid(row=2, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblAddress = Label(master, text="Address", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblAddress.grid(row=3, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblContactNumber = Label(master, text="Contact number", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblContactNumber.grid(row=4, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblDateOfEvent = Label(master, text="Date of event", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblDateOfEvent.grid(row=5, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblEventRoomNo = Label(master, text="Event Room Number", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblEventRoomNo.grid(row=6, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes, drop downs and date picker for wedding form
        self.EntNumberOfGuest = Entry(master, font=("arial", 10), width=50)
        # Validation
        self.Guests_VCMD = (self.EntNumberOfGuest.register(lambda p: Validation.max_size_200(p, master)))
        self.EntNumberOfGuest.config(validate='key', validatecommand=(self.Guests_VCMD, '%P'))

        self.EntNameOfContact = Entry(master, font=("arial", 10), width=50)
        # Validation
        self.Name_VCMD = (self.EntNameOfContact.register(lambda p: Validation.max_character_length_50(p, master)))
        self.EntNameOfContact.config(validate='key', validatecommand=(self.Name_VCMD, '%P'))

        self.EntAddress = Entry(master, font=("arial", 10), width=50)
        # Validation
        self.Add_VCMD = (self.EntAddress.register(lambda p: Validation.max_character_length_150(p, master)))
        self.EntAddress.config(validate='key', validatecommand=(self.Add_VCMD, '%P'))

        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        # Validation
        self.Contact_VCMD = (self.EntContactNumber.register
                             (lambda p: Validation.contact_number_val(p, self.EntContactNumber, master)))
        self.EntContactNumber.config(validate='focusout', validatecommand=(self.Contact_VCMD, '%P'))

        self.display_date = StringVar()
        self.CalDateOfEvent = Entry(master, font=("arial", 10), width=50,
                                    textvariable=self.display_date, state="readonly")
        self.CalDateOfEvent.bind("<Button-1>", lambda event: self.popup(event, master))
        self.data = {}

        self.om_room_val = StringVar()
        self.om_room_val.set("Please Select a date first")
        self.OpmEventRoomNumber = OptionMenu(master, self.om_room_val, ())

        # Entry boxes, drop downs and date picker for wedding form being placed using grid layout
        self.EntNumberOfGuest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntNameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.CalDateOfEvent.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        # Buttons for Add and Cancel on the wedding form
        self.btnCloseForm = Button(master, text="Cancel", bg="medium aquamarine", font=("arial", 11, "bold"),
                                   width=30, height=3,
                                   # calls destroy and message box
                                   command=lambda: [DialogBoxes.not_saved(master), master.destroy()])
        self.btnCloseForm.bind("<Enter>", on_enter_close)
        self.btnCloseForm.bind("<Leave>", on_leave_close)
        self.btnAddBooking = Button(master, text="Add Booking", bg="medium aquamarine", font=("arial", 11, "bold"),
                                    width=30, height=3)
        self.btnAddBooking.bind("<Enter>", on_enter_add_booking)
        self.btnAddBooking.bind("<Leave>", on_leave_add_booking)
        # Buttons for Add and Cancel on the wedding form being placed using grid layout
        self.btnAddBooking.grid(row=10, column=1, columnspan=1, pady=(50, 50), padx=(75, 25), sticky="ew")
        self.btnCloseForm.grid(row=10, column=3, columnspan=2, pady=(50, 50), padx=(75, 25), sticky="ew")

    # function to display calendar widget for date of event
    def popup(self, event, master):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        master.grab_release()
        child.grab_set()
        child.wait_window()
        child.grab_release()
        master.grab_set()
        self.get_selected_date(master)

    # function to get the selected date from calendar widget and display it as a formatted string
    def get_selected_date(self, master):
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