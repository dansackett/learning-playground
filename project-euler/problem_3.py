#!/usr/bin/python

"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def main():
    NUMBER = 600851475143
    SEED = 2
    largest_prime = 1

    while NUMBER != 1:
        while not NUMBER % SEED:
            NUMBER = NUMBER / SEED
            largest_prime = SEED
        SEED += 1

    print largest_prime


if __name__ == '__main__':
    main()
