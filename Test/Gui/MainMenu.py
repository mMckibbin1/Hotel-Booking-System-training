from tkinter import *
from Gui import viewbooking
import Gui.CreateWeddingForm
import Gui.CreatePartyForm
import Gui.CreateConferenceForm
import Gui.viewbooking


# Functions to call various pop-ups
def call_wedding_popup():
    top = Toplevel()
    ui = Gui.CreateWeddingForm.BookWedding(top)
    top.grab_set()
    top.wait_window()
    top.destroy()


def call_party_popup():
    top = Toplevel()
    ui = Gui.CreatePartyForm.BookParty(top)
    top.grab_set()
    top.wait_window()
    top.destroy()


def call_conference_popup():
    top = Toplevel()
    ui = Gui.CreateConferenceForm.BookConference(top)
    top.grab_set()
    top.wait_window()
    top.destroy()


def call_viewBookings_popup():
    top = Toplevel()
    ui = Gui.viewbooking.FrmViewBooking(top)
    top.grab_set()
    top.wait_window()
    top.destroy()


##########################################       MAIN MENU      ###################################################

# Main menu of application used to access all other forms
class MainMenu:
    def __init__(self):
        # creates form, removes maximise button on form, adds form title and adds background colour
        self.main_menu = Tk()
        self.main_menu.resizable(0, 0)
        self.main_menu.title("Hotel Booking System - Main Menu")
        self.main_menu.config(background="#70ABAF")

        # button hover colour - wedding
        def on_enter_wedding(e):
            btnBookWedding['background'] = "aquamarine4"

        def on_leave_wedding(e):
            btnBookWedding['background'] = "medium aquamarine"

        # button hover colour - party
        def on_enter_party(e):
            btnBookParty['background'] = "aquamarine4"

        def on_leave_party(e):
            btnBookParty['background'] = "medium aquamarine"

        # button hover colour - conference
        def on_enter_conference(e):
            btnBookConference['background'] = "aquamarine4"

        def on_leave_conference(e):
            btnBookConference['background'] = "medium aquamarine"

        # button hover colour - view bookings
        def on_enter_view_bookings(e):
            btnViewBookings['background'] = "aquamarine4"

        def on_leave_view_bookings(e):
            btnViewBookings['background'] = "medium aquamarine"

        # adding UI elements to the form
        # Main menu Title

        Label(self.main_menu, text="Welcome", font=("arial", 30, "bold", "underline",), bg="#70ABAF") \
            .grid(row=0, pady=(25, 0), padx=(10, 10))
        Label(self.main_menu, text="Please select what you would like to do today", font=("arial", 14), bg="#70ABAF")\
            .grid(row=1, pady=(25, 0), padx=(10, 10))

        # Main menu buttons with styling that redirect to our other windows
        btnBookWedding = Button(self.main_menu, text="Add Wedding Booking", font=("arial", 12, "bold"),
                                width=30, height=4, bg="medium aquamarine", command=call_wedding_popup)
        btnBookWedding.bind("<Enter>", on_enter_wedding)
        btnBookWedding.bind("<Leave>", on_leave_wedding)
        btnBookParty = Button(self.main_menu, text="Add Party Booking", font=("arial", 12, "bold"),
                              width=30, height=4, bg="medium aquamarine", command=call_party_popup)
        btnBookParty.bind("<Enter>", on_enter_party)
        btnBookParty.bind("<Leave>", on_leave_party)
        btnBookConference = Button(self.main_menu, text="Add Conference Booking", font=("arial", 12, "bold"),
                                   width=30, height=4, bg="medium aquamarine", command=call_conference_popup)
        btnBookConference.bind("<Enter>", on_enter_conference)
        btnBookConference.bind("<Leave>", on_leave_conference)
        btnViewBookings = Button(self.main_menu, text="View, edit and delete Bookings", font=("arial", 12, "bold"),
                                 width=30, height=4, bg="medium aquamarine", command=call_viewBookings_popup)
        btnViewBookings.bind("<Enter>", on_enter_view_bookings)
        btnViewBookings.bind("<Leave>", on_leave_view_bookings)

        # Main menu buttons being placed using grid layout
        btnBookWedding.grid(row=2, column=0, pady=(25, 5))
        btnBookParty.grid(row=3, column=0, pady=(25, 5))
        btnBookConference.grid(row=4, column=0, pady=(25, 5))
        btnViewBookings.grid(row=5, column=0, pady=(25, 25))

        # calling the main menu loop
        self.main_menu.mainloop()
