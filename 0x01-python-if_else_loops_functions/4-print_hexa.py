#!/usr/bin/python3
print("".join(map(lambda alp: chr(alp), filter(lambda alp: alp != 101 and alp != 113, range(97, 123)))), end='')
