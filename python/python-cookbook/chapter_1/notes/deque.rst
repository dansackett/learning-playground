Creating a simple Queue for deque
=================================

There are a lot of good places to use a queue in programming. One easy way in
python is using::

    from collections import deque

The deque module allows us to create either a fixed size queue or an infinite
size queue. A maxlength queue looks like::

    >>> from collections import deque
    >>> q = deque(maxlen=3)
    >>> q.append(1)
    >>> q.append(2)
    >>> q.append(3)
    >>> q
    deque([1, 2, 3], maxlen=3)
    >>> q.append(4)
    >>> q
    deque([2, 3, 4], maxlen=3)
    >>> q.append(5)
    >>> q
    deque([3, 4, 5], maxlen=3)

As we see, adding a new item to the queue will pop the oldest item to make
room for the new item. We can also do other queue operations::

    >>> from collections import deque
    >>> q = deque()
    >>> q.append(1)
    >>> q.append(2)
    >>> q.append(3)
    >>> q
    deque([1, 2, 3])
    >>> q.appendleft(4)
    >>> q
    deque([4, 1, 2, 3])
    >>> q.pop()
    3
    >>> q
    deque([4, 1, 2])
    >>> q.popleft()
    4
    >>> q
    deque([1, 2])

Why choose a queue over a list?

* Queues can be used well with threads to make threadsafe operations.
* Queues are more elegant than lists
* Queues are faster than lists

Queues are definitely a lesser know Python feature to check out.
