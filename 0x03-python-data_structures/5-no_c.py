#!/usr/bin/python3
def no_c(my_string):
    leng = len(my_string)

    x = 0

    new = my_string[:]

    for y in range(leng):
        if (my_string[y] == 'c' or my_string[y] == 'C'):
            new = new[:(y - x)] + my_string[(y + 1):]
            x += 1

    return (new)
