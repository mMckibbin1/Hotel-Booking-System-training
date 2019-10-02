from Gui import MainMenu
from Database import dbHelper
from Events import Conference, Wedding, Party

# list  = [[],[],[]]
#
# w1 = Wedding.Wedding('Bill','Bob','Tom','Hooly',1,1,1,1,1,1,1)
# w2 = Wedding.Wedding(2,'Bob',2,2,2,2,2,2,2,2,2)
#
# p1 = Party.Party(1,'Bob',1,1,1,1,1,1,1,2)
# p2 = Party.Party(2,'Bob',2,2,2,2,2,2,2,2)
#
# c1 = Conference.Conference(1,'Bob',1,1,1,1,1,1,1,1,1)
# c2 = Conference.Conference(2,'Bob',2,2,2,2,2,2,2,2,2)
#
# list[0].append(w1)
# list[0].append(w2)
#
# list[1].append(p1)
# list[1].append(p2)
#
# list[2].append(c1)
# list[2].append(c2)
#
# for list1 in list:
#     for object in list1:
#         if type(object) == Wedding.Wedding:
#             print(object.noGuests)
#             print(object.contactNo)
#             'weddign'






dbHelper.connect()
MainMenu.MainMenu()

