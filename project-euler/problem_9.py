#!/usr/bin/python

"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

        For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main(limit):
    for a in xrange(3, limit):
        for b in xrange(a + 1, limit):
            c = limit - (a + b)

            if a + b > limit:
                continue

            if c <= b:
                continue

            if sum([a, b, c]) == 1000 and (a**2 + b**2) == c**2:
                print reduce(lambda x, y: x * y, [a, b, c])


if __name__ == '__main__':
    main(1000)
