#!/usr/bin/python

"""
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

        n -> n/2 (n is even) n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

        13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
limit = 1000000
chain_length = 0
longest_chain = 0
best_chain_start = 13
next = 14
link = 13

while next - 1 < limit:
    chain_length += 1

    if link == 1:
        if chain_length > longest_chain:
            longest_chain = chain_length
            best_chain_start = next - 1

        chain_length = 0
        link = next
        next += 1
        continue

    if not link % 2:
        link = link / 2
    else:
        link = 3 * link + 1

print longest_chain
print best_chain_start
