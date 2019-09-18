from Database import dbHelper
from Events import Wedding, Party, Conference
from tkinter import *
from Gui import DialogBoxes
from addtionalWidgets import CalendarWidget
from Gui import EditPartyForm, EditWeddingForm, EditConferenceForm

def call_update_wedding_popup(object):
    top = Toplevel()
    ui = EditWeddingForm.EditWedding(top, object)
    top.grab_set()
    top.wait_window()
    top.destroy()


def call_update_party_popup(object):
    top = Toplevel()
    ui = EditPartyForm.EditParty(top, object)
    top.grab_set()
    top.wait_window()
    top.destroy()


def call_update_conference_popup(object):
    top = Toplevel()
    ui = EditConferenceForm.EditConference(top, object)
    top.grab_set()
    top.wait_window()
    top.destroy()

def unSelectItem(a, self):
    self.treeview.selection_clear()
    self.removeAllLabels(self)


def Search(self):


    eventslist = []

    if self.checkVarWedding.get() != "":
        eventslist.append( self.checkVarWedding.get())
    if  self.checkVarParty.get() != "":
        eventslist.append(self.checkVarParty.get())
    if  self.checkVarConference.get() != "":
        eventslist.append( self.checkVarConference.get())

    dbHelper.search(eventslist, self.EntStartDate.get(), self.EntEndDate.get())

def update_selected(self):
    listofevents = []
    listofdb = dbHelper.read_all_from_db()
    # try:
    curItem = self.tree.focus()

    RowID = self.tree.item(curItem)['text']

    for value in self.tree.item(curItem)['values']:
        listofevents.append(value)

        types = listofevents[0]

    for list in listofdb:
        for object in list:
            if types == "Wedding":
                if type(object) == Wedding.Wedding:
                    if object.ID == RowID:
                        object = object
                        return call_update_wedding_popup(object)
            elif types == "Party":
                if type(object) == Party.Party:
                    if object.ID == RowID:
                        object = object
                        return call_update_party_popup(object)
            elif types == "Conference":
                if type(object) == Conference.Conference:
                    if object.ID == RowID:
                        object = object
                        print(object.noOfDays)
                        return call_update_conference_popup(object)


# selects item from treeview
def selectItem(a, self):
    listofevents = []
    listofdb = dbHelper.read_all_from_db()

    # sets the current item as the highlighted row in the treeview
    curItem = self.tree.focus()

    # sets the id
    RowID = self.tree.item(curItem)['text']

    # adds the values in the tree view to a list
    for value in self.tree.item(curItem)['values']:
        listofevents.append(value)

        types = listofevents[0]

    # changes the labels depending on the ID and event type
    for list in listofdb:
        for object in list:
            if types == "Wedding":
                if type(object) == Wedding.Wedding:
                    if object.ID == RowID:
                        return DetailsLabelChange(self, types, object)
            elif types == "Party":
                if type(object) == Party.Party:
                    if object.ID == RowID:
                        return DetailsLabelChange(self, types, object)
            elif types == "Conference":
                if type(object) == Conference.Conference:
                    if object.ID == RowID:
                        return DetailsLabelChange(self, types, object)


