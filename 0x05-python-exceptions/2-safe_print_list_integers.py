#!/usr/bin/python3
"""
    prin first nbr element of list nd only int

    """


def safe_print_list_integers(my_list=[], x=0):
    nb = 0
    for y in range(0, x):
        try:
            if y >= len(my_list):
                raise ValueError("x is greater than the length of my_list")
            print("{:d}".format(my_list[y]), end="")
            nb += 1
        except (TypeError, ValueError):
            pass
    print()
    return nb
