#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100 separated by a space.
    Multiples of 3 -> Fizz
    Multiples of 5 -> Buzz
    Multiples of 3 and 5 -> FizzBuzz
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
