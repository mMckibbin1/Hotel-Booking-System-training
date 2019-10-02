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

        # Labels for Wedding booking form
        self.lblSubheading.config(text="Please Fill in the Details for the Wedding")

        self.lblbandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblbandName.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoofRoomsRes = Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"),
                                     bg="#70ABAF")
        self.lblNoofRoomsRes.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes and dropdowns

        self.om_band_name = StringVar()
        self.om_band_name.set("Please Select a date first")
        self.OpmBandName = OptionMenu(master, self.om_band_name,() )
        self.OpmBandName.config(state="disabled")

        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)
        self.BedsVcmd = (self.EntBedroomReserved.register(lambda P:Validation.max_size_50(P,master)))
        self.EntBedroomReserved.config(validate='key', validatecommand=(self.BedsVcmd, '%P'))

        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the wedding form
        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [self.validation()])

        self.OpmEventRoomNumber.config(state="disabled")
        self.display_date.trace('w', lambda name, index, mode: [self.wedding_room_check(), self.band_name_check()])

    def band_name_check(self):
        self.OpmBandName.config(state="normal")

        self.band_name_option_menu_menu = self.OpmBandName.children["menu"]
        self.band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set("Pick a Band")
        for value in dbHelper.bands_in_use(self.display_date.get()):
            self.band_name_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_band_name.set(v))

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
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.", parent=self.master)

        elif dbHelper.date_conflict("weddingTable", self.display_date.get(), self.om_room_val):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntnumberOfguest.get()]):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have entered more than one guest.", parent=self.master)

        if valpassed:
            Events.Wedding.createwedding(
                self.EntnumberOfguest.get(),
                self.EntnameOfContact.get(),
                self.EntAddress.get(),
                self.EntContactNumber.get(),
                self.om_room_val.get(),
                self.CalDateOfEvent.get(),
                self.om_band_name.get(),
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
        self.validationTestList.append(self.om_band_name.get())
        self.validationTestList.append(self.EntBedroomReserved.get())
        return self.validationTestList
