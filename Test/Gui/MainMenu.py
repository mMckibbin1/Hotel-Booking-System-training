from tkinter import *
from Gui import viewbooking
import Gui.CreateWeddingForm
import Gui.CreatePartyForm
import Gui.CreateConferenceForm
import Gui.viewbooking

# # Functions to call various pop-ups
def call_wedding_popup():
    top = Toplevel()
    ui = Gui.CreateWeddingForm.bookwedding(top)
    top.grab_set()
    top.wait_window()
    top.destroy()

def call_party_popup():
    top = Toplevel()
    ui = Gui.CreatePartyForm.bookParty(top)
    top.grab_set()
    top.wait_window()
    top.destroy()

def call_conference_popup():
    top = Toplevel()
    ui = Gui.CreateConferenceForm.bookConference(top)
    top.grab_set()
    top.wait_window()
    top.destroy()

def call_viewBookings_popup():
    top = Toplevel()
    ui = Gui.viewbooking.frmViewBooking(top)
    top.grab_set()
    top.wait_window()
    top.destroy()



##########################################       MAIN MENU      ###################################################

# Main menu of application used to access all other forms
class mainMenu:
    def __init__(self):
        # creates form, removes maximise button on form, adds form title and adds background colour
        self.main_menu = Tk()
        self.main_menu.resizable(0, 0)
        self.main_menu.title("Hotel Booking System - Main Menu")
        self.main_menu.config(background="#70ABAF")


        # button hover colour - wedding
        def on_enterWedding(e):
            btnbookWedding['background'] = "aquamarine4"

        def on_leaveWedding(e):
            btnbookWedding['background'] = "medium aquamarine"

        # button hover colour - party
        def on_enterParty(e):
            btnbookParty['background'] = "aquamarine4"

        def on_leaveParty(e):
            btnbookParty['background'] = "medium aquamarine"

        # button hover colour - conference
        def on_enterConference(e):
            btnbookConference['background'] = "aquamarine4"

        def on_leaveConference(e):
            btnbookConference['background'] = "medium aquamarine"

        # button hover colour - view bookings
        def on_enterViewBookings(e):
            btnviewbookings['background'] = "aquamarine4"

        def on_leaveViewBookings(e):
            btnviewbookings['background'] = "medium aquamarine"

        # adding UI elements to the form

        # Main menu Title

        Label(self.main_menu, text="Welcome", font=("arial", 30, "bold","underline",), bg="#70ABAF") \
            .grid(row=0, pady=(25, 0), padx=(10, 10))
        Label(self.main_menu, text="Please select what you would like to do today",font=("arial",14), bg="#70ABAF")\
            .grid(row=1, pady=(25, 0), padx=(10,10))

        # Main menu buttons with styling that redirect to our other windows
        btnbookWedding = Button(self.main_menu, text="Add Wedding Booking", font=("arial", 12, "bold"), width=30,height=4, bg="medium aquamarine",
                                command=call_wedding_popup)
        btnbookWedding.bind("<Enter>", on_enterWedding)
        btnbookWedding.bind("<Leave>", on_leaveWedding)
        btnbookParty = Button(self.main_menu, text="Add Party Booking",font=("arial", 12, "bold"),  width=30,height=4, bg="medium aquamarine",
                              command=call_party_popup)
        btnbookParty.bind("<Enter>", on_enterParty)
        btnbookParty.bind("<Leave>", on_leaveParty)
        btnbookConference = Button(self.main_menu, text="Add Conference Booking",font=("arial", 12, "bold"),  width=30,height=4, bg="medium aquamarine",
                                   command=call_conference_popup)
        btnbookConference.bind("<Enter>", on_enterConference)
        btnbookConference.bind("<Leave>", on_leaveConference)
        btnviewbookings = Button(self.main_menu, text="View, edit and delete Bookings", font=("arial", 12, "bold"),width=30,height=4, bg="medium aquamarine",
                                 command=call_viewBookings_popup)
        btnviewbookings.bind("<Enter>", on_enterViewBookings)
        btnviewbookings.bind("<Leave>", on_leaveViewBookings)

        # Main menu buttons being placed using grid layout
        btnbookWedding.grid(row=2, column=0, pady=(25, 5))
        btnbookParty.grid(row=3, column=0, pady=(25, 5))
        btnbookConference.grid(row=4, column=0, pady=(25, 5))
        btnviewbookings.grid(row=5, column=0, pady=(25, 25))

        # calling the main menu loop
        self.main_menu.mainloop()