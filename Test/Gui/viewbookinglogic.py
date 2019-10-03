"""Module contains the functions used by the viewbookings form"""

import datetime
from tkinter.filedialog import asksaveasfile
from Database import dbHelper
from Events import Wedding, Party, Conference
from tkinter import *
from Gui import DialogBoxes
from tkinter import messagebox
from addtionalWidgets import CalendarWidget
import CurrencyConvert
from Gui import EditPartyForm, EditWeddingForm, EditConferenceForm
import Invoice.Invoice

# global to store data from database so all functions can use it and reduce calls on the database
data_list = []


def call_update_wedding_popup(booking, self, parent):
    """Opens update form for Wedding"""
    top = Toplevel()
    EditWeddingForm.EditWedding(top, booking, self)
    top.grab_set()
    top.wait_window()
    top.destroy()
    parent.grab_set()


def call_update_party_popup(booking, self, parent):
    """Opens update form for Party"""
    top = Toplevel()
    EditPartyForm.EditParty(top, booking, self)
    top.grab_set()
    top.wait_window()
    top.destroy()
    parent.grab_set()


def call_update_conference_popup(booking, self, parent):
    """Opens update form for Conference"""
    top = Toplevel()
    EditConferenceForm.EditConference(top, booking, self)
    top.grab_set()
    top.wait_window()
    top.destroy()
    parent.grab_set()


def details_label_change(self, event_type, booking):
    """function to change the labels shown, depending on the event type selected in the tree view"""
    if event_type == 'Wedding':
        remove_all_labels(self)
        add_wedding_labels(self, booking)
        update_price_breakdown(self, booking)

    elif event_type == 'Party':
        remove_all_labels(self)
        add_party_labels(self, booking)
        update_price_breakdown(self, booking)

    elif event_type == 'Conference':
        remove_all_labels(self)
        add_conference_labels(self, booking)
        update_price_breakdown(self, booking)

    else:
        remove_all_labels(self)


def remove_all_labels(self):
    """functions to allow the labels to change in the additional info labelframe,
    removes all labels stored within labelframe"""
    self.lblNoOfGuests.grid_remove()
    self.lblDisNoOfGuests.grid_remove()
    self.lblAddress.grid_remove()
    self.lblDisAddress.grid_remove()
    self.lblDateOfBooking.grid_remove()
    self.lblDisDateOfBooking.grid_remove()
    self.lblCostPerHead.grid_remove()
    self.lblDisCostPerHead.grid_remove()
    self.lblBandName.grid_remove()
    self.lblDisBandName.grid_remove()
    self.lblBandPrice.grid_remove()
    self.lblDisBandPrice.grid_remove()
    self.lblCompanyName.grid_remove()
    self.lblDisCompanyName.grid_remove()
    self.lblNumberOfDays.grid_remove()
    self.lblDisNumberOfDays.grid_remove()
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


def add_base_labels(self, booking):
    """adds the labels that are consistent throughout all event types"""
    self.lblNoOfGuests.grid()
    self.lblDisNoOfGuests.grid()
    self.lblAddress.grid()
    self.lblDisAddress.grid()
    self.lblDateOfBooking.grid()
    self.lblDisDateOfBooking.grid()
    self.lblCostPerHead.grid()
    self.lblDisCostPerHead.grid()

    # additional info labels
    self.lblDisNoOfGuests.config(text=booking.noGuests)
    self.lblDisAddress.config(text=booking.address)
    self.lblDisDateOfBooking.config(text=booking.dateOfBooking)
    self.lblDisCostPerHead.config(text=CurrencyConvert.pound_string(booking.costPerHead))


def add_wedding_labels(self, booking):
    """adds the labels that are used for weddings"""
    add_base_labels(self, booking)
    self.lblBandName.grid()
    self.lblDisBandName.grid()
    self.lblBandPrice.grid()
    self.lblDisBandPrice.grid()
    self.lblNoOfBedsReserved.grid()
    self.lblDisNoOfBedsReserved.grid()

    # additional info labels
    self.lblDisBandName.config(text=booking.bandName)
    self.lblDisBandPrice.config(text=CurrencyConvert.pound_string(booking.bandPrice))
    self.lblDisNoOfBedsReserved.config(text=booking.noBedroomsReserved)


