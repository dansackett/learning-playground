#!/usr/bin/python

"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is:
      12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is:
      (1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640. Find the difference
between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
"""

def main(limit):
    return square_of_sum(limit) - sum_of_squares(limit)


def sum_of_squares(limit):
    return sum(x**2 for x in xrange(1, limit + 1))


def square_of_sum(limit):
    return sum(xrange(1, limit + 1)) ** 2


if __name__ == '__main__':
    print main(100)
