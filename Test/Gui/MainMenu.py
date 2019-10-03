"""Module contains class used to create main menu UI and functions used to open other forms from the main menu"""

from tkinter import *
from Gui import viewbooking
import Gui.CreateWeddingForm
import Gui.CreatePartyForm
import Gui.CreateConferenceForm
import Gui.viewbooking


# Functions to call various pop-ups
def call_wedding_popup():
    """function used to open create wedding form"""
    top = Toplevel()
    Gui.CreateWeddingForm.BookWedding(top)
    top.grab_set()
    top.wait_window()
    top.destroy()


def call_party_popup():
    """function used to open create party form"""
    top = Toplevel()
    Gui.CreatePartyForm.BookParty(top)
    top.grab_set()
    top.wait_window()
    top.destroy()


def call_conference_popup():
    """function used to open create conference form"""
    top = Toplevel()
    Gui.CreateConferenceForm.BookConference(top)
    top.grab_set()
    top.wait_window()
    top.destroy()


def call_viewbookings_popup():
    """function used to open viewbookings form form"""
    top = Toplevel()
    Gui.viewbooking.FrmViewBooking(top)
    top.grab_set()
    top.wait_window()
    top.destroy()


class MainMenu:
    """Main menu UI of application used to access all other forms in application"""
    def __init__(self):
        # creates form, removes maximise button on form, adds form title and adds background colour
        self.main_menu = Tk()
        self.main_menu.resizable(0, 0)
        self.main_menu.title("Hotel Booking System - Main Menu")
        self.main_menu.config(background="#70ABAF")

        # button hover colour - wedding
        def on_enter_wedding():
            btn_book_wedding['background'] = "aquamarine4"

        def on_leave_wedding():
            btn_book_wedding['background'] = "medium aquamarine"

        # button hover colour - party
        def on_enter_party():
            btn_book_party['background'] = "aquamarine4"

        def on_leave_party():
            btn_book_party['background'] = "medium aquamarine"

        # button hover colour - conference
        def on_enter_conference():
            btn_book_conference['background'] = "aquamarine4"

        def on_leave_conference():
            btn_book_conference['background'] = "medium aquamarine"

        # button hover colour - view bookings
        def on_enter_view_bookings():
            btn_view_bookings['background'] = "aquamarine4"

        def on_leave_view_bookings():
            btn_view_bookings['background'] = "medium aquamarine"

        # adding UI elements to the form
        # Main menu Title

        Label(self.main_menu, text="Welcome", font=("arial", 30, "bold", "underline",), bg="#70ABAF") \
            .grid(row=0, pady=(25, 0), padx=(10, 10))
        Label(self.main_menu, text="Please select what you would like to do today", font=("arial", 14), bg="#70ABAF")\
            .grid(row=1, pady=(25, 0), padx=(10, 10))

        # Main menu buttons with styling that redirect to our other windows
        btn_book_wedding = Button(self.main_menu, text="Add Wedding Booking", font=("arial", 12, "bold"),
                                  width=30, height=4, bg="medium aquamarine", command=call_wedding_popup)
        btn_book_wedding.bind("<Enter>", lambda e: on_enter_wedding())
        btn_book_wedding.bind("<Leave>", lambda e: on_leave_wedding())
        btn_book_party = Button(self.main_menu, text="Add Party Booking", font=("arial", 12, "bold"),
                                width=30, height=4, bg="medium aquamarine", command=call_party_popup)
        btn_book_party.bind("<Enter>", lambda e: on_enter_party())
        btn_book_party.bind("<Leave>", lambda e: on_leave_party())
        btn_book_conference = Button(self.main_menu, text="Add Conference Booking", font=("arial", 12, "bold"),
                                     width=30, height=4, bg="medium aquamarine", command=call_conference_popup)
        btn_book_conference.bind("<Enter>", lambda e: on_enter_conference())
        btn_book_conference.bind("<Leave>", lambda e: on_leave_conference())
        btn_view_bookings = Button(self.main_menu, text="View, edit and delete Bookings", font=("arial", 12, "bold"),
                                   width=30, height=4, bg="medium aquamarine", command=call_viewbookings_popup)
        btn_view_bookings.bind("<Enter>", lambda e: on_enter_view_bookings())
        btn_view_bookings.bind("<Leave>", lambda e: on_leave_view_bookings())

        # Main menu buttons being placed using grid layout
        btn_book_wedding.grid(row=2, column=0, pady=(25, 5))
        btn_book_party.grid(row=3, column=0, pady=(25, 5))
        btn_book_conference.grid(row=4, column=0, pady=(25, 5))
        btn_view_bookings.grid(row=5, column=0, pady=(25, 25))

        # calling the main menu loop
        self.main_menu.mainloop()
