from tkinter import *


class CreateInvoiceDialog:
    # setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''

    def __init__(self, master):
        # Creation of wedding form set title, size ect..
        self.master = master
        self.master.title("Enter File name")
        self.master.resizable(0, 0)
        self.master.config(background="#70ABAF")

        self.lblHeading = Label(master, text="Save Invoice as:", font=("arial", 10, "bold"), bg="#70ABAF")
        self.lblHeading.pack(padx=(10,10), pady=(5,5))
        self.ent_file_name = Entry(master, font=("arial", 10), width=30)
        self.ent_file_name.pack(padx=(10,10), pady=(5,5))
        self.btn_Save = Button(master,text="Save")
        self.btn_Save.pack(padx=(10,10), pady=(5,5),side='left', anchor='n', fill='x',expand='yes')
        self.btn_cancel = Button(master, text="Cancel")
        self.btn_cancel.pack(padx=(10,10), pady=(5,5),side='right', anchor='n', fill='x',expand='yes')

        