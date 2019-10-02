"""Contains function used to mail-merge an invoice using template"""

from __future__ import print_function
import datetime
from mailmerge import MailMerge
from addtionalWidgets import CurrencyConvert


def invoice(address, invoice_type, cost_per_head, number_of_guests, band_name, band_cost, number_of_days,
            guests_cost, cost_per_day, sub_total, VAT, total, file_name):
    try:
        template = "M:\GitHub\Hotel-Booking-System-training\Test\Invoice Template\invoiceTemplate.docx"

        document = MailMerge(template)

        document.merge(
            GuestsCost=str(guests_cost),
            costPerHead=str(cost_per_head),
            BandCost=str(band_cost),
            Date=str(datetime.datetime.now().date()),
            VAT=str(VAT),
            Address=str(address),
            BandName=str(band_name),
            subTotal=str(sub_total),
            TotalCost=str(total),
            CostPerDay=str(cost_per_day),
            numberofguests=str(number_of_guests),
            InvoiceType=str(invoice_type),
            numberofDays=str(number_of_days)
        )
        if file_name:
            document.write(file_name)
    except Exception as e:
        print(e)