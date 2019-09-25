from tkinter import messagebox

import Gui.BaseEditForm
from tkinter import *
import Events.Party
import Validation
from Database import dbHelper
from Gui import DialogBoxes


class EditParty(Gui.BaseEditForm.BaseEditEvent):
    def __init__(self, master, object, viewbookingself):
        RoomOption = ['D', 'E', 'F', 'G']
        super().__init__(master,RoomOption, object)
        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Update Selected Party")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        self.viewbookingself = viewbookingself
        # defines options for dropdown boxes

        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        self.DefaultBandName = StringVar(master)
        self.DefaultBandName.set(object.bandName)  # default value from db for selected entry

        # Labels for Party booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblBandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblBandName.grid(row=7, columnspan=2,pady=(25, 0), padx=(10, 10))

        # Entry boxes, dropdowns and datepicker for party form
        self.OpmBandName = OptionMenu(master, self.DefaultBandName, *BandNames, command=self.getBandName)

        # Entry boxes, dropdowns and datepicker for party form being placed using grid layout
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        # Buttons for Add and Cancel on the party form
        self.btnUpdateBooking.config(command=lambda: self.validation(object))  # calls update ,destroy and message box

    def validation(self,booking):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.", parent=self.master)
        elif dbHelper.date_conflict_update("partyTable", self.CalDateOfEvent.get(), self.eventRoomNo, booking.ID ):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntnumberOfguest.get()]):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have more than one guest.", parent=self.master)

        if valpassed:
            Events.Party.updateParty(self.EntnumberOfguest.get(),
                                      self.EntnameOfContact.get(),
                                      self.EntAddress.get(),
                                      self.EntContactNumber.get(), self.DefaultRoomNo.get(),
                                      self.CalDateOfEvent.get(), booking.dateOfBooking,
                                      self.DefaultBandName.get(), booking.ID)

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
        self.validationTestList.append(self.DefaultBandName.get())
        return self.validationTestList

    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value

