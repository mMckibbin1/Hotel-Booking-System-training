from tkinter import messagebox


# tests for empty entry boxes
def stringEmpty(test):
    validationfailed = False
    for strings in test:
        if strings == "" or strings == "Pick a room" or str.upper(strings) == "PICK A BAND" or str.isspace(strings):
            validationfailed = True

    return validationfailed


# only allows numbers to be entered into an entry box
def digits_only(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False


# only allows characters to be entered into an entry box
def charOnly(C):
    val_passed = True
    for item in C:
        if str.isalpha(item) or str.isspace(item) or item == "":
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


def max_character_length_50(input_string, master):
    if len(input_string) >= 50:
        messagebox.showinfo("Character limited Reached", "You have hit the maximum number of characters", parent=master)
        return False
    if not charOnly(input_string):
        return False
    return True


def max_character_length_150(input_string, master):
    if len(input_string) >= 150:
        messagebox.showinfo("Character limited Reached", "You have hit the maximum number of characters", parent=master)
        return False
    return True


def max_size_200(input_string, master):
    if input_string =="":
        return True
    if not digits_only(input_string):
        return False
    if int(input_string) > 200:
        messagebox.showinfo("Input to large", "The input that you have entered is over 200", parent=master)
        return False
    return True


def max_size_50(input_string, master):
    print("testing")
    if input_string =="":
        return True
    if not digits_only(input_string):
        return False
    if int(input_string) > 50:
        messagebox.showinfo("Input to large", "The input that you have entered is over 50", parent=master)
        return False
    return True


def max_size_31(input_string, master):
    if input_string =="":
        return True
    if not digits_only(input_string):
        return False
    if int(input_string) > 31:
        messagebox.showinfo("Input to large", "The input that you have entered is over 31", parent=master)
        return False
    return True
