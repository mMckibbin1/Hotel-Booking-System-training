from tkinter.messagebox import *

# tests for empty entry boxes
def stringEmpty(test):
    validationfailed = False
    for strings in test:
        if strings == "" or strings == "Pick a room" or str.upper(strings) == "PICK A BAND" or str.isspace(strings):
            validationfailed = True

    return validationfailed


# only allows numbers to be entered into an entry box
def callback(P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

# only allows characters to be entered into an entry box
def charOnly(C):
    val_passed = True
    for item in C:
        if str.isalpha(item) or str.isspace(item) or item=="":
            val_passed = True
        else:
            val_passed = False
    return val_passed


def min_number(list):
    val_failed = True
    for item in list:
        if int(item) >= 1:
            val_failed = False
        else:
            val_failed = True
            return val_failed
    return val_failed
