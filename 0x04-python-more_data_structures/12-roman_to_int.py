#!/usr/bin/python3

def roman_to_int(roman_string):
    dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50,
            "C" : 100, "D" : 500, "M" : 1000}
    res = 0

    if type(roman_string) != str or not roman_string:
        return 0
    else:
        for char in roman_string:
            for key in dict.keys():
                if char == key:
                    res = res + dict[key]
        return res
