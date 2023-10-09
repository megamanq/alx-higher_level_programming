#!/usr/bin/python3

from sys import argv


if __name__ == "__main__":
    i = 1
    arg_number = len(argv) - 1

    if arg_number == 0:
        print("{} arguments.".format(arg_number))
    elif arg_number == 1:
        print("{} argument:".format(arg_number))
    else:
        print("{} arguments:".format(arg_number))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
