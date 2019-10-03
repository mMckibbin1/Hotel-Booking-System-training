"""module is that access point to the program and """

from Gui import MainMenu
from Database import dbHelper

dbHelper.connect()  # calls function to ensure that database exists
MainMenu.MainMenu()  # Calls main menu UI
