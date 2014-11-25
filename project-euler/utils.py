"""
Utility Functions
"""
def is_prime(number):
    """Check if a number if prime"""
    if number == 2:
        return True

    if not number % 2:
        return False

    for x in xrange(3, int(number**.5) + 1, 2):
        if not number % x:
            return False

    return True
