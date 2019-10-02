import datetime
from tkinter.filedialog import asksaveasfile
from Database import dbHelper
from Events import Wedding, Party, Conference
from tkinter import *
from Gui import DialogBoxes
from tkinter import messagebox
from addtionalWidgets import CalendarWidget, CurrencyConvert
from Gui import EditPartyForm, EditWeddingForm, EditConferenceForm
import Events.Invoice
# global to store data from database so all functions can use it and reduce calls on the database
data_list = []


#  Opens update form for Wedding
def call_update_wedding_popup(object, self, parent):
    top = Toplevel()
    EditWeddingForm.EditWedding(top, object, self)
    top.grab_set()
    top.wait_window()
    top.destroy()
    parent.grab_set()


#  Opens update form for Party
def call_update_party_popup(object, self, parent):
    top = Toplevel()
    EditPartyForm.EditParty(top, object, self)
    top.grab_set()
    top.wait_window()
    top.destroy()
    parent.grab_set()


#  Opens update form for Conference
def call_update_conference_popup(object, self, parent):
    top = Toplevel()
    EditConferenceForm.EditConference(top, object, self)
    top.grab_set()
    top.wait_window()
    top.destroy()
    parent.grab_set()


# function to change the labels shown, depending on the event type selected in the treeview
def details_label_change(self, eventType, object):
    if eventType == 'Wedding':
        remove_all_labels(self)
        add_wedding_labels(self, object)
        update_price_breakdown(self, object)

    elif eventType == 'Party':
        remove_all_labels(self)
        add_party_labels(self, object)
        update_price_breakdown(self, object)

    elif eventType == 'Conference':
        remove_all_labels(self)
        add_conference_lables(self, object)
        update_price_breakdown(self, object)

    else:
        remove_all_labels(self)


# functions to allow the labels to change in the additional info labelframe
# removes all labels stored within labelframe
def remove_all_labels(self):
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
def add_base_lables(self, object):
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
    self.lblDisCostPerHead.config(text=CurrencyConvert.pound_string(object.costPerHead))


# adds the labels that are used for weddings
def add_wedding_labels(self, object):
    add_base_lables(self, object)
    self.lblBandName.grid()
    self.lblDisBandName.grid()
    self.lblBandPrice.grid()
    self.lblDisBandPrice.grid()
    self.lblNoOfBedsReserved.grid()
    self.lblDisNoOfBedsReserved.grid()

    # additional info labels
    self.lblDisBandName.config(text=object.bandName)
    self.lblDisBandPrice.config(text=CurrencyConvert.pound_string(object.bandPrice))
    self.lblDisNoOfBedsReserved.config(text=object.noBedroomsReserved)


# adds the labels that are used for parties
def add_party_labels(self, object):
    add_base_lables(self, object)
    self.lblBandName.grid()
    self.lblDisBandName.grid()
    self.lblBandPrice.grid()
    self.lblDisBandPrice.grid()

    # additional info labels
    self.lblDisBandName.config(text=object.bandName)
    self.lblDisBandPrice.config(text=CurrencyConvert.pound_string(object.bandPrice))


# adds the labels that are used for conferences
def add_conference_lables(self, object):
    add_base_lables(self, object)
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
def update_price_breakdown(self, object):
    # Label for guest price
    self.lblDisGuestPrice.config(text=CurrencyConvert.pound_string(object.guestsCost()))

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
        self.lblDisBandCost.config(text=CurrencyConvert.pound_string(object.guestsCost()) + '   ( * ' + str(object.noOfDays) + " days)")
    else:
        self.lblBandCost.config(text="Band Price")
        self.lblDisBandCost.config(text=CurrencyConvert.pound_string(object.bandPrice))

    # labels for totals
    self.lblDisSubTotal.config(text=CurrencyConvert.pound_string(object.grosstotal()))
    self.lblDisVat.config(text=CurrencyConvert.pound_string(object.VAT()))
    self.lblDisTotal.config(text=CurrencyConvert.pound_string(object.netTotal()))


# function to display calendar widget for date of event
def calendar_popup(event, entry_field, master, root):
    child = Toplevel()
    child.title("Select A Date")
    cal = CalendarWidget.Calendar(child, master.data)
    root.grab_release()
    child.grab_set()
    child.wait_window()
    child.grab_release()
    root.grab_set()
    get_selected_date(master, event, entry_field)


# function to get the selected date from calendar widget and display it as a formatted string
def get_selected_date(self, event, entry_field):
    day = self.data.get("day_selected", "date error")
    month = self.data.get("month_selected", "date error")
    year = self.data.get("year_selected", "date error")
    date = str(year) + "-" + str(month) + "-" + str(day)

    if day == "date error":
        return

    format_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    if entry_field == "EntStartDate":
        self.display_start_date.set("")
        self.display_start_date.set(format_date)
    else:
        self.display_end_date.set("")
        self.display_end_date.set(format_date)


