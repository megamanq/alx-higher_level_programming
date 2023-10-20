#!/usr/bin/python3

def best_score(a_dictionary):
    key = ""
    val = 0

    if not a_dictionary:
        return None
    else:
        for k, v in a_dictionary.items():
            if v > val:
                val = v
                key = k
        return key
