#!/usr/bin/python

"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
number = 600851475143
seed = 2
largest_prime = 1

while number != 1:
    while not number % seed:
        number = number / seed
        largest_prime = seed
    seed += 1

print largest_prime
