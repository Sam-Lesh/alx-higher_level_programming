#!/usr/bin/python3
def remove_char_at(str, n):
    st = ""
    for a in range(len(str)):
        if a != n:
            st = st + str[a]
    return (st)
