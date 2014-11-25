#!/usr/bin/python

"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main():
    a = b = 999
    solution = False

    while a > 99 and b > 99:
        product = a * b

        if a == 100:
            a = 999
            b -= 1
        else:
            a -= 1

        if str(product) == str(product)[::-1]:
            solution = product if product > solution else solution

    print solution


if __name__ == '__main__':
    main()
