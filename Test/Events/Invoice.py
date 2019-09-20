from __future__ import print_function

import datetime

from mailmerge import MailMerge

template = "M:\GitHub\Hotel-Booking-System-training\Test\Invoice Template\invoiceTemplate.docx"

document = MailMerge(template)
print(document.get_merge_fields())

def Invoice(address, invoice_number, cost_per_head, number_of_guests, band_name, band_cost, number_of_days,
             guests_cost, cost_per_day, sub_total, VAT, total, file_name):
    template = "M:\GitHub\Hotel-Booking-System-training\Test\Invoice Template\invoiceTemplate.docx"

    document = MailMerge(template)
    print(document.get_merge_fields())

    document.merge(
        GuestsCost=guests_cost,
        costPerHead=cost_per_head,
        BandCost=band_cost,
        Date=datetime.datetime.now().date(),
        VAT=VAT,
        Address=address,
        BandName=band_name,
        subTotal=sub_total,
        TotalCost=total,
        CostPerDay=cost_per_day,
        numberofguests=number_of_guests,
        InvoiceNumber=invoice_number,
        numberofDays=number_of_days
    )

    document.write("Invoice Template/{}.docx".format(file_name))
