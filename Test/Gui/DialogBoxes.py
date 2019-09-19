from tkinter.messagebox import *
from Gui import viewbookinglogic
from tkinter import messagebox



# delete dialog box
# classes to display and accept response from a dialog box
class Delete:
    # dialog to confirm that user wants to delete booking from database
    def __init__(self, vbself):


                # dialog box pops up
                if askyesno('Delete', 'Do you want to delete this booking?'):
                    # deletes booking
                    viewbookinglogic.delete_data(vbself)
                    # informs user that booking is deleted
                    showinfo('Yes', 'Booking Deleted')

                else:
                    # informs user that booking is not deleted
                    showinfo('No', 'Booking Not Deleted')



# updated dialog message box
def updated(self):
 messagebox.showinfo("Successful", "These details have been changed!")

# not saved dialog message box
def not_saved(self):
    messagebox.showinfo("Aborted", "Action canceled, no details have been saved!")

# saved dialog message box
def saved(self):
    messagebox.showinfo("Successful", "These details have been successfully saved!")

# table refreshed dialog message box
def table_refreshed():
    messagebox.showinfo("Successful", "The table has been refreshed and is now up to date.")

#promt for user to select a row
def select_row():
    messagebox.showinfo("Nothing Selected", "Please Select a Row first!")

