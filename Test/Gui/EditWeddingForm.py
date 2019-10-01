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
        super().__init__(master, booking)
        #Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Update Selected Wedding")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        self.viewbookingself = viewbookingself
        self.booking = booking

        #Labels for Wedding booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblbandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblbandName.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoofRoomsRes = Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoofRoomsRes.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        #Entry boxes, dropdowns and datepicker for wedding form
        self.om_band_name = StringVar()
        self.om_band_name.set("Please Select a date first")
        self.OpmBandName = OptionMenu(master, self.om_band_name, ())

        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)

        # Entry boxes, dropdowns and datepicker for wedding form being placed using grid layout
        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.BedsVcmd = (self.EntBedroomReserved.register(lambda P: Validation.max_size_50(P, master)))
        self.EntBedroomReserved.config(validate='key', validatecommand=(self.BedsVcmd, '%P'))

        #Buttons for Add and Cancel on the wedding for
        self.btnUpdateBooking.config(command=lambda: self.validation(booking)) # calls update ,destroy and message box

        self.display_date.trace('w', lambda name, index, mode: [self.wedding_room_check(), self.band_name_check()])

        #Buttons for Add and Cancel on the wedding form being placed using grid layout
        self.populateform_wedding(booking)

        self.band_name_option_menu_menu = self.OpmBandName.children["menu"]
        self.band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set(booking.bandName)
        for value in dbHelper.bands_in_use_update("Wedding",self.display_date.get(), self.booking.ID):
            self.band_name_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_band_name.set(v))

    def band_name_check(self):
        self.OpmBandName.config(state="normal")

        self.band_name_option_menu_menu = self.OpmBandName.children["menu"]
        self.band_name_option_menu_menu.delete(0, "end")
        self.om_band_name.set("Pick a Band")
        for value in dbHelper.bands_in_use_update("Wedding",self.display_date.get(), self.booking.ID):
            self.band_name_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_band_name.set(v))

    def wedding_room_check(self):
        self.OpmEventRoomNumber.config(state="normal")

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")
        for value in dbHelper.rooms_in_use_update(event_type="weddingTable",id=self.booking.ID, date=self.display_date.get()):
            self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    def populateform_wedding(self, booking):
        self.om_band_name.set(booking.bandName)
        self.EntBedroomReserved.insert(0, booking.noBedroomsReserved)

# validation
    def validation(self, booking):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "All fields are required to be filled in.", parent=self.master)

        elif dbHelper.date_conflict_update("weddingTable", self.display_date.get(), self.om_room_val.get(), booking.ID):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntnumberOfguest.get()]):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have entered more than one guest.", parent=self.master)

        if valpassed:
            Events.Wedding.updateWedding(self.EntnumberOfguest.get(),
                                         self.EntnameOfContact.get(),
                                         self.EntAddress.get(),
                                         self.EntContactNumber.get(),
                                         self.om_room_val.get(),
                                         self.display_date.get(), booking.dateOfBooking,
                                         self.om_band_name.get(),
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
        self.validationTestList.append(self.display_date.get())
        self.validationTestList.append(self.om_room_val.get())
        self.validationTestList.append(self.om_band_name.get())
        self.validationTestList.append(self.EntBedroomReserved.get())
        return self.validationTestList