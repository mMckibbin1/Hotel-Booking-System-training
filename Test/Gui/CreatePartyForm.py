import Gui.BaseCreateForm
from tkinter import *
import Events.Party
import Validation
from Gui import DialogBoxes
from Database import dbHelper
from tkinter import messagebox


class bookParty(Gui.BaseCreateForm.BaseEvent):

    bandName = ''

    def __init__(self, master):
        # room options available for event type
        RoomOption = ['D', 'E', 'F', 'G']
        super(bookParty, self).__init__(master,RoomOption)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Book a Party")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        # defines options for bandName dropdown box
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        # variable to store selected band name from dropdown
        DefaultBandName = StringVar(master)
        DefaultBandName.set("Please Select a Band")  # default value

        # Labels for Party booking form
        self.lblSubheading.config(text="Please Fill in the Details for the Party")
        self.lblBandName = Label(master, text="Band Name",font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblBandName.grid(row=7, columnspan=2,pady=(25, 0), padx=(10, 10))

        # dropdowns for party form
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [self.validation(), master.destroy()])

    # validation
    def validation(self):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.")
        elif dbHelper.date_conflict("partyTable", self.CalDateOfEvent.get(), self.eventRoomNo):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.')
        elif Validation.min_number(self.EntnumberOfguest.get()):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have more than one guest.")


        if valpassed:
            Events.Party.createParty(
                self.EntnumberOfguest.get(),
                self.EntnameOfContact.get(),
                self.EntAddress.get(),
                self.EntContactNumber.get(),
                self.eventRoomNo,
                self.CalDateOfEvent.get(),
                self.bandName)

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