#!/usr/bin/python

"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

NOTE: This is slow. 7 seconds slow. Haven't thought of a better way yet.
"""
from utils import is_prime

limit = 2000000
current = 3
master_sum = 2

while current < limit:
    if is_prime(current):
        master_sum += current

    current += 2

print master_sum
