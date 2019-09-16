import Gui.BaseCreateForm
from tkinter import *
import Events.Party

class bookParty(Gui.BaseCreateForm.BaseEvent):
    def __init__(self, master):
        RoomOption = ['D', 'E', 'F', 'G']
        super(bookParty, self).__init__(master,RoomOption)
        # Creation of wedding form set title, size ect..
        master.title("Party bookings")
        master.resizable(0, 0)
        master.config(background="powder blue")

        # defines options for dropdown boxes

        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        DefaultBandName = StringVar(master)
        DefaultBandName.set("Please Select a Band")  # default value

        # Labels for Party booking form
        self.lblSubheading.config(text="Please fill in the details for the Party event you are booking")

        self.lblBandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="powder blue")
        self.lblBandName.grid(row=7, columnspan=2,pady=(25, 0), padx=(10, 10))

        # Entry boxes, dropdowns and datepicker for party form
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)

        # Entry boxes, dropdowns and datepicker for party form being placed using grid layout
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        # Buttons for Add and Cancel on the party form
        self.btnAddBooking.config(command=lambda: [Events.Party.createParty(self.EntnumberOfguest.get(),
                                                                     self.EntnameOfContact.get(),
                                                                     self.EntAddress.get(),
                                                                     self.EntContactNumber.get(),
                                                                     self.eventRoomNo,
                                                                     self.CalDateOfEvent.get(),
                                                                     self.bandName), master.destroy()])

    # function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value

    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value