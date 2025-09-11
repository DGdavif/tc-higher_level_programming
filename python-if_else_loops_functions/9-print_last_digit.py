#!/usr/bin/python3
def print_last_digit(number):
    """Imprime e retorna o último dígito de number."""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
