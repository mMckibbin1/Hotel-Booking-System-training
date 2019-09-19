import datetime


class Invoice:
    def  __init__(self, address, invoice_number, cost_per_head, number_of_guests, band_name, band_cost, number_of_days):
        self.date = datetime.datetime.now()
        self.address = address
        self.invoice_number = invoice_number
        self.cost_per_head = cost_per_head
        self.number_of_guests = number_of_guests
        self.band_name = band_name
        self.band_cost = band_cost
        self.number_of_days = number_of_days
