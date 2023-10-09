#!/usr/bin/python3

from sys import argv


def main(*argv):

    res = 0

    for arg in range(1, len(argv)):
        res = res + int(argv[arg])

    print("{:d}".format(res))


if __name__ == "__main__":
    main(*argv)
