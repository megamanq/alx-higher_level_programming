#!/usr/bin/python3

def weight_average(my_list=[]):
    sums = 0
    divs = 0
    
    sums = sum([x * y for x, y in my_list])
    divs = sum([x[1] for x in my_list])

    return sums / divs
