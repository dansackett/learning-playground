#!/usr/bin/python

# Largest palindrome product
# Problem 4
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import time

def main():
    change = base = 999
    solution = False

    while base > 99 and change > 99:
        product = base * change

        if change == 100:
            base -= 1
            change = 999
        else:
            change -= 1

        if str(product) == str(product)[::-1]:
            solution = product if product > solution else solution

    print solution


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = (time.time() - start)
    print "Found in %s seconds" % (elapsed)