def add_party_labels(self, booking):
    """adds the labels that are used for parties"""
    add_base_labels(self, booking)
    self.lblBandName.grid()
    self.lblDisBandName.grid()
    self.lblBandPrice.grid()
    self.lblDisBandPrice.grid()

    # additional info labels
    self.lblDisBandName.config(text=booking.bandName)
    self.lblDisBandPrice.config(text=CurrencyConvert.pound_string(booking.bandPrice))


def add_conference_labels(self, booking):
    """adds the labels that are used for conferences"""
    add_base_labels(self, booking)
    self.lblCompanyName.grid()
    self.lblDisCompanyName.grid()
    self.lblNumberOfDays.grid()
    self.lblDisNumberOfDays.grid()
    self.lblProjectorRequired.grid()
    self.lblDisProjectorRequired.grid()

    # additional info labels
    self.lblDisCompanyName.config(text=booking.companyName)
    self.lblDisNumberOfDays.config(text=booking.noOfDays)
    self.lblDisProjectorRequired.config(text=booking.projectorRequired)


def update_price_breakdown(self, booking):
    """functions to allow the labels to change in the price breakdown labelframe"""

    # Label for guest price
    self.lblDisGuestPrice.config(text=CurrencyConvert.pound_string(booking.guests_cost()))

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
    if type(booking) == Conference.Conference:
        self.lblBandCost.config(text="Cost Per Day:")

        self.lblDisBandCost.config(text=CurrencyConvert.pound_string(booking.guests_cost()) + '   ( * ' +
                                   str(booking.noOfDays) + " days)")
    else:
        self.lblBandCost.config(text="Band Price")
        self.lblDisBandCost.config(text=CurrencyConvert.pound_string(booking.bandPrice))

    # labels for totals
    self.lblDisSubTotal.config(text=CurrencyConvert.pound_string(booking.gross_total()))
    self.lblDisVat.config(text=CurrencyConvert.pound_string(booking.vat()))
    self.lblDisTotal.config(text=CurrencyConvert.pound_string(booking.net_total()))


def calendar_popup(entry_field, master, root):
    """function to display calendar widget for date of event"""
    child = Toplevel()
    child.title("Select A Date")
    CalendarWidget.Calendar(child, master.data)
    root.grab_release()
    child.grab_set()
    child.wait_window()
    child.grab_release()
    root.grab_set()
    get_selected_date(master, entry_field)


def get_selected_date(self, entry_field):
    """function to get the selected date from calendar widget and display it as a formatted string"""

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


def cal_income(master):
    """function that calculates the total income of selected booking in treeview"""
    total_income = 0.0
    master.lblTotalIncome.config(text=total_income)
    # adds up the values in the total cost column
    for child in master.treeview.get_children():
        # costs = master.treeview.item(child, "values")[5]
        total_income += float(CurrencyConvert.remove_pound_string(master.treeview.item(child, "values")[5]))
        CurrencyConvert.pound_string(total_income)
        master.lblTotalIncome.config(text=CurrencyConvert.pound_string(total_income))


def number_of_rows(master):
    """"""
    master.lbl_number_of_rows.config(text=len(master.treeview.get_children()))


def insert_data(self, id_num, event_type, name_of_contact, contact_no, date_of_event, event_room_no, net_total):
    """function that adds data to treeview"""
    self.treeview.insert('', 'end', text=id_num,
                         values=(event_type, name_of_contact, contact_no, date_of_event, event_room_no, net_total))


