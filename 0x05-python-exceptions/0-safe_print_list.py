#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    d = 0

    for a in range(x):
        try:
            print("{}".format(my_list[a]), end='')
        except:
            break
        else:
            d += 1

    print()
    return (d)
