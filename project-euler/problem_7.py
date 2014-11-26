#!/usr/bin/python

"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10,001th prime number?
"""
from utils import is_prime

limit = 10001
current = 1
count = 1

while count < limit:
    current += 2
    if is_prime(current):
        count += 1

print current
