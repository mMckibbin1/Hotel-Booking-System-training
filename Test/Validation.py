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
    if str.isalpha(C) or str.isspace(C) or C == "":
        return True
    else:
        return False


# min number
def min_number(M, N=1):
    if int(M) and int(N) >= 1:
        return False
    else:
        return True
