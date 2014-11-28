Namedtuple for Code Clarity and Easier Tuples
=============================================

Instead of worrying about position with a tuple or list, we can opt to use the
collections.namedtuple call to give us an almost-object making accessing parts
of tuples like a class::

    >>> from collections import namedtuple
    >>>
    >>> Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    >>> sub = Subscriber(addr='dan@gmail.com', joined='2012-10-19')
    >>> print(sub)
    Subscriber(addr='dan@gmail.com', joined='2012-10-19')
    >>> print(sub.addr)
    dan@gmail.com
    >>> print(sub.joined)
    2012-10-19

Namedtuples are good candidates for replacing more memory intensive
dictionaries but they are immutable like tuples so we will run into assignment
issues. We have options though::

    from collections import namedtuple
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
    s = Stock('ACME', 100, 123.45)
    s._replace(shares=75)

Again, this isn't the most efficient data structure, but it's another option
and certainly great for making more readable code overall rather than random
indices.
