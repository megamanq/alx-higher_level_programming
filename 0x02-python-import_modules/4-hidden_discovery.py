#!/usr/bin/python3
import hidden_4


def main():
    lng = dir(hidden_4)
    for i in range(len(lng)):
        if(lng[i][0] != '_'):
            print("{}".format(lng[i]))


if __name__ == "__main__":
    main()
