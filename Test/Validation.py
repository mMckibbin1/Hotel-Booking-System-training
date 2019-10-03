"""module contains function use to validate user input"""

from tkinter import messagebox, END


def string_empty(test):
    """function tests for empty entry boxes"""
    validation_failed = False
    for strings in test:

        if strings == "" or strings == "Pick a room" or strings == "No Rooms Free" \
                or str.upper(strings) == "PICK A BAND" or str.isspace(strings):
            validation_failed = True
    return validation_failed


def digits_only(p):
    """function to only allows numbers to be entered into an entry box"""
    if str.isdigit(p) or p == "":
        return True
    else:
        return False


def char_only(c):
    """function to only allows characters to be entered into an entry box"""
    val_passed = True
    for item in c:
        if str.isalpha(item) or str.isspace(item) or item == "":
            val_passed = True
        else:
            val_passed = False
    return val_passed


def min_number(string_list):
    """function to ensure that an entry box value is equal to or greater than 1"""
    val_failed = True
    for item in string_list:
        if int(item) >= 1:
            val_failed = False
        else:
            val_failed = True
            return val_failed
    return val_failed


def max_character_length_50(input_string, master):
    """function to stop entry box input greater that 50 characters"""
    if len(input_string) > 50:
        messagebox.showinfo("Character limit Reached", "You have hit the maximum number of characters", parent=master)
        return False
    if not char_only(input_string):
        return False
    return True


def max_character_length_150(input_string, master):
    """function to stop entry box input greater that 150 characters"""
    if len(input_string) > 150:
        messagebox.showinfo("Character limit Reached", "You have hit the maximum number of characters", parent=master)
        return False
    return True


def max_character_length_25_digits_only(input_string, master):
    """function to stop entry box input greater that 25 characters and to ensure that only digits are used"""
    if input_string == "":
        return True
    if not digits_only(input_string):
        return False
    if len(input_string) > 25:
        messagebox.showinfo("Character limit Reached", "You have hit the maximum number of characters", parent=master)
        return False
    return True


def max_size_200(input_string, master):
    """function to stop value entered into entry box input greater that 200 and to ensure that only
    digits are used"""
    if input_string == "":
        return True
    if not digits_only(input_string):
        return False
    if int(input_string) > 200:
        messagebox.showinfo("Input too large", "The input that you have entered is over 200", parent=master)
        return False
    return True


def max_size_50(input_string, master):
    """function to stop value entered into entry box input greater that 50 and to ensure that only
    digits are used"""
    if input_string == "":
        return True
    if not digits_only(input_string):
        return False
    if int(input_string) > 50:
        messagebox.showinfo("Input too large", "The input that you have entered is over 50", parent=master)
        return False
    return True


def max_size_31(input_string, master):
    """function to stop value entered into entry box input greater that 31 and to ensure that only
    digits are used"""
    if input_string == "":
        return True
    if not digits_only(input_string):
        return False
    if int(input_string) > 31:
        messagebox.showinfo("Input too large", "The input that you have entered is over 31", parent=master)
        return False
    return True


def contact_number_val(input_string, entry_field, parent):
    """function to stop value entered being longer than 25 characters, less that 4 characters, and only contain
    digits"""
    if not digits_only(input_string):
        messagebox.showinfo("Error", "Contact Number can only contain digits", parent=parent)
        entry_field.focus()
        entry_field.delete(0, END)
        return False
    elif len(input_string) > 25:
        messagebox.showinfo("Error", "Contact Number too long max input of 25", parent=parent)
        entry_field.focus()
        entry_field.delete(0, END)
        return False
    elif len(input_string) < 4:
        messagebox.showinfo("Error", "Contact Number too short minimum input of 4", parent=parent)
        entry_field.focus()
        entry_field.delete(0, END)
        return False
    else:
        return True
