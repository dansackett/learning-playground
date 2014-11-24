#!/usr/bin/python

# Smallest multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?
from collections import defaultdict, Counter


def main():
    prime_factorization = defaultdict(int)

    # Loop through numbers 2-19 getting all prime factors excluding 1 and itself
    for x in xrange(2, 20):
        seed = 2
        count = 0
        factors = []
        # Find prime factors of number
        while x != 1:
            while not x % seed:
                x = x / seed
                factors.append(seed)
            seed += 1

        # Count occurances of each prime factor
        counts = Counter(factors)

        # Update prime_factorization so factors are properly reflected
        for key, value in Counter(factors).iteritems():
            if value > prime_factorization[key]:
                prime_factorization[key] = value

    # Get number based on prime factors multiplied by their max exponent
    my_number = 1
    for key, value in prime_factorization.iteritems():
        my_number *= key ** value

    print my_number


if __name__ == '__main__':
    main()
