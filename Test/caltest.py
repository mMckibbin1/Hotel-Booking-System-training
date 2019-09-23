import datetime
import tkinter
from tkinter.simpledialog import *
from tkinter import simpledialog
from tkcalendar import *


class cDemo:
    def __init__(self,e, master):
        top = Toplevel()
        self.master = top
        self.calendar = Calendar(top, mindate=datetime.datetime.now())
        self.calendar.grid()
        self.ok = Button(top, text='ok', command=lambda :self.okclick(master))
        self.ok.grid(row=1)

    def okclick(self,master):
        master.CalDateOfEvent.delete(0, 'end')
        master.CalDateOfEvent.insert([0], str(self.calendar.selection_get()))
        self.master.destroy()


# Demo code:
# def main():
#     root = tkinter.Tk()
#     root.wm_title("CalendarDialog Demo")
#     button = tkinter.Button(root, text="Click me to see a calendar!", command=demo)
#     button.pack()
#     root.mainloop()
#
# def demo():
#     top = Toplevel()
#     ui = cDemo(top)
#
# main()