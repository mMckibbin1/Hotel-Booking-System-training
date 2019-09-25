from tkinter import *
import Events.Wedding
import Gui.BaseCreateForm
import Validation
from Database import dbHelper
from Gui import DialogBoxes
from tkinter import messagebox


class bookwedding(Gui.BaseCreateForm.BaseEvent):
    def __init__(self, master):
        # Creation of wedding form set title, size ect..
        super().__init__(master)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Book a Wedding")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        # defines options for dropdown boxes
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]
        # variable to store selected band name from dropdown
        DefaultBandName = StringVar(master)
        DefaultBandName.set("Please Select a Band")  # default value

        # Labels for Wedding booking form
        self.lblSubheading.config(text="Please Fill in the Details for the Wedding")

        self.lblbandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblbandName.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoofRoomsRes = Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"),
                                     bg="#70ABAF")
        self.lblNoofRoomsRes.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes, dropdowns and datepicker for wedding form
        # Entry boxes and dropdowns
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)

        self.OpmEventRoomNumber.config(state="disabled")


        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)
        self.BedsVcmd = (self.EntBedroomReserved.register(Validation.callback))
        self.EntBedroomReserved.config(validate='all', validatecommand=(self.BedsVcmd, '%S'))

        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the wedding for
        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [self.validation()])

        self.display_date.trace('w', lambda name, index, mode: self.wedding_room_check())

    def wedding_room_check(self):
        self.OpmEventRoomNumber.config(state="normal")

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")
        for value in dbHelper.rooms_in_use("weddingTable", self.display_date.get()):
            self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    # validation
    def validation(self):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.")

        elif dbHelper.date_conflict("weddingTable", self.display_date.get(), self.om_room_val):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.')
        elif Validation.min_number([self.EntnumberOfguest.get(), self.EntBedroomReserved.get()]):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have entered more than one guest and room.")

        if valpassed:
            Events.Wedding.createwedding(
                self.EntnumberOfguest.get(),
                self.EntnameOfContact.get(),
                self.EntAddress.get(),
                self.EntContactNumber.get(),
                self.om_room_val.get(),
                self.CalDateOfEvent.get(),
                self.bandName,
                self.EntBedroomReserved.get())

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
        self.validationTestList.append(self.bandName)
        self.validationTestList.append(self.EntBedroomReserved.get())
        return self.validationTestList

    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value
