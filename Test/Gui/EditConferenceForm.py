from tkinter import *
from tkinter import messagebox

import Events.Conference
import Gui.BaseEditForm
import Validation
from Database import dbHelper
from Gui import DialogBoxes


class EditConference(Gui.BaseEditForm.BaseEditEvent):

    def __init__(self, master, booking, viewbookingself):
        RoomOption = ['A', 'B', 'C']

        super().__init__(master, RoomOption, booking)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Update Selected Conference")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        self.viewbookingself = viewbookingself

        def ch_box_sel():
            print(self.CheckVar1.get())

        # defines options for dropdown boxes

        # Labels for Conference booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblCompanyname = Label(master, text="Company Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblCompanyname.grid(row=7,columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblNoofDays = Label(master, text="Number of Days", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoofDays.grid(row=8,columnspan=2, pady=(25, 0),padx=(10, 10))

        self.lblProjectorReq = Label(master, text="Projector Required", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblProjectorReq.grid(row=9, columnspan=2,pady=(25,0),padx=(10,10))


        # Entry boxes, dropdowns and datepicker for conference form
        self.EntCompanyName = Entry(master, font=("arial", 10), width=50)

        self.EntNoOfDays = Entry(master, font=("arial", 10), width=50)
        self.DaysVcmd = (self.EntNoOfDays.register(Validation.callback))
        self.EntNoOfDays.config(validate='all', validatecommand=(self.DaysVcmd, '%P'))

        #checkbox now works :)
        self.CheckVar1 = IntVar()
        self.chxProjectorRequired = Checkbutton(master, text='', variable=self.CheckVar1, onvalue=True, offvalue=False, bg="#70ABAF", command=ch_box_sel)

        # Entry boxes, dropdowns and datepicker for conference form being placed using a grid layout
        self.EntCompanyName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntNoOfDays.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))


        #checkbox.....
        self.chxProjectorRequired.grid(row=9, column=2, pady=(25, 0), padx=(0, 25))
        print(booking.dateOfBooking)
        # Buttons for Add and Cancel on the conference form
        self.btnUpdateBooking.config(command=lambda: self.validation(booking)) # calls update ,destroy and message box


        self.populateform_conference(booking)
        # print(booking.ID)

    def populateform_conference(self, booking):
        self.EntCompanyName.insert(0, booking.companyName)
        self.EntNoOfDays.insert(0, booking.noOfDays)

        value = booking.projectorRequired

        if value == 1:
            self.chxProjectorRequired.select()
        elif value == 0:
            self.chxProjectorRequired.deselect()


# validation
    def validation(self, booking):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed",
                                       "All fields are required to be filled in.", parent=self.master)
        elif dbHelper.con_date_conflict_update("conferenceTable", self.CalDateOfEvent.get(), self.EntNoOfDays.get(), self.eventRoomNo, booking.Id):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntnumberOfguest.get()]):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have more than one guest.", parent=self.master)


        if valpassed:
            Events.Conference.updateConference(self.EntnumberOfguest.get(),
                                               self.EntnameOfContact.get(),
                                               self.EntAddress.get(),
                                               self.EntContactNumber.get(), self.DefaultRoomNo.get(),
                                               self.CalDateOfEvent.get(), booking.dateOfBooking,
                                               self.EntCompanyName.get(),
                                               self.EntNoOfDays.get(),
                                               self.CheckVar1.get(), booking.ID)

            DialogBoxes.updated(self, master=self.master)
            self.master.destroy()


    def savelist(self):
        self.validationTestList = []
        self.validationTestList.append(self.EntnumberOfguest.get())
        self.validationTestList.append(self.EntnameOfContact.get())
        self.validationTestList.append(self.EntAddress.get())
        self.validationTestList.append(self.EntContactNumber.get())
        self.validationTestList.append(self.DefaultRoomNo.get())
        self.validationTestList.append(self.CalDateOfEvent.get())
        self.validationTestList.append(self.EntCompanyName.get())
        self.validationTestList.append(self.EntNoOfDays.get())
        return self.validationTestList

