from tkinter.messagebox import *
from Gui import viewbookinglogic


# delete dialog box
class Delete:
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


# update dialog box
class Update:
    def __init__(self):
        # dialog box pops up
        if askyesno('Save Changes', 'Do you want to save changes to this booking?'):
            # informs user that booking is updated
            showinfo('Yes', 'Changes Saved')
        else:
            # informs user that changes have not been saved
            showinfo('No', 'Changes Not Saved')

