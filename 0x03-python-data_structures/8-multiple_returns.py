#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)

    if lenght:
        first = sentence[0]
    else:
        frist = None

    return lenght, first
