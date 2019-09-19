import Gui.BaseCreateForm
from tkinter import *
import Events.Party
import Validation


class bookParty(Gui.BaseCreateForm.BaseEvent):
    def __init__(self, master):
        # room options available for event type
        RoomOption = ['D', 'E', 'F', 'G']
        super(bookParty, self).__init__(master,RoomOption)

        # Creation of wedding form set title, size ect..
        master.title("Party bookings")
        master.resizable(0, 0)
        master.config(background="powder blue")

        # defines options for bandName dropdown box
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        #variable to store selected band name from dropdown
        DefaultBandName = StringVar(master)
        DefaultBandName.set("Please Select a Band")  # default value

        # Labels for Party booking form
        self.lblSubheading.config(text="Please fill in the details for the Party event you are booking")
        self.lblBandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="powder blue")
        self.lblBandName.grid(row=7, columnspan=2,pady=(25, 0), padx=(10, 10))

        # dropdowns for party form
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [Validation.stringEmpty(self.savelist()), Events.Party.createParty(
                                                            self.EntnumberOfguest.get(),
                                                            self.EntnameOfContact.get(),
                                                            self.EntAddress.get(),
                                                            self.EntContactNumber.get(),
                                                            self.eventRoomNo,
                                                            self.CalDateOfEvent.get(),
                                                            self.bandName), master.destroy()])

    def savelist(self):
        self.validationTestList = []
        self.validationTestList.append(self.EntnumberOfguest.get())
        self.validationTestList.append(self.EntnameOfContact.get())
        self.validationTestList.append(self.EntAddress.get())
        self.validationTestList.append(self.EntContactNumber.get())
        self.validationTestList.append(self.eventRoomNo)
        self.validationTestList.append(self.CalDateOfEvent.get())
        self.validationTestList.append(self.bandName)
        return self.validationTestList

    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value