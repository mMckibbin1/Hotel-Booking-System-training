from tkinter import *
import Events.Wedding
import Gui.BaseEditForm
from Gui import BaseEditForm


class EditWedding(Gui.BaseEditForm.BaseEditEvent):
    #setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''
    bandName = ''

    def __init__(self, master, booking):
        RoomOption = ['H', 'I']
        super().__init__(master, RoomOption, booking)
        #Creation of wedding form set title, size ect..
        master.title("Wedding Edit")
        master.resizable(0, 0)
        master.config(background="powder blue")

        #defines options for dropdown boxes
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]
        DefaultBandName = StringVar(master)
        DefaultBandName.set(booking.bandName)  # default value from db for selected item


        #Labels for Wedding booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblbandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="powder blue")
        self.lblbandName.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoofRoomsRes = Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"), bg="powder blue")
        self.lblNoofRoomsRes.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        #Entry boxes, dropdowns and datepicker for wedding form
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)
        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)

        # Entry boxes, dropdowns and datepicker for wedding form being placed using grid layout
        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        #Buttons for Add and Cancel on the wedding for
        self.btnUpdateBooking.config(command=lambda: [Events.Wedding.updateWedding(self.EntnumberOfguest.get(),
                                                                       self.EntnameOfContact.get(),
                                                                       self.EntAddress.get(),
                                                                       self.EntContactNumber.get(),
                                                                       self.eventRoomNo,
                                                                       self.CalDateOfEvent.get(),booking.dateOfBooking,
                                                                       self.bandName,
                                                                       self.EntBedroomReserved.get(), booking.ID), master.destroy()])

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