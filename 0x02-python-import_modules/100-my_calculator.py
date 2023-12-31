#!/usr/bin/python3

import calculator_1 as calc
from sys import argv


def main(*argv):
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif argv[2] == "-":
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif argv[2] == "*":
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif argv[2] == "/":
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)


if __name__ == "__main__":
    main(*argv)
