#!/usr/bin/python

"""
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

def main(limit = 4000000):
    last = 1
    current = 2
    total = 0

    while current < limit:
        total += current if not current % 2 else 0
        current, last = current + last, current

    print total


if __name__ == '__main__':
    main()
