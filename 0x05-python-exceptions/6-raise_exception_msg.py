#!/usr/bin/python3
"""
    func rais type excep with msg
    """

def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except:
        raise