def search(self):
    """function that calls dbhelper functions to search db"""
    events_list = []

    if self.checkVarConference.get() == "" and self.checkVarWedding.get() == "" and self.checkVarParty.get() == "":
        return messagebox.showinfo("Bad search criteria","At least one event type must be chosen", parent=self)

    if self.checkVarWedding.get() != "":
        events_list.append(self.checkVarWedding.get())
    if self.checkVarParty.get() != "":
        events_list.append(self.checkVarParty.get())
    if self.checkVarConference.get() != "":
        events_list.append(self.checkVarConference.get())

    if self.EntStartDate.get() != "" and self.EntEndDate.get() != "":
        if datetime.datetime.strptime(self.EntEndDate.get(), "%Y-%m-%d").date() < datetime.datetime.strptime(
                self.EntStartDate.get(), "%Y-%m-%d").date():
            return messagebox.showinfo("Bad search criteria", "End date must fall after the start date.", parent=self)

    self.treeview.delete(*self.treeview.get_children())

    search_results_list = dbHelper.search(events_list, self.EntStartDate.get(), self.EntEndDate.get())
    if len(search_results_list) == 0:
        cal_income(self)
        number_of_rows(self)
        select_first_row_(self)
        return messagebox.showinfo('No Results',
                                   'No results found.', parent=self.master2)
    for booking in search_results_list:
        if type(booking) == Wedding.Wedding:
            insert_data(self, booking.ID, "Wedding", booking.nameOfContact,
                        booking.contactNo, booking.dateOfEvent, booking.eventRoomNo,
                        CurrencyConvert.pound_string(booking.net_total()))
        elif type(booking) == Party.Party:
            insert_data(self, booking.ID, "Party", booking.nameOfContact,
                        booking.contactNo, booking.dateOfEvent, booking.eventRoomNo,
                        CurrencyConvert.pound_string(booking.net_total()))
        elif type(booking) == Conference.Conference:
            insert_data(self, booking.ID, "Conference", booking.nameOfContact,
                        booking.contactNo, booking.dateOfEvent, booking.eventRoomNo,
                        CurrencyConvert.pound_string(booking.net_total()))

    cal_income(self)
    number_of_rows(self)
    select_first_row_(self)


def load_data(master):
    """function to load the data from the database into the treeview and save the data into a global list for other
     functions to use"""
    data_base_list = dbHelper.read_all_from_db()

    for booking_list in data_base_list:
        for booking in booking_list:
            if type(booking) == Wedding.Wedding:
                insert_data(master, booking.ID, "Wedding", booking.nameOfContact,
                            booking.contactNo, booking.dateOfEvent, booking.eventRoomNo,
                            CurrencyConvert.pound_string(booking.net_total()))
            elif type(booking) == Party.Party:
                insert_data(master, booking.ID, "Party", booking.nameOfContact,
                            booking.contactNo, booking.dateOfEvent, booking.eventRoomNo,
                            CurrencyConvert.pound_string(booking.net_total()))
            elif type(booking) == Conference.Conference:
                insert_data(master, booking.ID, "Conference", booking.nameOfContact,
                            booking.contactNo, booking.dateOfEvent, booking.eventRoomNo,
                            CurrencyConvert.pound_string(booking.net_total()))

    global data_list
    data_list = data_base_list


def clear_date(self):
    """function clears date from date entries fields"""
    self.display_start_date.set("")
    self.display_end_date.set("")


def refresh_data(master):
    """function to refresh the data in the treeview"""
    master.treeview.delete(*master.treeview.get_children())
    load_data(master)
    cal_income(master)
    number_of_rows(master)
    select_first_row_(master)


def get_selected_db_entry(self):
    """function to return booking object for the selected row on treeview"""
    try:
        list_of_events = []
        global data_list
        types = None

        # sets the current item as the highlighted row in the tree view
        cur_item = self.tree.focus()

        # sets the id
        row_id = self.tree.item(cur_item)['text']

        # adds the values in the tree view to a list
        for value in self.tree.item(cur_item)['values']:
            list_of_events.append(value)

            types = list_of_events[0]

        # changes the labels depending on the ID and event type
        for booking_list in data_list:
            for booking in booking_list:
                if types == "Wedding":
                    if isinstance(booking, Wedding.Wedding):
                        if booking.ID == row_id:
                            return booking
                elif types == "Party":
                    if type(booking) == Party.Party:
                        if booking.ID == row_id:
                            return booking
                elif types == "Conference":
                    if type(booking) == Conference.Conference:
                        if booking.ID == row_id:
                            return booking
    except Exception as e:
        print(e)
        raise


def select_item(self):
    """function that gets object from database that matches selects item from treeview"""
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
    except Exception as e:
        print(e)


