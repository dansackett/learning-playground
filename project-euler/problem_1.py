#!/usr/bin/python

"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
limit = 1000
print sum(x for x in xrange(limit) if not x % 3 or not x % 5)
