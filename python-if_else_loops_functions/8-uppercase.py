#!/usr/bin/python3
def uppercase(str):
    """Imprime a string em maiúsculas seguida de nova linha."""
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
