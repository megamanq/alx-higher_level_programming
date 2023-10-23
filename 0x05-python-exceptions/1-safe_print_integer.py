#!/usr/bin/python3
"""
    print int in str.format().

    """


def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
        return(True)
    except:
        return False
