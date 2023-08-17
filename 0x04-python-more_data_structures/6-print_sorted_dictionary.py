#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dict = list(a_dictionary.keys())
    list_dict.sort()
    for d in list_dict:
        print("{}: {}".format(d, a_dictionary.get(d)))
