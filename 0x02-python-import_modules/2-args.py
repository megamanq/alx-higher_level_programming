#!/usr/bin/python3

import sys


def main(*argv):
    i = 0
    ln = len(sys.argv) - 1
    if ln == 1:
        print("{:d} argument:".format(ln))
    elif ln == 0:
        print("{:d} arguments.".format(ln))
    else:
        print("{:d} arguments:".format(ln))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()