def update_selected(self, parent):
    """opens update form for selected event type on the tree view"""
    try:
        booking = get_selected_db_entry(self)

        if type(booking) == Wedding.Wedding:
            return call_update_wedding_popup(booking, self, parent)
        elif type(booking) == Party.Party:
            return call_update_party_popup(booking, self, parent)
        elif type(booking) == Conference.Conference:
            return call_update_conference_popup(booking, self, parent)
    except Exception as e:
        print(e)
        DialogBoxes.select_row(self.master2)


def invoice(self):
    """creates an invoice for selected row in form"""
    try:
        booking = get_selected_db_entry(self)

        def load_file():
            file_name = asksaveasfile(defaultextension=".docx", filetypes=([("document file", "*.docx")]), parent=self)
            if file_name:
                return file_name.name

        # changes the labels depending on the ID and event type
        if type(booking) == Wedding.Wedding:
            return Invoice.Invoice.invoice(address=booking.address, invoice_type="Wedding",
                                           cost_per_head=CurrencyConvert.pound_string(booking.costPerHead),
                                           number_of_guests=booking.noGuests,
                                           band_name=booking.bandName,
                                           band_cost=CurrencyConvert.pound_string(booking.bandPrice),
                                           number_of_days="N/A",
                                           guests_cost=CurrencyConvert.pound_string(booking.guests_cost()),
                                           cost_per_day="N/A",
                                           sub_total=CurrencyConvert.pound_string(booking.gross_total()),
                                           vat=CurrencyConvert.pound_string(booking.vat()),
                                           total=CurrencyConvert.pound_string(booking.net_total()),
                                           file_name=load_file())
        elif type(booking) == Party.Party:
            return Invoice.Invoice.invoice(address=booking.address, invoice_type="Party",
                                           cost_per_head=CurrencyConvert.pound_string(booking.costPerHead),
                                           number_of_guests=booking.noGuests,
                                           band_name=booking.bandName,
                                           band_cost=CurrencyConvert.pound_string(booking.bandPrice),
                                           number_of_days="N/A",
                                           guests_cost=CurrencyConvert.pound_string(booking.guests_cost()),
                                           cost_per_day="N/A",
                                           sub_total=CurrencyConvert.pound_string(booking.gross_total()),
                                           vat=CurrencyConvert.pound_string(booking.vat()),
                                           total=CurrencyConvert.pound_string(booking.net_total()),
                                           file_name=load_file())
        elif type(booking) == Conference.Conference:
            return Invoice.Invoice.invoice(address=booking.address, invoice_type="Conference",
                                           cost_per_head=CurrencyConvert.pound_string(booking.costPerHead),
                                           number_of_guests=booking.noGuests,
                                           band_name="N/A", band_cost="N/A",
                                           number_of_days=booking.noOfDays,
                                           guests_cost=CurrencyConvert.pound_string(booking.guests_cost()),
                                           cost_per_day=CurrencyConvert.pound_string(booking.guests_cost()),
                                           sub_total=CurrencyConvert.pound_string(booking.gross_total()),
                                           vat=CurrencyConvert.pound_string(booking.vat()),
                                           total=CurrencyConvert.pound_string(booking.net_total()),
                                           file_name=load_file())
    except Exception as e:
        print(e)
        return DialogBoxes.select_row(self)


def select_first_row_(self):
    """selects the first row on the tree view when form loads"""
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


def is_row_selected_delete(self, master):
    """function to check if a row is selected"""
    try:
        list_of_events = []
        types = None
        cur_item = self.tree.focus()
        # sets the id to the id in the row
        row_id = self.tree.item(cur_item)['text']

        for value in self.tree.item(cur_item)['values']:
            list_of_events.append(value)
            types = list_of_events[0]
        # if the row is not empty then the delete functions will be run
        if row_id != "":
            # asks user is there really want to delete or not
            if DialogBoxes.delete(master):
                dbHelper.deleteBooking(row_id, types)
                messagebox.showinfo('Deleted', 'Booking Deleted', parent=master)
                refresh_data(master=master)

        # if it is empty user will be prompted to select a row
        else:
            # displays a prompt to select a row
            DialogBoxes.select_row(self.master2)
    except Exception as e:
        print(e)
