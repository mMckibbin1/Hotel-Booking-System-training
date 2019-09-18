from tkinter import *
from Gui import viewbooking
import Gui.CreateWeddingForm
import Gui.CreatePartyForm
import Gui.CreateConferenceForm
import Gui.viewbooking


#Functions to call various pop-ups
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

# Main menu of applIction used to access all other forms
class mainMenu:
    def __init__(self):
        # creates form, removes maximise button on form, adds form title and adds background colour
        main_menu = Tk()
        main_menu.resizable(0, 0)
        main_menu.title("Main Menu")
        main_menu.config(background="powder blue")

        #adding UI elements to the form

        #Main menu Title

        Label(main_menu, text="Please select what you would like to do...",font=("arial",15,"bold"), bg="powder blue")\
            .grid(row=0, pady=(25, 0), padx=(10,10))

        #Main menu buttons with styling that redirect to our other windows
        btnbookWedding = Button(main_menu, text="Add wedding Booking", width=23, bg="medium aquamarine",command=call_wedding_popup)
        btnbookParty = Button(main_menu, text="Add Party Booking", width=23, bg="medium aquamarine", command=call_party_popup)
        btnbookConference = Button(main_menu, text="Add Conference Booking", width=23, bg="medium aquamarine",command=call_conference_popup)
        btnviewbookings = Button(main_menu, text="View, edit and delete Bookings", width=23, bg="medium aquamarine", command=call_viewBookings_popup)

        #Main menu buttons being placed using grid layout
        btnbookWedding.grid(row=1, column=0, pady=(25, 5))
        btnbookParty.grid(row=2, column=0, pady=(25, 5))
        btnbookConference.grid(row=3, column=0, pady=(25, 5))
        btnviewbookings.grid(row=4, column=0, pady=(25, 25))

        #calling the main menu loop
        main_menu.mainloop()