#!/usr/bin/python3

def weight_average(my_list=[]):
    sums = 0
    divs = 0

    for tupl in my_list:
        sums += 0 + tupl[0] * tupl[1]
        divs += 0 + tupl[1]
    return sums / divs
