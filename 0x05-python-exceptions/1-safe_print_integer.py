#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not str(value).isdigit():
            # return "{:d}".format(value)
            print("{}".format(value))
        else:
            # return "{:}".format(value)
            print("{:d}".format(value))
    except SyntaxError:
        return "Please redo it again"
