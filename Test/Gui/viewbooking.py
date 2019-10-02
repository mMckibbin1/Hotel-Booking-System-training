from tkinter import *
import tkinter as Tkinter
import tkinter.ttk as ttk
from Gui import viewbookinglogic
import Gui.viewbookinglogic


class FrmViewBooking(Tkinter.Frame):
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

        # Set the tree view
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
        self.tree.bind('<ButtonRelease-1>', lambda e: Gui.viewbookinglogic.select_item(e, self))
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
        ttk.Label(self.parent, text="Total Income",
                  font=("arial", 10, "bold"), background="#70ABAF").grid(row=2, column=5, sticky="se", padx=(10, 10))

        self.lblTotalIncome = Label(self.parent, text="£0", font=("arial", 10, "bold"), background="#70ABAF")
        self.lblTotalIncome.grid(row=2, column=6, sticky="sw", padx=(0, 55))

        # BUTTONS #
        # button hover colour - update
        def on_enter_update(e):
            btnUpdate['background'] = "snow2"  # "#F0F704"

        def on_leave_update(e):
            btnUpdate['background'] = "snow"

        # button hover colour - delete
        def on_enter_delete(e):
            btnDelete['background'] = "tomato"

        def on_leave_delete(e):
            btnDelete['background'] = "snow"

        # button hover colour - refresh
        def on_enter_refresh(e):
            btnRefresh['background'] = "snow2"  # "#42A2FF"

        def on_leave_refresh(e):
            btnRefresh['background'] = "snow"

        # button hover colour - clear
        def on_enter_clear(e):
            self.btn_clear_date['background'] = "snow2"

        def on_leave_clear(e):
            self.btn_clear_date['background'] = "snow"

        # button update
        btnUpdate = Button(self.parent, text="Update Selected Booking", width=20, height=2, background="snow",
                           font=("arial", 10),
                           command=lambda: Gui.viewbookinglogic.update_selected(self.master2, self.master))
        btnUpdate.grid(row=3, column=7, sticky="ne", pady=(0, 20))
        btnUpdate.bind("<Enter>", on_enter_update)
        btnUpdate.bind("<Leave>", on_leave_update)

        # button delete
        btnDelete = Button(self.parent, text="Delete Selected Booking", width=20, height=2, background="snow",
                           font=("arial", 10),
                           command=lambda: viewbookinglogic.is_row_selected_delete(self, self.master2))
        btnDelete.grid(row=3, column=8, sticky="ne", pady=(0, 20))
        btnDelete.bind("<Enter>", on_enter_delete)
        btnDelete.bind("<Leave>", on_leave_delete)

        # button refresh
        btnRefresh = Button(self.parent, text="Refresh table", width=13, height=2, background="snow",
                            font=("arial", 10),
                            command=lambda: Gui.viewbookinglogic.refresh_data(self.master2))
        btnRefresh.grid(row=3, column=0, sticky="nw", pady=(0, 20), padx=(10, 0))
        btnRefresh.bind("<Enter>", on_enter_refresh)
        btnRefresh.bind("<Leave>", on_leave_refresh)

        # LABELFRAMES #
        # labelframe for select date
        self.SelectLabelFrame = LabelFrame(self.parent, width=305, height=167)
        self.SelectLabelFrame.grid(row=4, column=0, columnspan=12, sticky="ew", )
        self.SelectLabelFrame.config(background="#F0F7F4")

        # columns
        self.SelectLabelFrame.grid_columnconfigure(1, minsize=50)
        self.SelectLabelFrame.grid_columnconfigure(2, minsize=50)
        self.SelectLabelFrame.grid_columnconfigure(3, minsize=50)
        self.SelectLabelFrame.grid_columnconfigure(4, minsize=50)
        self.SelectLabelFrame.grid_columnconfigure(5, minsize=50)
        self.SelectLabelFrame.grid_columnconfigure(6, minsize=50)
        self.SelectLabelFrame.grid_columnconfigure(7, minsize=50)

        # rows
        self.SelectLabelFrame.grid_rowconfigure(1, minsize=20)
        self.SelectLabelFrame.grid_rowconfigure(2, minsize=20)
        self.SelectLabelFrame.grid_rowconfigure(3, minsize=20)

        # Search for dates
        ttk.Label(self.SelectLabelFrame, text="Search by date", font=("arial", 11, "bold"), background="#F0F7F4")\
            .grid(row=2, column=0, sticky=W, columnspan=1, padx=10, pady=(0, 5))

        self.display_start_date = StringVar()
        self.EntStartDate = ttk.Entry(self.SelectLabelFrame, font=("arial", 10), width=30,
                                      textvariable=self.display_start_date, state="readonly")
        self.EntStartDate.grid(row=3, column=0, sticky="ew", padx=10, columnspan=1, pady=(0, 20))
        self.EntStartDate.bind("<Button-1>", lambda event: Gui.viewbookinglogic.calendar_popup(event, "EntStartDate",
                                                                                               self.master2, master))

        ttk.Label(self.SelectLabelFrame, text="To", font=("arial", 10, "bold"),
                  background="#F0F7F4").grid(row=3, column=1, pady=(0, 20))

        self.display_end_date = StringVar()
        self.EntEndDate = ttk.Entry(self.SelectLabelFrame, font=("arial", 10), width=30,
                                    textvariable=self.display_end_date, state="readonly")
        self.EntEndDate.grid(row=3, column=2, sticky="ew", padx=10, columnspan=1, pady=(0, 20))
        self.EntEndDate.bind("<Button-1>", lambda event: Gui.viewbookinglogic.calendar_popup(event, "EntEndDate",
                                                                                             self.master2, master))
        self.data = {}
        self.btn_clear_date = Button(self.SelectLabelFrame, text="Clear Dates", width=13, height=2, background="snow",
                                     font=("arial", 10), command=lambda: Gui.viewbookinglogic.clear_date(self.master2))
        self.btn_clear_date.grid(row=4, column=0, sticky="ew", padx=10, columnspan=1, pady=(0, 20))
        self.btn_clear_date.bind("<Enter>", on_enter_clear)
        self.btn_clear_date.bind("<Leave>", on_leave_clear)

        # check boxes

        self.checkVarWedding = StringVar()
        self.checkVarConference = StringVar()
        self.checkVarParty = StringVar()

        self.CbxWedding = Checkbutton(self.SelectLabelFrame, text='Weddings', variable=self.checkVarWedding,
                                      onvalue="weddingTable", offvalue="", font=("arial", 10), background="#F0F7F4")
        self.CbxWedding.grid(row=3, column=4, padx=(0, 20), sticky=W, pady=(0, 20))
        self.CbxWedding.select()

        self.CbxConference = Checkbutton(self.SelectLabelFrame, text='Conference', font=("arial", 10),
                                         background="#F0F7F4", variable=self.checkVarConference,
                                         onvalue="conferenceTable", offvalue="")
        self.CbxConference.grid(row=3, column=5, padx=(0, 20), pady=(0, 20))
        self.CbxConference.select()

        self.CbxParties = Checkbutton(self.SelectLabelFrame, text='Parties', font=("arial", 10),
                                      background="#F0F7F4", variable=self.checkVarParty,
                                      onvalue="partyTable", offvalue="")
        self.CbxParties.grid(row=3, column=6, padx=(0, 0), pady=(0, 20))
        self.CbxParties.select()

        # button hover colour - search
        def on_enter_search(e):
            btnSearchDate['background'] = "snow2"  # "#57FFA5"

        def on_leave_search(e):
            btnSearchDate['background'] = "snow"

        # button hover colour - main menu
        def on_enter_main_menu(e):
            btn_main_menu['background'] = "snow2"  # "#57FFA5"

        def on_leave_main_menu(e):
            btn_main_menu['background'] = "snow"

        # button search
        btnSearchDate = Button(self.SelectLabelFrame, text="Search",
                               width=13, height=2, background="snow", font=("arial", 10),
                               command=lambda: Gui.viewbookinglogic.search(self.master2))
        btnSearchDate.grid(row=3, column=8, pady=(0, 20), padx=(8, 15))
        btnSearchDate.bind("<Enter>", on_enter_search)
        btnSearchDate.bind("<Leave>", on_leave_search)

        btn_main_menu = Button(self.SelectLabelFrame, text="Main Menu", width=13, height=2, background="snow",
                               font=("arial", 10), command=lambda: self.master.destroy())
        btn_main_menu.grid(row=4, column=8, pady=(0, 20), padx=(8, 15), sticky="WE")
        btn_main_menu.bind("<Enter>", on_enter_main_menu)
        btn_main_menu.bind("<Leave>", on_leave_main_menu)

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
        self.lblNoOfGuests = Label(self.labelframe, text="No of Guests: ", background="#70ABAF")
        self.lblNoOfGuests.grid(row=1, column=1)
        self.lblDisNoOfGuests = Label(self.labelframe, text='10', background="#70ABAF")
        self.lblDisNoOfGuests.grid(row=1, column=2)

        # labels for Address in additional details label frame
        self.lblAddress = Label(self.labelframe, text="Address: ", background="#70ABAF")
        self.lblAddress.grid(row=2, column=1)
        self.lblDisAddress = Label(self.labelframe, text='SERC', background="#70ABAF", width=22)
        self.lblDisAddress.grid(row=2, column=2)

        # labels for Date of Booking in additional details label frame
        self.lblDateOfBooking = Label(self.labelframe, text="Date of Booking: ", background="#70ABAF")
        self.lblDateOfBooking.grid(row=3, column=1)
        self.lblDisDateOfBooking = Label(self.labelframe, text='10/10/2010', background="#70ABAF")
        self.lblDisDateOfBooking.grid(row=3, column=2)

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
        self.lblCompanyName = Label(self.labelframe, text="Company Name: ", background="#70ABAF")
        self.lblCompanyName.grid(row=5, column=1)
        self.lblDisCompanyName = Label(self.labelframe, text='SERC', background="#70ABAF")
        self.lblDisCompanyName.grid(row=5, column=2)

        # labels for Number of Days in additional details label frame
        self.lblNumberOfDays = Label(self.labelframe, text="Number of Days: ", background="#70ABAF")
        self.lblNumberOfDays.grid(row=6, column=1)
        self.lblDisNumberOfDays = Label(self.labelframe, text='5', background="#70ABAF")
        self.lblDisNumberOfDays.grid(row=6, column=2)

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
        self.TotalLabelFrame = LabelFrame(self.parent, text="Price Breakdown", width=324, height=100,
                                          background="#70ABAF", font=("arial", 9, "bold"))
        self.TotalLabelFrame.grid(row=1, column=7, columnspan=3, padx=(10, 20), pady=(0, 20))

        # columns
        self.TotalLabelFrame.grid_columnconfigure(1, minsize=80)
        self.TotalLabelFrame.grid_columnconfigure(2, minsize=80)
        self.TotalLabelFrame.grid_columnconfigure(3, minsize=80)
        self.TotalLabelFrame.grid_columnconfigure(4, minsize=80)

        # rows
        self.TotalLabelFrame.grid_rowconfigure(1, minsize=20)
        self.TotalLabelFrame.grid_rowconfigure(2, minsize=20)
        self.TotalLabelFrame.grid_rowconfigure(3, minsize=20)
        self.TotalLabelFrame.grid_rowconfigure(4, minsize=20)

        # label for guest price
        self.lblGuestPrice = Label(self.TotalLabelFrame, text="Guests: ", background="#70ABAF")
        self.lblGuestPrice.grid(row=1, column=1)
        self.lblDisGuestPrice = Label(self.TotalLabelFrame, text='£', background="#70ABAF")
        self.lblDisGuestPrice.grid(row=1, column=2)

        # Label for band price
        self.lblBandCost = Label(self.TotalLabelFrame, text="Band: ", background="#70ABAF")
        self.lblBandCost.grid(row=1, column=3)
        self.lblDisBandCost = Label(self.TotalLabelFrame, text="£", background="#70ABAF")
        self.lblDisBandCost.grid(row=1, column=4)

        # Label for sub total
        self.lblSubTotal = Label(self.TotalLabelFrame, text="Sub Total: ", background="#70ABAF")
        self.lblSubTotal.grid(row=2, column=1)
        self.lblDisSubTotal = Label(self.TotalLabelFrame, text="£", background="#70ABAF")
        self.lblDisSubTotal.grid(row=2, column=2)

        # Label for VAT
        self.lblVat = Label(self.TotalLabelFrame, text="VAT: ", background="#70ABAF")
        self.lblVat.grid(row=3, column=1)
        self.lblDisVat = Label(self.TotalLabelFrame, text="£", background="#70ABAF")
        self.lblDisVat.grid(row=3, column=2)

        # Label for total
        self.lblTotal = Label(self.TotalLabelFrame, text="Total: ", background="#70ABAF")
        self.lblTotal.grid(row=4, column=1)
        self.lblDisTotal = Label(self.TotalLabelFrame, text="£", background="#70ABAF")
        self.lblDisTotal.grid(row=4, column=2)

        # button hover colour - invoice
        def on_enter_save_invoice(e):
            self.btnInvoice['background'] = "snow2"

        def on_leave_save_invoice(e):
            self.btnInvoice['background'] = "snow"

        self.btnInvoice = Button(self.TotalLabelFrame, text="Save Invoice",
                                 command=lambda: Gui.viewbookinglogic.invoice(self.master2))
        self.btnInvoice.grid(row=3, column=3, rowspan=2, columnspan=2)
        self.btnInvoice.bind("<Enter>", on_enter_save_invoice)
        self.btnInvoice.bind("<Leave>", on_leave_save_invoice)

        # setting weight for rows and columns
        self.TotalLabelFrame.grid_rowconfigure(0, weight=1)
        self.TotalLabelFrame.grid_rowconfigure(3, weight=1)
        self.TotalLabelFrame.grid_columnconfigure(0, weight=1)
        self.TotalLabelFrame.grid_columnconfigure(3, weight=1)

        # method calls
        self.master2 = self
        Gui.viewbookinglogic.load_data(self.master2)
        Gui.viewbookinglogic.cal_income(self.master2)
        Gui.viewbookinglogic.remove_all_labels(self.master2)
        Gui.viewbookinglogic.select_first_row_(self.master2)
