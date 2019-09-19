from tkinter import *
import Events.Wedding
import Gui.BaseCreateForm
import Validation


class bookwedding(Gui.BaseCreateForm.BaseEvent):

    # setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''

    #setting default values for BandName as a empty string
    bandName = ''

    def __init__(self, master):
        # room options available for event type
        RoomOption = ['H', 'I']

        super().__init__(master, RoomOption)
        # Creation of wedding form set title, size ect..
        super().__init__(master,RoomOption)

        #Creation of wedding form set title, size ect..
        master.title("Wedding bookings")
        master.resizable(0, 0)
        master.config(background="powder blue")

        # defines options for dropdown boxes
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]
        # variable to store selected band name from dropdown
        DefaultBandName = StringVar(master)
        DefaultBandName.set("Please Select a Band")  # default value


        # Labels for Wedding booking form
        self.lblSubheading.config(text="Please fill in the details for the wedding event you are booking")

        self.lblbandName = Label(master, text="Band Name", font=("arial", 10, "bold"), bg="powder blue")
        self.lblbandName.grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.lblNoofRoomsRes = Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"), bg="powder blue")
        self.lblNoofRoomsRes.grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        # Entry boxes, dropdowns and datepicker for wedding form
        #Entry boxes and dropdowns
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)

        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)
        self.BedsVcmd = (self.EntBedroomReserved.register(Validation.callback))
        self.EntBedroomReserved.config(validate='all', validatecommand=(self.BedsVcmd, '%P'))

        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))


        # Buttons for Add and Cancel on the wedding for
        # Button config to override the parent button config
        self.btnAddBooking.config(command=lambda: [Validation.stringEmpty(self.savelist()), Events.Wedding.createwedding(
                                                                        self.EntnumberOfguest.get(),
                                                                        self.EntnameOfContact.get(),
                                                                        self.EntAddress.get(),
                                                                        self.EntContactNumber.get(),
                                                                        self.eventRoomNo,
                                                                        self.CalDateOfEvent.get(),
                                                                        self.bandName,
                                                                        self.EntBedroomReserved.get()), master.destroy()])

        # Buttons for Add and Cancel on the wedding form being placed using grid layout

    # validation
    def savelist(self):
        self.validationTestList = []
        self.validationTestList.append(self.EntnumberOfguest.get())
        self.validationTestList.append(self.EntnameOfContact.get())
        self.validationTestList.append(self.EntAddress.get())
        self.validationTestList.append(self.EntContactNumber.get())
        self.validationTestList.append(self.eventRoomNo)
        self.validationTestList.append(self.CalDateOfEvent.get())
        self.validationTestList.append(self.bandName)
        self.validationTestList.append(self.EntBedroomReserved.get())
        return self.validationTestList

    # function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value


    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value