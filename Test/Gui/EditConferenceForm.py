from tkinter import *
from tkinter import messagebox
import Events.Conference
import Gui.BaseEditForm
import Validation
from Database import dbHelper
from Gui import DialogBoxes


class EditConference(Gui.BaseEditForm.BaseEditEvent):

    def __init__(self, master, booking, viewbookingself):
        super().__init__(master, booking)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Update Selected Conference")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        self.viewbookingself = viewbookingself
        self.booking = booking

        def ch_box_sel():
            print(self.CheckVar1.get())

        # defines options for dropdown boxes

        # Labels for Conference booking form
        self.lblSubheading.config(text="Please update any details that you want to change")

        self.lblCompanyname = Label(master, text="Company Name", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblCompanyname.grid(row=7,columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblNoofDays = Label(master, text="Number of Days", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoofDays.grid(row=8,columnspan=2, pady=(25, 0),padx=(10, 10))

        self.lblProjectorReq = Label(master, text="Projector Required", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblProjectorReq.grid(row=9, columnspan=2,pady=(25,0),padx=(10,10))

        # Entry boxes, dropdowns and datepicker for conference form
        self.EntCompanyName = Entry(master, font=("arial", 10), width=50)
        self.CompanyNameVcmd = (self.EntCompanyName.register(lambda P: Validation.max_character_length_150(P, master)))
        self.EntCompanyName.config(validate='key', validatecommand=(self.CompanyNameVcmd, '%P'))

        self.number_of_days = StringVar()
        self.EntNoOfDays = Entry(master, font=("arial", 10), width=50,textvariable=self.number_of_days)
        self.DaysVcmd = (self.EntNoOfDays.register(lambda P: Validation.max_size_31(P,master)))
        self.EntNoOfDays.config(validate='key', validatecommand=(self.DaysVcmd, '%P'))

        # checkbox
        self.CheckVar1 = IntVar()
        self.chxProjectorRequired = Checkbutton(master, text='', variable=self.CheckVar1, onvalue=True, offvalue=False, bg="#70ABAF", command=ch_box_sel)

        # Entry boxes, dropdowns and datepicker for conference form being placed using a grid layout
        self.EntCompanyName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntNoOfDays.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        # checkbox
        self.chxProjectorRequired.grid(row=9, column=2, pady=(25, 0), padx=(0, 25))
        print(booking.dateOfBooking)
        # Buttons for Add and Cancel on the conference form
        self.btnUpdateBooking.config(command=lambda: self.validation(booking)) # calls update ,destroy and message box

        self.populateform_conference(self.booking)

        self.display_date.trace('w', lambda name, index, mode: self.conference_room_check())
        self.number_of_days.trace('w', lambda name, index, mode: self.conference_room_check())

    # functions
    def conference_room_check(self):
        if not self.number_of_days.get() or not self.display_date.get():
            self.om_room_val.set("Pick a date and duration first")
            self.OpmEventRoomNumber.config(state="disabled")
            return

        self.OpmEventRoomNumber.config(state="normal")

        self.room_option_menu_menu = self.OpmEventRoomNumber.children["menu"]
        self.room_option_menu_menu.delete(0, "end")
        self.om_room_val.set("Pick a room")
        for value in dbHelper.rooms_in_use_update("conferenceTable", self.display_date.get(),id=self.booking.ID, number_of_days=int(self.number_of_days.get())):
            self.room_option_menu_menu.add_command(label=value, command=lambda v=value: self.om_room_val.set(v))

    def populateform_conference(self, booking):
        self.EntCompanyName.insert(0, booking.companyName)
        self.EntNoOfDays.insert(0, booking.noOfDays)

        value = booking.projectorRequired

        if value == "Yes":
            self.chxProjectorRequired.select()
        elif value == "No":
            self.chxProjectorRequired.deselect()

# validation
    def validation(self, booking):
        valpassed = True

        if Validation.stringEmpty(self.savelist()):
            valpassed = False
            return messagebox.showinfo("Booking Failed",
                                       "All fields are required to be filled in.", parent=self.master)

        elif dbHelper.con_date_conflict_update("conferenceTable", self.CalDateOfEvent.get(), self.EntNoOfDays.get(), self.eventRoomNo, booking.ID):
            valpassed = False
            return messagebox.showinfo('Booking Failed',
                                       'Room is currently booked. Please select another room, or change the date of booking.', parent=self.master)
        elif Validation.min_number([self.EntnumberOfguest.get(), self.EntNoOfDays.get()]):
            valpassed = False
            return messagebox.showinfo("Booking Failed", "Must have more than one guest.\nThe duration of the event must be at least one day.", parent=self.master)

        if valpassed:
            Events.Conference.updateConference(self.EntnumberOfguest.get(),
                                               self.EntnameOfContact.get(),
                                               self.EntAddress.get(),
                                               self.EntContactNumber.get(), self.om_room_val.get(),
                                               self.display_date.get(), booking.dateOfBooking,
                                               self.EntCompanyName.get(),
                                               self.EntNoOfDays.get(),
                                               self.CheckVar1.get(), booking.ID)

            DialogBoxes.updated(self, master=self.master, view_booking=self.viewbookingself)
            self.master.destroy()

    def savelist(self):
        self.validationTestList = []
        self.validationTestList.append(self.EntnumberOfguest.get())
        self.validationTestList.append(self.EntnameOfContact.get())
        self.validationTestList.append(self.EntAddress.get())
        self.validationTestList.append(self.EntContactNumber.get())
        self.validationTestList.append(self.om_room_val.get())
        self.validationTestList.append(self.display_date.get())
        self.validationTestList.append(self.EntCompanyName.get())
        self.validationTestList.append(self.EntNoOfDays.get())
        return self.validationTestList

