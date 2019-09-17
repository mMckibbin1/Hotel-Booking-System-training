from tkinter import *
import tkinter as Tkinter
import tkinter.ttk as ttk
from Database import dbHelper
from Events import Wedding, Party, Conference

class frmViewBooking(Tkinter.Frame):
    #datalist = None
    master2 = None

    def __init__(self, master):
        '''
        Constructor
        '''
        # self.root = Tkinter.Tk()
        Tkinter.Frame.__init__(self, master)
        self.parent = master
        #self.initialize_user_interface()

        master.resizable(0, 0)

    #def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Booking view")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")

        def selectItem(a):

            listofevents = []
            listofdb = dbHelper.read_all_from_db()
            #try:
            curItem = self.tree.focus()

            RowID = self.tree.item(curItem)['text']


            for value in self.tree.item(curItem)['values']:
                listofevents.append(value)

                types = listofevents[0]

            for list in listofdb:
                for object in list:
                    if types == "Wedding":
                        if type(object) == Wedding.Wedding:
                            if object.ID == RowID:
                                return DetailsLabelChange(self, types, object)
                    elif types == "Party":
                        if type(object) == Party.Party:
                            if object.ID == RowID:
                                return DetailsLabelChange(self, types, object)
                    elif types == "Conference":
                        if type(object) == Conference.Conference:
                            if object.ID == RowID:
                                return DetailsLabelChange(self, types, object)



            #except:
                #print('Select a row!!!!')

        # functions to allow the labels to change in the additional info labelframe
        # removes all labels stored within labelframe
        def removeAllLabels(self):
            self.lblNoofGuests.grid_remove()
            self.lblDisNoofGuests.grid_remove()
            self.lblAddress.grid_remove()
            self.lblDisAddress.grid_remove()
            self.lblDateofBooking.grid_remove()
            self.lblDisDateofBooking.grid_remove()
            self.lblCostPerHead.grid_remove()
            self.lblDisCostPerHead.grid_remove()
            self.lblBandName.grid_remove()
            self.lblDisBandName.grid_remove()
            self.lblBandPrice.grid_remove()
            self.lblDisBandPrice.grid_remove()
            self.lblCompanyName.grid_remove()
            self.lblDisCompanyName.grid_remove()
            self.lblNumberofDays.grid_remove()
            self.lblDisNumberofDays.grid_remove()
            self.lblProjectorRequired.grid_remove()
            self.lblDisProjectorRequired.grid_remove()
            self.lblNoOfBedsReserved.grid_remove()
            self.lblDisNoOfBedsReserved.grid_remove()

        # adds the labels that are consistent throughout all event types
        def addBaseLables(self, object):
            self.lblNoofGuests.grid()
            self.lblDisNoofGuests.grid()
            self.lblAddress.grid()
            self.lblDisAddress.grid()
            self.lblDateofBooking.grid()
            self.lblDisDateofBooking.grid()
            self.lblCostPerHead.grid()
            self.lblDisCostPerHead.grid()

            self.lblDisNoofGuests.config(text=object.noGuests)
            self.lblDisAddress.config(text=object.address)
            self.lblDisDateofBooking.config(text=object.dateOfBooking)
            self.lblDisCostPerHead.config(text=object.costPerHead)

        # adds the labels that are used for weddings
        def addWeddingLabels(self, object):
            addBaseLables(self, object)
            self.lblBandName.grid()
            self.lblDisBandName.grid()
            self.lblBandPrice.grid()
            self.lblDisBandPrice.grid()
            self.lblNoOfBedsReserved.grid()
            self.lblDisNoOfBedsReserved.grid()

            self.lblDisBandName.config(text=object.bandName)
            self.lblDisBandPrice.config(text=object.bandPrice)
            self.lblDisNoOfBedsReserved.config(text=object.noBedroomsReserved)

        # adds the labels that are used for parties
        def addPartyLabels(self,object):
            addBaseLables(self, object)
            self.lblBandName.grid()
            self.lblDisBandName.grid()
            self.lblBandPrice.grid()
            self.lblDisBandPrice.grid()

            self.lblDisBandName.config(text=object.bandName)
            self.lblDisBandPrice.config(text=object.bandPrice)

        # adds the labels that are used for conferences
        def addConferenceLables(self, object):
            addBaseLables(self, object)
            self.lblCompanyName.grid()
            self.lblDisCompanyName.grid()
            self.lblNumberofDays.grid()
            self.lblDisNumberofDays.grid()
            self.lblProjectorRequired.grid()
            self.lblDisProjectorRequired.grid()

            self.lblDisCompanyName.config(text=object.companyName)
            self.lblDisNumberofDays.config(text=object.noOfDays)
            self.lblDisProjectorRequired.config(text=object.projectorRequired)

        def updatePriceBreakdown(self, object):
            self.lblDisGuestPrice.config(text= object.guestsCost())

            if type(object) == Conference.Conference:
                self.lblBandCost.config(text="Cost Per Day:")
                self.lblDisBandCost.config(text=str(object.guestsCost()) + '   ( * ' + str(object.noOfDays) + " days)")
            else:
                self.lblBandCost.config(text="Band Price")
                self.lblDisBandCost.config(text=object.bandPrice)

            self.lblDisSubTotal.config(text=object.grosstotal())
            self.lblDisVat.config(text=object.VAT())
            self.lblDisTotal.config(text=object.netTotal())

        # function to change the labels shown, depending on the event type selected in the treeview
        def DetailsLabelChange(self, eventType, object):

            if eventType == 'Wedding':
                removeAllLabels(self)
                addWeddingLabels(self, object)
                updatePriceBreakdown(self, object)

            elif eventType == 'Party':
                removeAllLabels(self)
                addPartyLabels(self, object)
                updatePriceBreakdown(self, object)

            elif eventType == 'Conference':
                removeAllLabels(self)
                addConferenceLables(self, object)
                updatePriceBreakdown(self, object)

            else:
                removeAllLabels(self)


        # Set the treeview
        self.tree = ttk.Treeview(self.parent,
                                 columns=('Event Type', 'Contact Name', 'Contact Number', 'Event Date',
                                          'Room Number', 'Total Cost'))
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Event Type')
        self.tree.heading('#2', text='Contact Name')
        self.tree.heading('#3', text='Contact Number')
        self.tree.heading('#4', text='Event Date')
        self.tree.heading('#5', text='Room Number')
        self.tree.heading('#6', text='Total Cost')
        self.tree.bind('<ButtonRelease-1>', selectItem)
        self.tree.column('#0', width=100)  # column width auto size
        self.tree.column('#1', width=100)
        self.tree.column('#2', width=100)
        self.tree.column('#3', width=100)
        self.tree.column('#4', width=100)
        self.tree.column('#5', width=100)
        self.tree.column('#6', width=100)
        self.tree.grid(row=0, columnspan=7, sticky="nws", padx=10, pady=(20, 0), rowspan=2)
        self.treeview = self.tree

        #  Total income section below the tree view
        ttk.Label(self.parent, text="Total Income", font=("arial", 10, "bold"), background="lavender").grid(row=2,
                                                                                    column=5, sticky="se", padx=(10, 10))

        self.lblTotalIncome = Label(self.parent, text="£10000", font=("arial", 10, "bold"), background="lavender")
        self.lblTotalIncome.grid(row=2, column=6,sticky="sw", padx=(0, 55))

        # BUTTONS #
        # button hover colour - update
        def on_enterUpdate(e):
            btnUpdate['background'] = "PaleTurquoise1"

        def on_leaveUpdate(e):
            btnUpdate['background'] = "snow"

        # button hover colour - delete
        def on_enterDelete(e):
            btnDelete['background'] = "tomato"

        def on_leaveDelete(e):
            btnDelete['background'] = "snow"

        # button hover colour - refresh
        def on_enterRefresh(e):
            btnRefresh['background'] = "PaleTurquoise1"

        def on_leaveRefresh(e):
            btnRefresh['background'] = "snow"


        # button update
        btnUpdate = Button(self.parent, text="Update", width=13, height=2, background="snow", font=("arial", 10))
        btnUpdate.grid(row=3, column=7, sticky="ne", pady=(0, 20))
        btnUpdate.bind("<Enter>", on_enterUpdate)
        btnUpdate.bind("<Leave>", on_leaveUpdate)

        # button delete
        btnDelete = Button(self.parent, text="Delete", width=13, height=2, background="snow", font=("arial", 10))
        btnDelete.grid(row=3, column=8, sticky="ne", pady=(0, 20))
        btnDelete.bind("<Enter>", on_enterDelete)
        btnDelete.bind("<Leave>", on_leaveDelete)

        # button refresh
        btnRefresh = Button(self.parent, text="Refresh", width=13, height=2, background="snow", font=("arial", 10))
        btnRefresh.grid(row=3, column=0, sticky="nw", pady=(0, 20), padx=(10, 0))
        btnRefresh.bind("<Enter>", on_enterRefresh)
        btnRefresh.bind("<Leave>", on_leaveRefresh)


        # LABELFRAMES #
        # labelframe for select date
        self.Selectlabelframe = LabelFrame(self.parent, width=305, height=167)
        self.Selectlabelframe.grid(row=4, column=0, columnspan=12, sticky="ew", )
        self.Selectlabelframe.config(background="alice blue")

        # columns
        self.Selectlabelframe.grid_columnconfigure(1, minsize=50)
        self.Selectlabelframe.grid_columnconfigure(2, minsize=50)
        self.Selectlabelframe.grid_columnconfigure(3, minsize=50)
        self.Selectlabelframe.grid_columnconfigure(4, minsize=50)
        self.Selectlabelframe.grid_columnconfigure(5, minsize=50)
        self.Selectlabelframe.grid_columnconfigure(6, minsize=50)
        self.Selectlabelframe.grid_columnconfigure(7, minsize=50)

        # rows
        self.Selectlabelframe.grid_rowconfigure(1, minsize=20)
        self.Selectlabelframe.grid_rowconfigure(2, minsize=20)
        self.Selectlabelframe.grid_rowconfigure(3, minsize=20)

        # Search for dates
        ttk.Label(self.Selectlabelframe, text="Search by date", font=("arial", 11, "bold"), background="alice blue")\
            .grid(row=2, column=0, sticky=W, columnspan=1, padx=10, pady=(0, 5))
        self.EntStartDate = ttk.Entry(self.Selectlabelframe, font=("arial", 10), width=30)
        self.EntStartDate.grid(row=3, column=0, sticky="ew", padx=10, columnspan=1, pady=(0, 20))
        ttk.Label(self.Selectlabelframe, text="To", font=("arial", 10, "bold"), background="alice blue")\
            .grid(row=3, column=1, pady=(0, 20))
        self.EntEndDate = ttk.Entry(self.Selectlabelframe, font=("arial", 10), width=30)
        self.EntEndDate.grid(row=3, column=2, sticky="ew", padx=10, columnspan=1, pady=(0, 20))

        # check boxes
        self.CbxWedding = Checkbutton(self.Selectlabelframe, text='Weddings', font=("arial", 10),
                                      background="alice blue")
        self.CbxWedding.grid(row=3, column=4, padx=(0, 20), sticky=W, pady=(0, 20))
        self.CbxConference = Checkbutton(self.Selectlabelframe, text='Conference', font=("arial", 10),
                                         background="alice blue")
        self.CbxConference.grid(row=3, column=5, padx=(0, 20), pady=(0, 20))
        self.CbxParties = Checkbutton(self.Selectlabelframe, text='Parties', font=("arial", 10),
                                      background="alice blue")
        self.CbxParties.grid(row=3, column=6, padx=(0, 0), pady=(0, 20))


        # button hover colour - search
        def on_enterSearch(e):
            btnSearchDate['background'] = "PaleTurquoise1"

        def on_leaveSearch(e):
            btnSearchDate['background'] = "snow"

        # button search
        btnSearchDate = Button(self.Selectlabelframe, text="Search",
                               width=13, height=2, background="snow", font=("arial", 10))
        btnSearchDate.grid(row=3, column=8, pady=(0, 20), padx=(8, 15))
        btnSearchDate.bind("<Enter>", on_enterSearch)
        btnSearchDate.bind("<Leave>", on_leaveSearch)


        # labelframe for additional info box
        self.labelframe = LabelFrame(self.parent, text="Additional Information", width=324, height=167,
                                     background="lavender", font=("arial", 9, "bold"))
        self.labelframe.grid(row=0, column=7, columnspan=3, padx=(10, 20), pady=(30, 0))

        # columns
        self.labelframe.grid_columnconfigure(1, minsize=160)
        self.labelframe.grid_columnconfigure(2, minsize=160)

        # rows
        self.labelframe.grid_rowconfigure(1, minsize=20)
        self.labelframe.grid_rowconfigure(2, minsize=20)
        self.labelframe.grid_rowconfigure(3, minsize=20)
        self.labelframe.grid_rowconfigure(4, minsize=20)
        self.labelframe.grid_rowconfigure(5, minsize=20)
        self.labelframe.grid_rowconfigure(6, minsize=20)
        self.labelframe.grid_rowconfigure(7, minsize=20)

        # labels for no. of guests in additional details label frame
        self.lblNoofGuests = Label(self.labelframe, text="No of Guests: ", background="lavender")
        self.lblNoofGuests.grid(row=1, column=1)
        self.lblDisNoofGuests = Label(self.labelframe, text='10', background="lavender")
        self.lblDisNoofGuests.grid(row=1, column=2)

        # labels for Address in additional details label frame
        self.lblAddress = Label(self.labelframe, text="Address: ", background="lavender")
        self.lblAddress.grid(row=2, column=1)
        self.lblDisAddress = Label(self.labelframe, text='SERC', background="lavender")
        self.lblDisAddress.grid(row=2, column=2)

        # labels for Date of Booking in additional details label frame
        self.lblDateofBooking = Label(self.labelframe, text="Date of Booking: ", background="lavender")
        self.lblDateofBooking.grid(row=3, column=1)
        self.lblDisDateofBooking = Label(self.labelframe, text='10/10/2010', background="lavender")
        self.lblDisDateofBooking.grid(row=3, column=2)

        # labels for Cost Per Head in additional details label frame
        self.lblCostPerHead = Label(self.labelframe, text="Cost Per Head: ", background="lavender")
        self.lblCostPerHead.grid(row=4, column=1)
        self.lblDisCostPerHead = Label(self.labelframe, text='30', background="lavender")
        self.lblDisCostPerHead.grid(row=4, column=2)

        # labels for Band Name in additional details label frame
        self.lblBandName = Label(self.labelframe, text="Band Name: ", background="lavender")
        self.lblBandName.grid(row=5, column=1)
        self.lblDisBandName = Label(self.labelframe, text='Prawn Mendes', background="lavender")
        self.lblDisBandName.grid(row=5, column=2)

        # labels for Band Price in additional details label frame
        self.lblBandPrice = Label(self.labelframe, text="Band Price: ", background="lavender")
        self.lblBandPrice.grid(row=6, column=1)
        self.lblDisBandPrice = Label(self.labelframe, text='£250', background="lavender")
        self.lblDisBandPrice.grid(row=6, column=2)

        # labels for number of bedrooms reserved in additional details label frame
        self.lblNoOfBedsReserved = Label(self.labelframe, text="No. of Bedrooms Reserved: ", background="lavender")
        self.lblNoOfBedsReserved.grid(row=7, column=1)
        self.lblDisNoOfBedsReserved = Label(self.labelframe, text='5', background="lavender")
        self.lblDisNoOfBedsReserved.grid(row=7, column=2)

        # labels for Company Name in additional details label frame
        self.lblCompanyName = Label(self.labelframe, text="Company Name ", background="lavender")
        self.lblCompanyName.grid(row=5, column=1)
        self.lblDisCompanyName = Label(self.labelframe, text='SERC', background="lavender")
        self.lblDisCompanyName.grid(row=5, column=2)

        # labels for Number of Days in additional details label frame
        self.lblNumberofDays = Label(self.labelframe, text="Number of Days: ", background="lavender")
        self.lblNumberofDays.grid(row=6, column=1)
        self.lblDisNumberofDays = Label(self.labelframe, text='5', background="lavender")
        self.lblDisNumberofDays.grid(row=6, column=2)

        # labels for projector required in additional details label frame
        self.lblProjectorRequired = Label(self.labelframe, text="Projector Required: ", background="lavender")
        self.lblProjectorRequired.grid(row=7, column=1)
        self.lblDisProjectorRequired = Label(self.labelframe, text='Yes', background="lavender")
        self.lblDisProjectorRequired.grid(row=7, column=2)

        # setting weight for rows and columns
        self.labelframe.grid_rowconfigure(0, weight=1)
        self.labelframe.grid_rowconfigure(3, weight=1)
        self.labelframe.grid_columnconfigure(0, weight=1)
        self.labelframe.grid_columnconfigure(3, weight=1)


        # labelframe for more price breakdown
        self.Totallabelframe = LabelFrame(self.parent, text="Price Breakdown", width=324, height=100,
                                          background="lavender", font=("arial", 9, "bold"))
        self.Totallabelframe.grid(row=1, column=7, columnspan=3, padx=(10, 20), pady=(0, 20))

        # columns
        self.Totallabelframe.grid_columnconfigure(1, minsize=80)
        self.Totallabelframe.grid_columnconfigure(2, minsize=80)
        self.Totallabelframe.grid_columnconfigure(3, minsize=80)
        self.Totallabelframe.grid_columnconfigure(4, minsize=80)

        # rows
        self.Totallabelframe.grid_rowconfigure(1, minsize=20)
        self.Totallabelframe.grid_rowconfigure(2, minsize=20)
        self.Totallabelframe.grid_rowconfigure(3, minsize=20)
        self.Totallabelframe.grid_rowconfigure(4, minsize=20)

        # label for guest price
        self.lblGuestPrice = Label(self.Totallabelframe, text="Guests: ", background="lavender")
        self.lblGuestPrice.grid(row=1, column=1)
        self.lblDisGuestPrice = Label(self.Totallabelframe, text='£', background="lavender")
        self.lblDisGuestPrice.grid(row=1, column=2)

        # Label for band price
        self.lblBandCost = Label(self.Totallabelframe, text="Band: ", background="lavender")
        self.lblBandCost.grid(row=1, column=3)
        self.lblDisBandCost = Label(self.Totallabelframe, text="£", background="lavender")
        self.lblDisBandCost.grid(row=1, column=4)

        # Label for sub total
        self.lblSubTotal = Label(self.Totallabelframe, text="Sub Total: ", background="lavender")
        self.lblSubTotal.grid(row=2, column=1)
        self.lblDisSubTotal = Label(self.Totallabelframe, text="£", background="lavender")
        self.lblDisSubTotal.grid(row=2, column=2)

        # Label for VAT
        self.lblVat = Label(self.Totallabelframe, text="VAT: ", background="lavender")
        self.lblVat.grid(row=3, column=1)
        self.lblDisVat = Label(self.Totallabelframe, text="£", background="lavender")
        self.lblDisVat.grid(row=3, column=2)

        # Label for total
        self.lblTotal = Label(self.Totallabelframe, text="Total: ", background="lavender")
        self.lblTotal.grid(row=4, column=1)
        self.lblDisTotal = Label(self.Totallabelframe, text="£", background="lavender")
        self.lblDisTotal.grid(row=4, column=2)

        # setting weight for rows and columns
        self.Totallabelframe.grid_rowconfigure(0, weight=1)
        self.Totallabelframe.grid_rowconfigure(3, weight=1)
        self.Totallabelframe.grid_columnconfigure(0, weight=1)
        self.Totallabelframe.grid_columnconfigure(3, weight=1)

        #DetailsLabelChange(self, '',)

        self.master2 = self
        self.loadData(self.master2)
        self.CalIncome(self.master2)

    def CalIncome(self, master):
        totalIncome = 0.0
        for child in master.treeview.get_children():
            totalIncome += float(master.treeview.item(child, "values")[5])
            master.lblTotalIncome.config(text=totalIncome)

    def loadData(self, master):

        datalist = dbHelper.read_all_from_db()

        for list in datalist:
            for object in list:
                if type(object) == Wedding.Wedding:
                    insert_data(master, object.ID, "Wedding", object.nameOfContact,
                                               object.contactNo, object.dateOfEvent, object.eventRoomNo,
                                               object.netTotal())
                elif type(object) == Party.Party:
                    insert_data(master, object.ID, "Party", object.nameOfContact,
                                object.contactNo, object.dateOfEvent, object.eventRoomNo,
                                object.netTotal())
                elif type(object) == Conference.Conference:
                    insert_data(master, object.ID, "Conference", object.nameOfContact,
                                object.contactNo, object.dateOfEvent, object.eventRoomNo,
                                object.netTotal())

# adding data to treeview
def insert_data(self, ID, EventType, nameOfContact, contactNo, dateOfEvent, eventRoomNo, netTotal):
    self.treeview.insert('', 'end', text= ID,
                         values=( EventType, nameOfContact, contactNo, dateOfEvent, eventRoomNo, netTotal))