#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    copy = ""

    for chr in str:
        if i == n:
            i = i + 1
            continue
        else:
            copy = copy + chr
            i = i + 1

    return copy
