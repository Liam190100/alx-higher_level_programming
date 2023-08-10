#!/usr/bin/python3
def fizzbuzz():
    for numer in range(1, 101):
        if numer % 3 == 0 and numer % 5 == 0:
            print("FizzBuzz ", end="")
        elif numer % 3 == 0:
            print("Fizz ", end="")
        elif numer % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numer), end="")
