"""Module contains function for different dialog boxes used in the program"""

from tkinter.messagebox import *
from Gui import viewbookinglogic
from tkinter import messagebox


def delete(master):
    """calls dialog box for delete function"""
    # dialog box pops up
    if askyesno('Delete', 'Do you want to delete this booking?', parent=master):
        return True
    else:
        # informs user that booking is not deleted
        showinfo('Not Deleted', 'Booking Not Deleted', parent=master)
        return False


# updated dialog message box
def updated(self, master, view_booking):
    """calls dialog box for update function"""
    messagebox.showinfo("Successful", "These details have been changed!", parent=master)
    viewbookinglogic.refresh_data(master=view_booking)


# not saved dialog message box
def not_saved(master):
    """calls dialog box when details aren't saved"""
    messagebox.showinfo("Aborted", "Action cancelled, no details have been saved!", parent=master)


# saved dialog message box
def saved(master):
    """calls dialog box when details are saved"""
    messagebox.showinfo("Successful", "These details have been successfully saved!", parent=master)


# prompt for user to select a row
def select_row(master):
    """calls dialog box when user hasn't selected a row"""
    messagebox.showinfo("Nothing Selected", "Please Select a Row first!", parent=master)
