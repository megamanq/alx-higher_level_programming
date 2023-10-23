#!/usr/bin/python3
import sys

"""
     func exec a func safely
    """


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
