from tkinter import *
import tkinter as Tkinter
import tkinter.ttk as ttk
from Gui import DialogBoxes, viewbookinglogic
import Gui.viewbookinglogic

from Database import dbHelper
from Events import Wedding, Party, Conference
from Gui import EditPartyForm, EditWeddingForm, EditConferenceForm
from Gui.EditConferenceForm import EditConference
from Gui.EditPartyForm import EditParty
from Gui.EditWeddingForm import EditWedding




class frmViewBooking(Tkinter.Frame):
    master2 = None
    def __init__(self, master):
        Tkinter.Frame.__init__(self, master)
        self.parent = master
        master.resizable(0, 0)
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Booking view")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="#70ABAF")

        # Set the treeview
        self.tree = ttk.Treeview(self.parent,
                                 columns=('Event Type', 'Contact Name', 'Contact Number', 'Event Date',
                                          'Room Number', 'Total Cost'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Event Type')
        self.tree.heading('#2', text='Contact Name')
        self.tree.heading('#3', text='Contact Number')
        self.tree.heading('#4', text='Event Date')
        self.tree.heading('#5', text='Room Number')
        self.tree.heading('#6', text='Total Cost')
        self.tree.bind('<ButtonRelease-1>', lambda e :Gui.viewbookinglogic.selectItem(e,self))
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
        ttk.Label(self.parent, text="Total Income", font=("arial", 10, "bold"), background="#70ABAF").grid(row=2,
                                                                                    column=5, sticky="se", padx=(10, 10))

        self.lblTotalIncome = Label(self.parent, text="£0", font=("arial", 10, "bold"),background="#70ABAF")
        self.lblTotalIncome.grid(row=2, column=6,sticky="sw", padx=(0, 55))

        # BUTTONS #
        # button hover colour - update
        def on_enterUpdate(e):
            btnUpdate['background'] = "#F0F704"

        def on_leaveUpdate(e):
            btnUpdate['background'] = "snow"

        # button hover colour - delete
        def on_enterDelete(e):
            btnDelete['background'] = "tomato"

        def on_leaveDelete(e):
            btnDelete['background'] = "snow"

        # button hover colour - refresh
        def on_enterRefresh(e):
            btnRefresh['background'] = "#42A2FF"

        def on_leaveRefresh(e):
            btnRefresh['background'] = "snow"


        # button update
        btnUpdate = Button(self.parent, text="Update Selected Booking", width=20, height=2, background="snow", font=("arial", 10),
                           command = lambda :Gui.viewbookinglogic.update_selected(self.master2))
        btnUpdate.grid(row=3, column=7, sticky="ne", pady=(0, 20))
        btnUpdate.bind("<Enter>", on_enterUpdate)
        btnUpdate.bind("<Leave>", on_leaveUpdate)

        # button delete
        btnDelete = Button(self.parent, text="Delete Selected Booking", width=20, height=2, background="snow", font=("arial", 10),
                           command=lambda : viewbookinglogic.is_row_selected_delete(self))
        btnDelete.grid(row=3, column=8, sticky="ne", pady=(0, 20))
        btnDelete.bind("<Enter>", on_enterDelete)
        btnDelete.bind("<Leave>", on_leaveDelete)

        # button refresh
        btnRefresh = Button(self.parent, text="Refresh table", width=13, height=2, background="snow", font=("arial", 10),
                            command=lambda :Gui.viewbookinglogic.refreshData(self.master2))
        btnRefresh.grid(row=3, column=0, sticky="nw", pady=(0, 20), padx=(10, 0))
        btnRefresh.bind("<Enter>", on_enterRefresh)
        btnRefresh.bind("<Leave>", on_leaveRefresh)


        # LABELFRAMES #
        # labelframe for select date
        self.Selectlabelframe = LabelFrame(self.parent, width=305, height=167)
        self.Selectlabelframe.grid(row=4, column=0, columnspan=12, sticky="ew", )
        self.Selectlabelframe.config(background="#F0F7F4")

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
        ttk.Label(self.Selectlabelframe, text="Search by date", font=("arial", 11, "bold"), background="#F0F7F4")\
            .grid(row=2, column=0, sticky=W, columnspan=1, padx=10, pady=(0, 5))
        self.EntStartDate = ttk.Entry(self.Selectlabelframe, font=("arial", 10), width=30)
        self.EntStartDate.grid(row=3, column=0, sticky="ew", padx=10, columnspan=1, pady=(0, 20))
        self.EntStartDate.bind("<Button-1>", lambda event: Gui.viewbookinglogic.Calendarpopup(event,"EntStartDate",self.master2,master))
        ttk.Label(self.Selectlabelframe, text="To", font=("arial", 10, "bold"), background="#F0F7F4")\
            .grid(row=3, column=1, pady=(0, 20))
        self.EntEndDate = ttk.Entry(self.Selectlabelframe, font=("arial", 10), width=30)
        self.EntEndDate.grid(row=3, column=2, sticky="ew", padx=10, columnspan=1, pady=(0, 20))
        self.EntEndDate.bind("<Button-1>", lambda event: Gui.viewbookinglogic.Calendarpopup(event, "EntEndDate",self.master2,master))
        self.data = {}
        self.btn_clear_date = Button(self.Selectlabelframe,text="Clear Dates", width=13, height=2, background="snow",
                                     font=("arial", 10), command=lambda:Gui.viewbookinglogic.clear_date(self.master2))
        self.btn_clear_date.grid(row=4, column=0, sticky="ew", padx=10, columnspan=1, pady=(0, 20))

        # check boxes

        self.checkVarWedding = StringVar()
        self.checkVarConference = StringVar()
        self.checkVarParty = StringVar()

        self.CbxWedding = Checkbutton(self.Selectlabelframe, text='Weddings', variable=self.checkVarWedding, onvalue="weddingTable",
                                      offvalue="", font=("arial", 10),background="#F0F7F4")
        self.CbxWedding.grid(row=3, column=4, padx=(0, 20), sticky=W, pady=(0, 20))

        self.CbxConference = Checkbutton(self.Selectlabelframe, text='Conference', font=("arial", 10),
                                         background="#F0F7F4",variable=self.checkVarConference, onvalue="conferenceTable",
                                         offvalue="")
        self.CbxConference.grid(row=3, column=5, padx=(0, 20), pady=(0, 20))

        self.CbxParties = Checkbutton(self.Selectlabelframe, text='Parties', font=("arial", 10),
                                      background="#F0F7F4", variable=self.checkVarParty, onvalue="partyTable", offvalue="")
        self.CbxParties.grid(row=3, column=6, padx=(0, 0), pady=(0, 20))

        # button hover colour - search
        def on_enterSearch(e):
            btnSearchDate['background'] = "#57FFA5"

        def on_leaveSearch(e):
            btnSearchDate['background'] = "snow"

        # button search
        btnSearchDate = Button(self.Selectlabelframe, text="Search",
                               width=13, height=2, background="snow", font=("arial", 10), command=lambda :Gui.viewbookinglogic.Search(self.master2))
        btnSearchDate.grid(row=3, column=8, pady=(0, 20), padx=(8, 15))
        btnSearchDate.bind("<Enter>", on_enterSearch)
        btnSearchDate.bind("<Leave>", on_leaveSearch)


        # labelframe for additional info box
        self.labelframe = LabelFrame(self.parent, text="Additional Information", width=324, height=167,
                                     background="#70ABAF", font=("arial", 9, "bold"))
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
        self.lblNoofGuests = Label(self.labelframe, text="No of Guests: ", background="#70ABAF")
        self.lblNoofGuests.grid(row=1, column=1)
        self.lblDisNoofGuests = Label(self.labelframe, text='10', background="#70ABAF")
        self.lblDisNoofGuests.grid(row=1, column=2)

        # labels for Address in additional details label frame
        self.lblAddress = Label(self.labelframe, text="Address: ", background="#70ABAF")
        self.lblAddress.grid(row=2, column=1)
        self.lblDisAddress = Label(self.labelframe, text='SERC', background="#70ABAF")
        self.lblDisAddress.grid(row=2, column=2)

        # labels for Date of Booking in additional details label frame
        self.lblDateofBooking = Label(self.labelframe, text="Date of Booking: ", background="#70ABAF")
        self.lblDateofBooking.grid(row=3, column=1)
        self.lblDisDateofBooking = Label(self.labelframe, text='10/10/2010', background="#70ABAF")
        self.lblDisDateofBooking.grid(row=3, column=2)

        # labels for Cost Per Head in additional details label frame
        self.lblCostPerHead = Label(self.labelframe, text="Cost Per Head: ", background="#70ABAF")
        self.lblCostPerHead.grid(row=4, column=1)
        self.lblDisCostPerHead = Label(self.labelframe, text='30', background="#70ABAF")
        self.lblDisCostPerHead.grid(row=4, column=2)

        # labels for Band Name in additional details label frame
        self.lblBandName = Label(self.labelframe, text="Band Name: ", background="#70ABAF")
        self.lblBandName.grid(row=5, column=1)
        self.lblDisBandName = Label(self.labelframe, text='Prawn Mendes', background="#70ABAF")
        self.lblDisBandName.grid(row=5, column=2)

        # labels for Band Price in additional details label frame
        self.lblBandPrice = Label(self.labelframe, text="Band Price: ", background="#70ABAF")
        self.lblBandPrice.grid(row=6, column=1)
        self.lblDisBandPrice = Label(self.labelframe, text='£250', background="#70ABAF")
        self.lblDisBandPrice.grid(row=6, column=2)

        # labels for number of bedrooms reserved in additional details label frame
        self.lblNoOfBedsReserved = Label(self.labelframe, text="No. of Bedrooms Reserved: ", background="#70ABAF")
        self.lblNoOfBedsReserved.grid(row=7, column=1)
        self.lblDisNoOfBedsReserved = Label(self.labelframe, text='5', background="#70ABAF")
        self.lblDisNoOfBedsReserved.grid(row=7, column=2)

        # labels for Company Name in additional details label frame
        self.lblCompanyName = Label(self.labelframe, text="Company Name ", background="#70ABAF")
        self.lblCompanyName.grid(row=5, column=1)
        self.lblDisCompanyName = Label(self.labelframe, text='SERC', background="#70ABAF")
        self.lblDisCompanyName.grid(row=5, column=2)

        # labels for Number of Days in additional details label frame
        self.lblNumberofDays = Label(self.labelframe, text="Number of Days: ", background="#70ABAF")
        self.lblNumberofDays.grid(row=6, column=1)
        self.lblDisNumberofDays = Label(self.labelframe, text='5', background="#70ABAF")
        self.lblDisNumberofDays.grid(row=6, column=2)

        # labels for projector required in additional details label frame
        self.lblProjectorRequired = Label(self.labelframe, text="Projector Required: ", background="#70ABAF")
        self.lblProjectorRequired.grid(row=7, column=1)
        self.lblDisProjectorRequired = Label(self.labelframe, text='Yes', background="#70ABAF")
        self.lblDisProjectorRequired.grid(row=7, column=2)

        # setting weight for rows and columns
        self.labelframe.grid_rowconfigure(0, weight=1)
        self.labelframe.grid_rowconfigure(3, weight=1)
        self.labelframe.grid_columnconfigure(0, weight=1)
        self.labelframe.grid_columnconfigure(3, weight=1)


        # labelframe for price breakdown
        self.Totallabelframe = LabelFrame(self.parent, text="Price Breakdown", width=324, height=100,
                                          background="#70ABAF", font=("arial", 9, "bold"))
        self.Totallabelframe.grid(row=1, column=7, columnspan=3, padx=(10, 20), pady=(0, 20))
#70ABAF # columns
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
        self.lblGuestPrice = Label(self.Totallabelframe, text="Guests: ", background="#70ABAF")
        self.lblGuestPrice.grid(row=1, column=1)
        self.lblDisGuestPrice = Label(self.Totallabelframe, text='£', background="#70ABAF")
        self.lblDisGuestPrice.grid(row=1, column=2)

        # Label for band price
        self.lblBandCost = Label(self.Totallabelframe, text="Band: ", background="#70ABAF")
        self.lblBandCost.grid(row=1, column=3)
        self.lblDisBandCost = Label(self.Totallabelframe, text="£", background="#70ABAF")
        self.lblDisBandCost.grid(row=1, column=4)

        # Label for sub total
        self.lblSubTotal = Label(self.Totallabelframe, text="Sub Total: ", background="#70ABAF")
        self.lblSubTotal.grid(row=2, column=1)
        self.lblDisSubTotal = Label(self.Totallabelframe, text="£", background="#70ABAF")
        self.lblDisSubTotal.grid(row=2, column=2)

        # Label for VAT
        self.lblVat = Label(self.Totallabelframe, text="VAT: ", background="#70ABAF")
        self.lblVat.grid(row=3, column=1)
        self.lblDisVat = Label(self.Totallabelframe, text="£", background="#70ABAF")
        self.lblDisVat.grid(row=3, column=2)

        # Label for total
        self.lblTotal = Label(self.Totallabelframe, text="Total: ", background="#70ABAF")
        self.lblTotal.grid(row=4, column=1)
        self.lblDisTotal = Label(self.Totallabelframe, text="£", background="#70ABAF")
        self.lblDisTotal.grid(row=4, column=2)

        self.btninvoice = Button(self.Totallabelframe, text="Save Invoice", command=lambda :Gui.viewbookinglogic.Invoice(self.master2))
        self.btninvoice.grid(row=3, column=3, rowspan=2, columnspan=2)

        # setting weight for rows and columns
        self.Totallabelframe.grid_rowconfigure(0, weight=1)
        self.Totallabelframe.grid_rowconfigure(3, weight=1)
        self.Totallabelframe.grid_columnconfigure(0, weight=1)
        self.Totallabelframe.grid_columnconfigure(3, weight=1)

        # method calls
        self.master2 = self
        Gui.viewbookinglogic.loadData(self.master2)
        Gui.viewbookinglogic.CalIncome(self.master2)
        Gui.viewbookinglogic.removeAllLabels(self.master2)
        Gui.viewbookinglogic.unSelectItem(self.master2)