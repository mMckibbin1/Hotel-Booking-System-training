from tkinter import *
import Events.Conference
import Gui.BaseCreateForm
import Validation
from Gui import DialogBoxes
from Database import dbHelper
from tkinter import messagebox
import datetime


class bookConference(Gui.BaseCreateForm.BaseEvent):
    def __init__(self, master):

        super().__init__(master)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Book a Conference")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        # method to get value of checkbutton
        def ch_box_sel():
            print(self.CheckVar1.get())

        # Labels for Conference booking form
        self.lblSubheading.config(text="Please Fill in the Details for the Conference")

        self.lblCompanyname = Label(master, text="Company Name",font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblCompanyname.grid(row=7,columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblNoofDays = Label(master, text="Number of Days",font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoofDays.grid(row=8,columnspan=2, pady=(25, 0),padx=(10, 10))

        self.lblProjectorReq = Label(master, text="Projector Required", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblProjectorReq.grid(row=9, columnspan=2,pady=(25,0),padx=(10,10))



        # Entry boxes, dropdowns and datepicker for conference form
        self.EntCompanyName = Entry(master, font=("arial", 10), width=50)

        self.number_of_days = StringVar()
        self.EntNoOfDays = Entry(master, font=("arial", 10), width=50, textvariable=self.number_of_days)
        self.DaysVcmd = (self.EntNoOfDays.register(Validation.callback))
        self.EntNoOfDays.config(validate='all', validatecommand=(self.DaysVcmd, '%S'))

        # checkbox now works :)
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
        if not self.number_of_days.get() or not self.display_date.get():
            self.om_room_val.set("Pick a date and duration first")
            self.OpmEventRoomNumber.config(state="disabled")
            return

        self.OpmEventRoomNumber.config(state="normal")

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")
        for value in dbHelper.rooms_in_use("conferenceTable", self.display_date.get(), int(self.number_of_days.get())):
            self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    # validation
    def validation(self):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed",
                                       "All fields are required to be filled in.", parent=self.master)
        elif dbHelper.con_date_conflict("conferenceTable", self.display_date.get(), self.EntNoOfDays.get(), self.om_room_val.get()):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number(self.EntnumberOfguest.get()):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have more than one guest.", parent=self.master)


        if valpassed:
            Events.Conference.createConference(
                self.EntnumberOfguest.get(),
                self.EntnameOfContact.get(),
                self.EntAddress.get(),
                self.EntContactNumber.get(),
                self.om_room_val.get(),
                self.display_date.get(),
                self.EntCompanyName.get(),
                self.EntNoOfDays.get(),
                self.CheckVar1.get())

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
        self.validationTestList.append(self.EntCompanyName.get())
        self.validationTestList.append(self.EntNoOfDays.get())
        return self.validationTestList