# functions to allow the labels to change in the additional info labelframe
# removes all labels stored within labelframe
def removeAllLabels(self):
    self.lblNoofGuests.grid_remove()
    self.lblDisNoofGuests.grid_remove()
    self.lblAddress.grid_remove()
    self.lblDisAddress.grid_remove()
    self.lblDateofBooking.grid_remove()
    self.lblDisDateofBooking.grid_remove()
    self.lblCostPerHead.grid_remove()
    self.lblDisCostPerHead.grid_remove()
    self.lblBandName.grid_remove()
    self.lblDisBandName.grid_remove()
    self.lblBandPrice.grid_remove()
    self.lblDisBandPrice.grid_remove()
    self.lblCompanyName.grid_remove()
    self.lblDisCompanyName.grid_remove()
    self.lblNumberofDays.grid_remove()
    self.lblDisNumberofDays.grid_remove()
    self.lblProjectorRequired.grid_remove()
    self.lblDisProjectorRequired.grid_remove()
    self.lblNoOfBedsReserved.grid_remove()
    self.lblDisNoOfBedsReserved.grid_remove()

    # label for guest price
    self.lblGuestPrice.grid_remove()
    self.lblDisGuestPrice.grid_remove()

    # Label for band price
    self.lblBandCost.grid_remove()
    self.lblDisBandCost.grid_remove()

    # Label for sub total
    self.lblSubTotal.grid_remove()
    self.lblDisSubTotal.grid_remove()

    # Label for VAT
    self.lblVat.grid_remove()
    self.lblDisVat.grid_remove()

    # Label for total
    self.lblTotal.grid_remove()
    self.lblDisTotal.grid_remove()


# adds the labels that are consistent throughout all event types
def addBaseLables(self, object):
    self.lblNoofGuests.grid()
    self.lblDisNoofGuests.grid()
    self.lblAddress.grid()
    self.lblDisAddress.grid()
    self.lblDateofBooking.grid()
    self.lblDisDateofBooking.grid()
    self.lblCostPerHead.grid()
    self.lblDisCostPerHead.grid()

    # additional info labels
    self.lblDisNoofGuests.config(text=object.noGuests)
    self.lblDisAddress.config(text=object.address)
    self.lblDisDateofBooking.config(text=object.dateOfBooking)
    self.lblDisCostPerHead.config(text=object.costPerHead)


# adds the labels that are used for weddings
def addWeddingLabels(self, object):
    addBaseLables(self, object)
    self.lblBandName.grid()
    self.lblDisBandName.grid()
    self.lblBandPrice.grid()
    self.lblDisBandPrice.grid()
    self.lblNoOfBedsReserved.grid()
    self.lblDisNoOfBedsReserved.grid()

    # additional info labels
    self.lblDisBandName.config(text=object.bandName)
    self.lblDisBandPrice.config(text=object.bandPrice)
    self.lblDisNoOfBedsReserved.config(text=object.noBedroomsReserved)


# adds the labels that are used for parties
def addPartyLabels(self, object):
    addBaseLables(self, object)
    self.lblBandName.grid()
    self.lblDisBandName.grid()
    self.lblBandPrice.grid()
    self.lblDisBandPrice.grid()

    # additional info labels
    self.lblDisBandName.config(text=object.bandName)
    self.lblDisBandPrice.config(text=object.bandPrice)


# adds the labels that are used for conferences
def addConferenceLables(self, object):
    addBaseLables(self, object)
    self.lblCompanyName.grid()
    self.lblDisCompanyName.grid()
    self.lblNumberofDays.grid()
    self.lblDisNumberofDays.grid()
    self.lblProjectorRequired.grid()
    self.lblDisProjectorRequired.grid()

    # additional info labels
    self.lblDisCompanyName.config(text=object.companyName)
    self.lblDisNumberofDays.config(text=object.noOfDays)
    self.lblDisProjectorRequired.config(text=object.projectorRequired)


# functions to allow the labels to change in the price breakdown labelframe
def updatePriceBreakdown(self, object):
    # Label for guest price
    self.lblDisGuestPrice.config(text=object.guestsCost())

    self.lblGuestPrice.grid()
    self.lblDisGuestPrice.grid()

    # Label for band price
    self.lblBandCost.grid()
    self.lblDisBandCost.grid()

    # Label for sub total
    self.lblSubTotal.grid()
    self.lblDisSubTotal.grid()

    # Label for VAT
    self.lblVat.grid()
    self.lblDisVat.grid()

    # Label for total
    self.lblTotal.grid()
    self.lblDisTotal.grid()

    # changes the labels if the event type is a conference
    if type(object) == Conference.Conference:
        self.lblBandCost.config(text="Cost Per Day:")
        self.lblDisBandCost.config(text=str(object.guestsCost()) + '   ( * ' + str(object.noOfDays) + " days)")
    else:
        self.lblBandCost.config(text="Band Price")
        self.lblDisBandCost.config(text=object.bandPrice)

    # labels for totals
    self.lblDisSubTotal.config(text=object.grosstotal())
    self.lblDisVat.config(text=object.VAT())
    self.lblDisTotal.config(text=object.netTotal())


