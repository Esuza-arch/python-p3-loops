#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):  # Loop from 10 to 1
        print(i)
    print("Happy New Year!")  # Print the final message


def square_integers(int_list):
    return [x ** 2 for x in int_list]  # Use list comprehension to square each integer

def fizzbuzz():
    for i in range(1, 101):  # Loop from 1 to 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)  # Print the number if it's not a multiple of 3 or 5

