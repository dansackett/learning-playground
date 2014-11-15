#!/usr/bin/python

# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

import time

def main():
    x = 2520
    solution = False

    while not solution:
        values = all([x % num == 0 for num in range(1, 21)])

        if not values:
            x += 1
        else:
            solution = True

        print x

        1 - 1
        2 - 2
        3 - 3
        4 - 2**2
        y5 - 5
        6 - 2*3
        y7 - 7
        y8 - 2**3
        y9 - 3**2
        10 - 2*5
        y11 - 11
        12 - 2*2*3
        y13 - 13
        14 - 2*7
        15 - 3*5
        16 - 2**2*2**2
        y17- 17
        18 - 2*2**3
        y19 - 19
        20 - 2*2*5


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = (time.time() - start)
    print "Found in %s seconds" % (elapsed)