# calculates the total income
def cal_income(master):
    total_income = 0.0
    master.lblTotalIncome.config(text=total_income)
    # adds up the values in the total cost column
    for child in master.treeview.get_children():
        #costs = master.treeview.item(child, "values")[5]
        total_income += float(CurrencyConvert.remove_pound_string(master.treeview.item(child, "values")[5]))
        CurrencyConvert.pound_string(total_income)
        master.lblTotalIncome.config(text=CurrencyConvert.pound_string(total_income))




# adding data to treeview
def insert_data(self, id, event_type, name_of_contact, contact_no, date_of_event, event_room_no, net_total):
    self.treeview.insert('', 'end', text=id,
                         values=(event_type, name_of_contact, contact_no, date_of_event, event_room_no, net_total))


# function to search db
def search(self):
    events_list = []

    if self.checkVarWedding.get() != "":
        events_list.append(self.checkVarWedding.get())
    if self.checkVarParty.get() != "":
        events_list.append(self.checkVarParty.get())
    if self.checkVarConference.get() != "":
        events_list.append(self.checkVarConference.get())

    self.treeview.delete(*self.treeview.get_children())
    search_results_list = dbHelper.search(events_list, self.EntStartDate.get(), self.EntEndDate.get())
    if len(search_results_list) == 0:
        cal_income(self)
        select_first_row_(self)
        return messagebox.showinfo('No Results',
                                   'No results found.', parent=self.master2)
    for object in search_results_list:
        if type(object) == Wedding.Wedding:
            insert_data(self, object.ID, "Wedding", object.nameOfContact,
                        object.contactNo, object.dateOfEvent, object.eventRoomNo,
                        CurrencyConvert.pound_string(object.netTotal()))
        elif type(object) == Party.Party:
            insert_data(self, object.ID, "Party", object.nameOfContact,
                        object.contactNo, object.dateOfEvent, object.eventRoomNo,
                        CurrencyConvert.pound_string(object.netTotal()))
        elif type(object) == Conference.Conference:
            insert_data(self, object.ID, "Conference", object.nameOfContact,
                        object.contactNo, object.dateOfEvent, object.eventRoomNo,
                        CurrencyConvert.pound_string(object.netTotal()))

    cal_income(self)
    select_first_row_(self)



# function to load the data from the database into the table
def load_data(master):
    data_base_list = dbHelper.read_all_from_db()

    for list in data_base_list:
        for object in list:
            if type(object) == Wedding.Wedding:
                insert_data(master, object.ID, "Wedding", object.nameOfContact,
                            object.contactNo, object.dateOfEvent, object.eventRoomNo,
                            CurrencyConvert.pound_string(object.netTotal()))
            elif type(object) == Party.Party:
                insert_data(master, object.ID, "Party", object.nameOfContact,
                            object.contactNo, object.dateOfEvent, object.eventRoomNo,
                            CurrencyConvert.pound_string(object.netTotal()))
            elif type(object) == Conference.Conference:
                insert_data(master, object.ID, "Conference", object.nameOfContact,
                            object.contactNo, object.dateOfEvent, object.eventRoomNo,
                            CurrencyConvert.pound_string(object.netTotal()))

    global data_list
    data_list = data_base_list


#  function clears date from date entries fields
def clear_date(self):
    self.display_start_date.set("")
    self.display_end_date.set("")


# function to reload the table
def refresh_data(master):
    master.treeview.delete(*master.treeview.get_children())
    load_data(master)
    cal_income(master)
    select_first_row_(master)
    # dialog box to confirm refresh
    # DialogBoxes.table_refreshed()


#  function to return object for the selected row on treeview
def get_selected_db_entry(self):
    try:
        list_of_events = []
        global data_list

        # sets the current item as the highlighted row in the treeview
        curItem = self.tree.focus()

        # sets the id
        RowID = self.tree.item(curItem)['text']

        # adds the values in the tree view to a list
        for value in self.tree.item(curItem)['values']:
            list_of_events.append(value)

            types = list_of_events[0]

        # changes the labels depending on the ID and event type
        for list in data_list:
            for object in list:
                if types == "Wedding":
                    if isinstance(object, Events.Wedding.Wedding):
                        if object.ID == RowID:
                            return object
                elif types == "Party":
                    if type(object) == Party.Party:
                        if object.ID == RowID:
                            return object
                elif types == "Conference":
                    if type(object) == Conference.Conference:
                        if object.ID == RowID:
                            return object
    except:
        print("")
        raise
        #DialogBoxes.select_row(self.master2)


# selects item from treeview
def select_item(a, self):
    # try except to make sure a row is selected
    try:
        booking = get_selected_db_entry(self)
        # changes the labels depending on the ID and event type
        if type(booking) == Wedding.Wedding:
            return details_label_change(self, "Wedding", booking)
        elif type(booking) == Party.Party:
            return details_label_change(self, "Party", booking)
        elif type(booking) == Conference.Conference:
            return details_label_change(self, "Conference", booking)
    except:
        print("Please select a row")


