from tkinter.messagebox import *
from Gui import viewbookinglogic

# classes to display and accept response from a dialog box
class Delete:
    # dialog to confirm that user wants to delete booking from database
    def __init__(self, vbself):
        if askyesno('Delete', 'Do you want to delete this booking?'):
            viewbookinglogic.delete_data(vbself)
            showinfo('Yes', 'Booking Deleted')
        else:
            showinfo('No', 'Booking Not Deleted')

class Update:
    # dialog to confirm user wants to save changes made to booking when updating info
    def __init__(self):
        if askyesno('Save Changes', 'Do you want to save changes to this booking?'):
            showinfo('Yes', 'Changes Saved')
        else:
            showinfo('No', 'Changes Not Saved')