import locale

locale.setlocale(locale.LC_ALL, '')


def pound_string(input_string):
    """function will convert a value into a string of pounds and pence containing a £ sign"""
    return locale.currency(input_string, grouping=True)


def remove_pound_string(input_string):
    return locale.atof(input_string.strip("£"))
