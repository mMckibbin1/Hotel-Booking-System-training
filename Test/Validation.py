from tkinter.messagebox import *

# tests for empty entry boxes
def stringEmpty(test):
    validationfailed = False
    for strings in test:
        if strings == "":
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
    if str.isalpha(C) or C == "":
        return True
    else:
        return False


def min_number(list):
    val_failed = True
    for item in list:
        if float(item) >= 1:
            val_failed = False
        else:
            val_failed = True
            return val_failed
    return val_failed
