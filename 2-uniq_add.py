#!/usr/bin/python3

def uniq_add(my_list=[]):
    list = set(my_list)
    res = 0

    for elem in list:
        res = res + elem
    return res
