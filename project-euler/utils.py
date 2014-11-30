"""
Utility Functions
"""
import math
import time
import functools


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
    """
    Get all of the factors for a given number
    """
    factor_pairs = ([x, number//x] for x in xrange(1, int(math.sqrt(number)) + 1)
                    if not number % x)
    return set(sum(factor_pairs, []))


def timer(func):
    @functools.wraps(func)
    def wrapper():
        start = time.time()
        func()
        end = time.time() - start
        print 'It took {end} seconds'.format(**locals())

    return wrapper

class Fib:
    """
    Generate the fibonacci terms
    """
    def __init__(self, limit):
        self.limit = limit
        self.total = 0
        self.last = 1
        self.current = 2

    def __iter__(self):
        while self.current < self.limit:
            yield self.current
            self.current, self.last = self.current + self.last, self.current

    def sum(self):
        for x in self:
            self.total += x
        return self.total

    def sum_even(self):
        for x in self:
            self.total += x if not x % 2 else 0
        return self.total

    def sum_odd(self):
        for x in self:
            self.total += x if x % 2 else 0
        return self.total
