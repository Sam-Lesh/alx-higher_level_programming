#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)

    if a_len == 0:
        a_1 = 0
        a_2 = 0
    elif a_len == 1:
        a_1 = tuple_a[0]
        a_2 = 0
    else:
        a_1 = tuple_a[0]
        a_2 = tuple_a[1]

    if b_len == 0:
        b_1 = 0
        b_2 = 0
    elif b_len == 1:
        b_1 = tuple_b[0]
        b_2 = 0
    else:
        b_1 = tuple_b[0]
        b_2 = tuple_b[1]

    new = (a_1 + b_1, a_2 + b_2)

    return (new)
