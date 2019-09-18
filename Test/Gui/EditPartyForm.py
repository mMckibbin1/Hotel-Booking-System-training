import Gui.BaseEditForm
from tkinter import *
import Events.Party

class EditParty(Gui.BaseEditForm.BaseEditEvent):
    def __init__(self, master, object):
        RoomOption = ['D', 'E', 'F', 'G']
        super().__init__(master,RoomOption, object)
        # Creation of wedding form set title, size ect..
        master.title("Party Edit")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        # defines options for dropdown boxes

        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        DefaultBandName = StringVar(master)
        DefaultBandName.set(object.bandName)  # default value from db for selected entry

        # Labels for Party booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblBandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="powder blue")
        self.lblBandName.grid(row=7, columnspan=2,pady=(25, 0), padx=(10, 10))

        # Entry boxes, dropdowns and datepicker for party form
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)

        # Entry boxes, dropdowns and datepicker for party form being placed using grid layout
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        # Buttons for Add and Cancel on the party form
        self.btnUpdateBooking.config(command=lambda: [Events.Party.updateParty(self.EntnumberOfguest.get(),
                                                                     self.EntnameOfContact.get(),
                                                                     self.EntAddress.get(),
                                                                     self.EntContactNumber.get(),self.eventRoomNo,
                                                                     self.CalDateOfEvent.get(), object.dateOfBooking,
                                                                     self.bandName, object.ID), master.destroy()])

    # function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value

    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value

