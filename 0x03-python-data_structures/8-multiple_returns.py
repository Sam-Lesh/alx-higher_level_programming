#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)

    if (leng == 0):
        new = (leng, None)
    else:
        new = (leng, sentence[0])

    return (new)
