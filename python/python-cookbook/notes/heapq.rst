Priority Queues and n Smallest and Largest with heapq
=====================================================

The heapq module is a very efficient solution to finding largest and smallest
values in a collection of data::

    >>> import heapq
    >>> nums = [1, 5, 8, 9, 0, 24, -3, 6]
    >>> heapq.nlargest(3, nums)
    [24, 9, 8]
    >>> heapq.nsmallest(3, nums)
    [-3, 0, 1]

This is a great way to find the smallest and largest items. It also takes a
key function to work with dictionaries::

    >>> portfolio =[
    ...     {'name': 'IBM', 'shares': 100, 'price': 91.1},
    ...     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    ...     {'name': 'FB', 'shares': 200, 'price': 21.09},
    ...     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    ...     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    ...     {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ... ]
    >>> cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    >>> expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    >>>
    >>> cheap
    [{'price': 16.35, 'shares': 45, 'name': 'YHOO'}, {'price': 21.09, 'shares': 200, 'name': 'FB'}, {'price': 31.75, 'shares': 35, 'name': 'HPQ'}]
    >>> expensive
    [{'price': 543.22, 'shares': 50, 'name': 'AAPL'}, {'price': 115.65, 'shares': 75, 'name': 'ACME'}, {'price': 91.1, 'shares': 100, 'name': 'IBM'}]

When using these features, the actual work going on under the hood looks
something like this::

    >>> import heapq
    >>> nums = [1, 5, 8, 9, 0, 24, -3, 6]
    >>> heap = list(nums)
    >>> heapq.heapify(heap)
    >>> heap
    [-3, 0, 1, 6, 5, 24, 8, 9]

We convert the sequence into a heap which gives us the following
posibilities::

    >>> heapq.heappop(heap)
    -3
    >>> heapq.heappop(heap)
    0
    >>> heapq.heappop(heap)
    1
    >>> heap
    [5, 6, 8, 24, 9]

These operations will update our heap and give us the subsequent smallest
value. One thing to note is that when you want to simply find the single
smallest or single largest item, min() and max() are much more efficient
functions. For a range or smallest and largest though, heapq is great.

When we want to work with priority queues, we should take into account this
structure::

    (-priority, index, item)

The reasoning for each piece:

* We negate the priority in order to sort the items with highest first
* We have an index to help sort when items have the same priority
* The item is the item itself

This structure can be seen `here </learning-playground/python/python-cookbook/code/heapq.py>`_.
