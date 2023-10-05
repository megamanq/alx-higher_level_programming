#!/usr/bin/python3

import hidden_4


def main():
    ln = dir(hidden_4)
    for i in range(len(ln)):
        if(ln[i][0] != '_'):
            print("{}".format(ln[i]))


if __name__ == "__main__":
    main()
