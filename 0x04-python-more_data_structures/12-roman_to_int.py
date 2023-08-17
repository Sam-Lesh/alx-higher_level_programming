#!/usr/bin/python3
def subtracting(list_num):
    sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            sub += n

    return (max_list - sub)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_num.keys())

    number = 0
    last_roman = 0
    list_num = [0]

    for a in roman_string:
        for rn in list_keys:
            if rn == a:
                if roman_num.get(a) <= last_roman:
                    number += subtracting(list_num)
                    list_num = [roman_num.get(a)]
                else:
                    list_num.append(roman_num.get(a))

                last_roman = roman_num.get(a)

    number += subtracting(list_num)

    return (number)
