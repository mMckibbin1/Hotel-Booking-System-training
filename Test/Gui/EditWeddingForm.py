from tkinter import *
from tkinter import messagebox

import Events.Wedding
import Gui.BaseEditForm
import Validation
from Database import dbHelper
from Gui import BaseEditForm, DialogBoxes


class EditWedding(Gui.BaseEditForm.BaseEditEvent):
    #setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''
    bandName = ''

    def __init__(self, master, booking, viewbookingself):
        RoomOption = ['H', 'I']
        super().__init__(master, RoomOption, booking)
        #Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Update Selected Wedding")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        self.viewbookingself = viewbookingself

        #defines options for dropdown boxes
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]
        self.DefaultBandName = StringVar(master)
        self.DefaultBandName.set(booking.bandName)  # default value from db for selected item


        #Labels for Wedding booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblbandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblbandName.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoofRoomsRes = Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoofRoomsRes.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        #Entry boxes, dropdowns and datepicker for wedding form
        self.OpmBandName = OptionMenu(master, self.DefaultBandName, *BandNames, command=self.getBandName)
        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)

        # Entry boxes, dropdowns and datepicker for wedding form being placed using grid layout
        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.BedsVcmd = (self.EntBedroomReserved.register(Validation.callback))
        self.EntBedroomReserved.config(validate='all', validatecommand=(self.BedsVcmd, '%P'))

        #Buttons for Add and Cancel on the wedding for
        self.btnUpdateBooking.config(command=lambda: self.validation(booking)) # calls update ,destroy and message box

        #Buttons for Add and Cancel on the wedding form being placed using grid layout
        self.populateform_wedding(booking)

    #function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value

    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value

    def populateform_wedding(self, booking):

        self.EntBedroomReserved.insert(0, booking.noBedroomsReserved)

# validation
    def validation(self, booking):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.")

        elif dbHelper.date_conflict_update("weddingTable", self.CalDateOfEvent.get(), self.eventRoomNo, booking.ID):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.')
        elif Validation.min_number([self.EntnumberOfguest.get(), self.EntBedroomReserved.get()]):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have entered more than one guest and room.")

        if valpassed:
            Events.Wedding.updateWedding(self.EntnumberOfguest.get(),
                                         self.EntnameOfContact.get(),
                                         self.EntAddress.get(),
                                         self.EntContactNumber.get(),
                                         self.DefaultRoomNo.get(),
                                         self.CalDateOfEvent.get(), booking.dateOfBooking,
                                         self.DefaultBandName.get(),
                                         self.EntBedroomReserved.get(),
                                         booking.ID)
            DialogBoxes.updated(self, master=self.master, view_booking=self.viewbookingself)
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
        self.validationTestList.append(self.EntBedroomReserved.get())
        return self.validationTestList