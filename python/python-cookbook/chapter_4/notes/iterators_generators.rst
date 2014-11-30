Iterators and Generators
========================

When defining an iterator, all we have to do is ensure that we have an
__iter__ method on our object. This allows us to loop through a defined set of
items in the iteration::

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

We define the __iter__ method and now we can call it and iterate through the
children nodes in this example. Very straightforward. Of course, the __iter__
method will expect you set and iter() on a list, tuple, etc.

When we want to create new iterator functions, generators should be used to
give us an indefinite continuation::

    >>> def frange(start, stop, increment):
    ...     x = start
    ...     while x < stop:
    ...         yield x
    ...         x += increment
    ...
    >>> for n in frange(0, 4, 0.5):
    ...     print(n)
    ...
    0
    0.5
    1.0
    1.5
    2.0
    2.5
    3.0
    3.5

If a function has a yield in it, then it is a generator by definition. We can
see how a generator works with the following example::

    >>> def countdown(n):
    ...     print('Starting to count from', n)
    ...     while n > 0:
    ...         yield n
    ...         n -= 1
    ...     print('Done!')
    ...
    >>> c = countdown(3)
    >>> c
    <generator object countdown at 0x7ff046991f50>
    >>> next(c)
    Starting to count from 3
    3
    >>> next(c)
    2
    >>> next(c)
    1
    >>> next(c)
    Done!
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

As we can see, when a generator is initialized, nothing happens. Until we call
the next() function on it, we don't get anything back. This is a lazy
function. On the first call, we see out start message but all subsequent calls
until the end do not output this start call. This is because the function
saves state and begins again at the yield statement. This concept allows you
to create efficient programs. To note, once a generator is used up then you
will have to recreate it to iterate through it again. This is still because of
the function starting at the yield statement when there's nothing to yield.

When defining iterators on an object, you should always do so as a generator.
It makes it far less complicated and works really well.

How about reverse iteration? We can do this with the reversed() function::

    >>> a = [1, 2, 3, 4]
    >>> for x in reversed(a):
    ...     print(x)
    ...
    4
    3
    2
    1

Note that we can call reversed on any object that has a definite length or
that we can call __len__ on. If it doesn't have a length, like a generator,
then we will have to cast it to a list or something first which is memory
intensive. For those, cases, you can define your own reversed method::

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

How about when we want to pass state in a generator? We can use a class to do
this where the generator is in the __iter__ method giving us access to class
attributes and methods::

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

    with open('somefile.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

One thing that people have trouble with using generators is the fact that you
can't take a slice from them. This isn't true. All we have to do is use the
itertools.islice() function to do this for us::

    >>> from itertools import islice
    >>>
    >>> def count(n):
    ...     while True:
    ...         yield n
    ...         n += 1
    ...
    >>> c = count(0)
    >>> print(c[10:20])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'generator' object is not subscriptable
    >>>
    >>> for x in islice(c, 10, 20):
    ...     print(x)
    ...
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19

The result of islice() is an iterator that produces the desired slice items,
but it does this by consuming and discarding all of the items up to the
starting slice index. Further items are then produced by the islice object
until the ending index has been reached.

A good example of something you would do in programming is read a file and
print the file contents. How about if we want to get rid of all the
boilerplate comments in the beginning? We can use the itertools.dropwhile()
function for this::

    >>> from itertools import dropwhile
    >>> with open('/etc/passwd') as f:
    ...     for line in dropwhile(lambda line: line.startswith('#'), f):
    ...         print(line, end='')

This will ignore the lines that match the statement and when the statement is
false, it will start outputting them.

A lot of times when there are multiple sets and you want to do the same
operation when iterating, people will write two identitcal loops to do so. We
can do this much easier with itertools.chain()::

    >>> from itertools import chain
    >>> a = [1, 2, 3, 4]
    >>> b = ['x', 'y', 'z']
    >>> for x in chain(a, b):
    ...     print(x)
    ...
    1
    2
    3
    4
    x
    y
    z

This will act as if they are on iterable but will in fact just give us one
loop instead of the identical multiples.

A cool example of using generators to help with memory intensive filesystem
tasks can be seen here on
`line 165 <https://github.com/dansackett/learning-playground/tree/master/python/python-cookbook/chapter_4/code/iterators_generators_example.py>`_

One nice thing in Python 3 is the yield from command. This will actually save
you a for loop and will process an iterable's values for you. We can see it
here::

    >>> from collections import Iterable
    >>> def flatten(items, ignore_types=(str, bytes)):
    ...     for x in items:
    ...         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
    ...             yield from flatten(x)
    ...         else:
    ...             yield x
    ...
    >>> items = [1, 2, [3, 4, [5, 6], 7], 8]
    >>> for x in flatten(items):
    ...     print(x)
    ...
    1
    2
    3
    4
    5
    6
    7
    8

In this case, we use yield from to output values from our nested iterable.

Iterating in a sorted manner can be done using the invaluable heapq module::

    >>> import heapq
    >>> a = [1, 4, 7, 10]
    >>> b = [2, 5, 6, 11]
    >>> for x in heapq.merge(a, b):
    ...     print(x)
    ...
    1
    2
    4
    5
    6
    7
    10
    11

Take note that the sequences must individually be sorted first for this method
to work for us. One super cool thing that should be happening instead of
infinite while loops is using the iter() function to process data::

    import sys
    with open('/etc/passwd') as f:
        for chunk in iter(lambda: f.read(10), ''):
            n = sys.stdout.write(chunk)

The iter() function takes a zero argument callable at the start and a
terminating sequence as well making it infinitely work for us. This will
return results until it matches the sentinal termination sequence and then
die. So cool.