#  opens update form for selected row in treeview on form
def update_selected(self, parent):
    print("fdskjdskjhfdskjhfdsiuh")
    try:
        booking = get_selected_db_entry(self)

        if type(booking) == Wedding.Wedding:
            return call_update_wedding_popup(booking, self, parent)
        elif type(booking) == Party.Party:
            return call_update_party_popup(booking, self, parent)
        elif type(booking) == Conference.Conference:
            return call_update_conference_popup(booking, self, parent)
    except:
        print("please select a row first")
        DialogBoxes.select_row(self.master2)


# creates an invoice for selected row in form
def invoice(self):
    try:
        booking = get_selected_db_entry(self)

        def load_file():
            file_name = asksaveasfile(defaultextension=".docx", filetypes=([("document file", "*.docx")]), parent=self)
            if file_name:
                return file_name.name

        # changes the labels depending on the ID and event type
        if type(booking) == Wedding.Wedding:
            return Events.Invoice.Invoice(address=booking.address, invoice_type="Wedding",
                                          cost_per_head=CurrencyConvert.pound_string(booking.costPerHead),
                                          number_of_guests=booking.noGuests,
                                          band_name=booking.bandName, band_cost=CurrencyConvert.pound_string(booking.bandPrice),
                                          number_of_days="N/A", guests_cost=CurrencyConvert.pound_string(booking.guestsCost()),
                                          cost_per_day="N/A", sub_total=CurrencyConvert.pound_string(booking.grosstotal()),
                                          VAT=CurrencyConvert.pound_string(booking.VAT()),
                                          total=CurrencyConvert.pound_string(booking.netTotal()), file_name=load_file())
        elif type(booking) == Party.Party:
            return Events.Invoice.Invoice(address=booking.address, invoice_type="Party",
                                          cost_per_head=CurrencyConvert.pound_string(booking.costPerHead),
                                          number_of_guests=booking.noGuests,
                                          band_name=booking.bandName, band_cost=CurrencyConvert.pound_string(booking.bandPrice),
                                          number_of_days="N/A", guests_cost=CurrencyConvert.pound_string(booking.guestsCost()),
                                          cost_per_day="N/A", sub_total=CurrencyConvert.pound_string(booking.grosstotal()),
                                          VAT=CurrencyConvert.pound_string(booking.VAT()),
                                          total=CurrencyConvert.pound_string(booking.netTotal()),
                                          file_name=load_file())
        elif type(booking) == Conference.Conference:
            return Events.Invoice.Invoice(address=booking.address, invoice_type="Conference",
                                          cost_per_head=CurrencyConvert.pound_string(booking.costPerHead),
                                          number_of_guests=booking.noGuests,
                                          band_name="N/A", band_cost="N/A",
                                          number_of_days=booking.noOfDays, guests_cost=CurrencyConvert.pound_string(booking.guestsCost()),
                                          cost_per_day=CurrencyConvert.pound_string(booking.guestsCost()),
                                          sub_total=CurrencyConvert.pound_string(booking.grosstotal()),
                                          VAT=CurrencyConvert.pound_string(booking.VAT()),
                                          total=CurrencyConvert.pound_string(booking.netTotal()), file_name=load_file())
    except:
        return DialogBoxes.select_row(self)


# selects the first row on the treeview when form loads
def select_first_row_(self):
    child_id = self.treeview.get_children()
    if child_id:
        self.tree.focus(child_id[0])
        self.tree.selection_set(child_id[0])
        remove_all_labels(self)

        booking = get_selected_db_entry(self)

        # changes the labels depending on the ID and event type
        if type(booking) == Wedding.Wedding:
            return details_label_change(self, "Wedding", booking)
        elif type(booking) == Party.Party:
            return details_label_change(self, "Party", booking)
        elif type(booking) == Conference.Conference:
            return details_label_change(self, "Conference", booking)
    else:
        remove_all_labels(self)


# delete data from table and database
def delete_data(self):
    # try catch to check if a row is selected
    try:
        list_of_events = []
        cur_item = self.tree.focus()
        # sets the id to the id in the row
        row_id = self.tree.item(cur_item)['text']

        for value in self.tree.item(cur_item)['values']:
            list_of_events.append(value)
            type = list_of_events[0]

        dbHelper.deleteBooking(row_id, type)

    except:
        print("please select a row first")
        # displays a promt to select a row
        DialogBoxes.select_row(self.master2)


def is_row_selected_delete(self, master):
    # function to check if a row is selected
    list_of_events = []
    cur_item = self.tree.focus()
    # sets the id to the id in the row
    row_id = self.tree.item(cur_item)['text']

    for value in self.tree.item(cur_item)['values']:
        list_of_events.append(value)
        Type = list_of_events[0]
    # if the row is not empty then the delete functions will be run
    if row_id != "":
        # asks user is there really want to delete or not
        DialogBoxes.Delete(self, master)
    # if it is empty user will be promted to select a row
    else:
        # displays a promt to select a row
        DialogBoxes.select_row(self.master2)
