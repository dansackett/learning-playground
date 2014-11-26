"""
Utility Functions
"""
import math


def is_prime(number):
    """
    Check if a number if prime
    """
    if number == 2:
        return True

    if not number % 2:
        return False

    for x in xrange(3, int(math.sqrt(number)) + 1, 2):
        if not number % x:
            return False

    return True


def get_factors(number):
    factor_pairs = ([x, number//x] for x in xrange(1, int(math.sqrt(number)) + 1)
                    if not number % x)
    return set(sum(factor_pairs, []))