# function to change the labels shown, depending on the event type selected in the treeview
def DetailsLabelChange(self, eventType, object):
    if eventType == 'Wedding':
        removeAllLabels(self)
        addWeddingLabels(self, object)
        updatePriceBreakdown(self, object)

    elif eventType == 'Party':
        removeAllLabels(self)
        addPartyLabels(self, object)
        updatePriceBreakdown(self, object)

    elif eventType == 'Conference':
        removeAllLabels(self)
        addConferenceLables(self, object)
        updatePriceBreakdown(self, object)

    else:
        removeAllLabels(self)


# calculates the total income
def CalIncome(master):
    totalIncome = 0.0
    # adds up the values in the total cost column
    for child in master.treeview.get_children():
        totalIncome += float(master.treeview.item(child, "values")[5])
        master.lblTotalIncome.config(text=totalIncome)


# function to reload the table
def refreshData(master):
    master.treeview.delete(*master.treeview.get_children())
    loadData(master)
    CalIncome(master)


# function to load the data from the database into the table
def loadData(master):

    datalist = dbHelper.read_all_from_db()

    for list in datalist:
        for object in list:
            if type(object) == Wedding.Wedding:
                insert_data(master, object.ID, "Wedding", object.nameOfContact,
                                           object.contactNo, object.dateOfEvent, object.eventRoomNo,
                                           object.netTotal())
            elif type(object) == Party.Party:
                insert_data(master, object.ID, "Party", object.nameOfContact,
                            object.contactNo, object.dateOfEvent, object.eventRoomNo,
                            object.netTotal())
            elif type(object) == Conference.Conference:
                insert_data(master, object.ID, "Conference", object.nameOfContact,
                            object.contactNo, object.dateOfEvent, object.eventRoomNo,
                            object.netTotal())

# adding data to treeview
def insert_data(self, ID, EventType, nameOfContact, contactNo, dateOfEvent, eventRoomNo, netTotal):
    self.treeview.insert('', 'end', text= ID,
                     values=( EventType, nameOfContact, contactNo, dateOfEvent, eventRoomNo, netTotal))

# function to display calander widget for date of event
def Calendarpopup(event,entryField, master, root):
    child = Toplevel()
    cal = CalendarWidget.Calendar(child, master.data)
    root.grab_release()
    child.grab_set()
    child.wait_window()
    child.grab_release()
    root.grab_set()
    Get_selected_date(master, event,entryField)

# function to get the selected date from calander widget and display it as a formatted string
def Get_selected_date(self, event, entryField):
    Day = self.data.get("day_selected", "date error")
    Month = self.data.get("month_selected", "date error")
    year = self.data.get("year_selected", "date error")
    Date = str(Day) + "/" + str(Month) + "/" + str(year)

    if entryField == "EntStartDate":
        self.EntStartDate.delete(0,'end')
        self.EntStartDate.insert([0], Date)
    else:
        self.EntEndDate.delete(0, 'end')
        self.EntEndDate.insert([0], Date)

# delete data from table
def delete_data(self):
    listofevents = []
    curItem = self.tree.focus()
    # sets the id to the id in the row
    RowID = self.tree.item(curItem)['text']

    for value in self.tree.item(curItem)['values']:
        listofevents.append(value)
        Type = listofevents[0]

    dbHelper.deleteBooking(RowID, Type)
