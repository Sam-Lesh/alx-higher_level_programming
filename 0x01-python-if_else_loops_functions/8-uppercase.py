#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        if ord(str[a]) >= 97 and ord(str[a]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[a]) - num), end='')
    print()
