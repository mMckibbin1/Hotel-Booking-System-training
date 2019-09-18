from tkinter import *
import Events.Conference
import Gui.BaseCreateForm


class bookConference(Gui.BaseCreateForm.BaseEvent):

    def __init__(self, master):
        # room options available for event type
        RoomOption = ['A', 'B', 'C']

        super().__init__(master, RoomOption)

        super().__init__(master,RoomOption)

        # Creation of wedding form set title, size ect..
        master.title("Hotel Booking System - Book a Conference")
        master.resizable(0, 0)
        master.config(background="#70ABAF")

        # method to get vaule of checkbutton
        def ch_box_sel():
            print(CheckVar1.get())

        # Labels for Conference booking form
        self.lblSubheading.config(text="Please Fill in the Details for the Conference")

        self.lblCompanyname = Label(master, text="Company Name",font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblCompanyname.grid(row=7,columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblNoofDays = Label(master, text="Number of Days",font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblNoofDays.grid(row=8,columnspan=2, pady=(25, 0),padx=(10, 10))

        self.lblProjectorReq = Label(master, text="Projector Required", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblProjectorReq.grid(row=9, columnspan=2,pady=(25,0),padx=(10,10))


        # Entry boxes, dropdowns and datepicker for conference form
        self.EntCompanyName = Entry(master, font=("arial", 10), width=50)
        self.EntNoOfDays = Entry(master, font=("arial", 10), width=50)

        # checkbox now works :)
        #checkbox

        CheckVar1 = IntVar()
        self.chxProjectorRequired = Checkbutton(master, text='', variable=CheckVar1, onvalue=True, offvalue=False, bg="#70ABAF", command=ch_box_sel)

        # Entry boxes
        self.EntCompanyName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntNoOfDays.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))


        # checkbox.....

        #checkbox

        self.chxProjectorRequired.grid(row=9, column=2, pady=(25, 0), padx=(0, 25))

        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [Events.Conference.createConference(self.EntnumberOfguest.get(),
                                                                          self.EntnameOfContact.get(),
                                                                          self.EntAddress.get(),
                                                                          self.EntContactNumber.get(),
                                                                          self.eventRoomNo,
                                                                          self.CalDateOfEvent.get(),
                                                                          self.EntCompanyName.get(),
                                                                          self.EntNoOfDays.get(),
                                                                          #checkbox get
                                                                          CheckVar1.get()), master.destroy()])