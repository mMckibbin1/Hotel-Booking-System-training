from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "Invoice Template/invoiceTemplate.docx"

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(
    costPerHead ="10",
    Band="AB/CD",
    Guests="10",
    Cost="£400",
    VAT="£50",
    Address="SERC",
    Sub="400",
    GuestsCost="20",
    Total="450",
    invoiceNumber="1",
    Number="12432324",
    Date="20/08/2019"
)

document.write("Invoice Template/invoiceTemplateTest.docx")