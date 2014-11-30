"""
Defining an iterator on a class
"""
class Node:
    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for ch in root:
    print(ch)


"""
Defining new iteration pattern with a generator
"""
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)


"""
Adding a generator to our Node class
"""
class Node:
    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
for ch in root.depth_first():
    print(ch)


"""
Iterating in reverse
"""
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)


"""
Defining your own reverse iterator
"""
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n

for x in Countdown(4):
    print(x)


"""
Passing more state with generators
"""
from collections import deque
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('README.rst') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')


"""
Slicing an iterator
"""
from itertools import islice

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
# print(c[10:20])

for x in islice(c, 10, 20):
    print(x)


"""
Dropwhile
"""
from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')


"""
Iterating over multiple sets
"""
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)


"""
Creating a processing pipeline
"""
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
    yield f
    f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
        yield line

# lognames = gen_find('access-log*', 'www')
# files = gen_opener(lognames)
# lines = gen_concatenate(files)
# pylines = gen_grep('(?i)python', lines)
# for line in pylines:
# print(line)


"""
Flatten a sequence
"""
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)


"""
Sorted order iterating
"""
import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for x in heapq.merge(a, b):
    print(x)


"""
Replacing infinite while loops with an iterator
"""
CHUNKSIZE = 8192
# def reader(s):
#     while True:
#         data = s.recv(CHUNKSIZE)
#         if data == b'':
#             break
#         process_data(data)

# replace with
# def reader(s):
#     for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
#         process_data(data)

# or

import sys
with open('/etc/passwd') as f:
    for chunk in iter(lambda: f.read(10), ''):
        n = sys.stdout.write(chunk)
