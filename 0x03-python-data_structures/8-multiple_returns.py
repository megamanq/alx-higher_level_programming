#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    first = ''
    if lenght != 0:
        first = sentence[0]
    else:
        frist = None

    return lenght, first
