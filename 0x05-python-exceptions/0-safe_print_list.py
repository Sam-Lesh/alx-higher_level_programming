#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    if not my_list:
        print("")
        return (0)
    while a < x:
        try:
            print("{}".format(my_list[a]), end="")
            a += 1
        except IndexError:
            break
    print("")
    return (a)
