from tkinter.messagebox import *

# tests for empty entry boxes
def stringEmpty(test):
    validationfailed = False
    for strings in test:

        if strings == "":
            validationfailed = True

    if validationfailed:
        showwarning('Warning', 'Please enter a value')

        # else:
        #     showwarning('Warning', 'Failed')


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