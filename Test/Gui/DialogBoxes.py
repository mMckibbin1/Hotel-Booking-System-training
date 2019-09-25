from tkinter.messagebox import *
from Gui import viewbookinglogic
from tkinter import messagebox
import Gui.MainMenu


# delete dialog box
# classes to display and accept response from a dialog box
class Delete:
    # dialog to confirm that user wants to delete booking from database
    def __init__(self, vbself, master):

        # dialog box pops up
        if askyesno('Delete', 'Do you want to delete this booking?', parent=master):
            # deletes booking
            viewbookinglogic.delete_data(vbself)
            # informs user that booking is deleted
            showinfo('Yes', 'Booking Deleted', parent=master)
            viewbookinglogic.refresh_data(master=master)

        else:
            # informs user that booking is not deleted
            showinfo('No', 'Booking Not Deleted', parent=master)


# updated dialog message box
def updated(self, master, view_booking):
    messagebox.showinfo("Successful", "These details have been changed!", parent=master)
    viewbookinglogic.refresh_data(master=view_booking)


# not saved dialog message box
def not_saved(self):
    messagebox.showinfo("Aborted", "Action canceled, no details have been saved!", parent=self)


# saved dialog message box
def saved(self):
    messagebox.showinfo("Successful", "These details have been successfully saved!", parent=self)


# table refreshed dialog message box
def table_refreshed():
    messagebox.showinfo("Successful", "The table has been refreshed and is now up to date.")


# promt for user to select a row
def select_row(self):
    messagebox.showinfo("Nothing Selected", "Please Select a Row first!", parent=self)
