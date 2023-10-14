#!/usr/bin/env python3

def no_c(my_string):
    ns = ""
    for ch in my_string:
        if ch not in ("c", "C"):
            ns = ns + ch
    return ns
