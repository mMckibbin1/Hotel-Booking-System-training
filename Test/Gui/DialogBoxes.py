from tkinter import *
from tkinter.messagebox import *
from Gui import viewbookinglogic


class Delete:
    def __init__(self, vbself):
        if askyesno('Delete', 'Do you want to delete this booking?'):
            viewbookinglogic.delete_data(vbself)
            showinfo('Yes', 'Booking Deleted')
        else:
            showinfo('No', 'Booking Not Deleted')


class Update:
    def __init__(self):
        if askyesno('Save Changes', 'Do you want to save changes to this booking?'):
            showinfo('Yes', 'Changes Saved')
        else:
            showinfo('No', 'Changes Not Saved')


# B1 = Button(top, text="Delete Booking", command=delete)
# B1.place(x=50, y=50)
#
# B2 = Button(top, text="Update Booking", command=update)
# B2.place(x=50, y=100)
#
# top.mainloop()