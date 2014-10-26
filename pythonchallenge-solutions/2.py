from itertools import groupby, ifilter
from collections import defaultdict

with open('2.txt') as file:
    string = file.read()

counts = defaultdict(int)

# Find character counts
for symbol, value in groupby(sorted(string)):
    for x in value:
        counts[symbol] += 1

# Find all characters that appear once
rare = [x for x, y in counts.items() if y == 1]

# Scan the string again and only print letters if they're rare
print ''.join([letter for letter in string if letter in rare])
