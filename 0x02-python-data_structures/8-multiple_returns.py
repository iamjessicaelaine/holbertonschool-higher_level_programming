#!/usr/bin/python3
def multiple_returns(sentence):
    newtuple = ()

    senlen = len(sentence)
    if senlen == 0:
        sentence[0] = None
    newtuple = (senlen, sentence[0])
    return newtuple
