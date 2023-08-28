#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    d = 0

    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            d += 1

    print()
    return (d)
