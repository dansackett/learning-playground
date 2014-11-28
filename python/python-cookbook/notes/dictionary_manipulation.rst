Dictionary Manipulations
========================

When working with dictionaries, it's common to want to set a key to multiple
values. The elegant solutions are with defaultdict and setdefault::

    >>> from collections import defaultdict
    >>> d = defaultdict(list)
    >>> d['a'].append(1)
    >>> d['a'].append(2)
    >>> d['a'].append(3)
    >>> d
    defaultdict(<class 'list'>, {'a': [1, 2, 3]})
    >>>
    >>> e = {}
    >>> e.setdefault('a', []).append(1)
    >>> e.setdefault('a', []).append(2)
    >>> e.setdefault('a', []).append(3)
    >>> e
    {'a': [1, 2, 3]}

Of the two, defaultdict is the more Pythonic and more elegant solution in my
opinion. One thing to note is that both have drawbacks.

* defaultdict will create keys when accessing something which may not be ideal
* setdefault creates a list object on every call which is a slight memory hit

Either way, there are better solutions than::

    d = {}
    for key, value in items:
        if key not in d:
            d[key] = []
        d[key] = value

This is far from elegant.

Another thing to worry about with dictionaries is sorting and working with
values. By default, dicts sort on keys. We can do some value work with a few
functions::

    >>> prices = {
    ...     'ACME': 45.23,
    ...     'AAPL': 612.78,
    ...     'IBM': 205.55,
    ...     'HPQ': 37.20,
    ...     'FB': 10.75
    ... }
    >>> min_price = min(zip(prices.values(), prices.keys()))
    >>> max_price = max(zip(prices.values(), prices.keys()))
    >>> prices_sorted = sorted(zip(prices.values(), prices.keys()))
    >>> min_price
    (10.75, 'FB')
    >>> max_price
    (612.78, 'AAPL')
    >>> prices_sorted
    [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

One important note about zip() is that it creates a one-tiem iterator so you'l
exhaust it after one iteration meaning you must re-zip for each calculation.

Another cool thing with dictionaries is we can use set operations on keys to
manipulate them and find commonalities across other dictionaries::

    >>> a = {
    ...     'x': 1,
    ...     'y': 2,
    ...     'z': 3,
    ... }
    >>>
    >>> b = {
    ...     'w': 10,
    ...     'x': 11,
    ...     'y': 2,
    ... }
    >>> a.keys() & b.keys()
    {'y', 'x'}
    >>> a.keys() - b.keys()
    {'z'}
    >>> a.items() & b.items()
    {('y', 2)}
    >>> c = {key:a[key] for key in a.keys() - {'z', 'w'}}
    >>> c
    {'y': 2, 'x': 1}

One thing with sorting dictionaries as well is we can use the sorted()
function with a key function. For this, we use the operator.itemgetter
callable as it is efficient and more succinct than a lambda expression in a
lot of cases::

    >>> from operator import itemgetter
    >>> rows = [
    ...     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    ...     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    ...     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    ...     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
    ... ]
    >>> rows_by_fname = sorted(rows, key=itemgetter('fname'))
    >>> rows_by_fname
    [{'lname': 'Jones', 'uid': 1004, 'fname': 'Big'}, {'lname': 'Jones', 'uid': 1003, 'fname': 'Brian'}, {'lname': 'Beazley', 'uid': 1002, 'fname': 'David'}, {'lname': 'Cleese', 'uid': 1001, 'fname': 'John'}]
    >>> rows_by_uid = sorted(rows, key=itemgetter('uid'))
    >>> rows_by_uid
    [{'lname': 'Cleese', 'uid': 1001, 'fname': 'John'}, {'lname': 'Beazley', 'uid': 1002, 'fname': 'David'}, {'lname': 'Jones', 'uid': 1003, 'fname': 'Brian'}, {'lname': 'Jones', 'uid': 1004, 'fname': 'Big'}]

A little unknown feature similiar to itemgetter is the operator.attrgetter
which works well with sorting objects based on their properties::

    from operator import attrgetter
    sorted(users, key=attrgetter('user_id'))

Another cool thing to do is to group items in a dictionary based on similiar
values. For this, we can use itertools.groupby::


    >>> from itertools import groupby
    >>> rows = [
    ...     {'address': '5412 N CLARK', 'date': '07/01/2012'},
    ...     {'address': '5148 N CLARK', 'date': '07/04/2012'},
    ...     {'address': '5800 E 58TH', 'date': '07/02/2012'},
    ...     {'address': '2122 N CLARK', 'date': '07/03/2012'},
    ...     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    ...     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    ...     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    ...     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ... ]
    >>> rows.sort(key=itemgetter('date'))
    >>>
    >>> for date, items in groupby(rows, key=itemgetter('date')):
    ...     print(date)
    ...     for i in items:
    ...         print('   ', i)
    ...
    07/01/2012
        {'date': '07/01/2012', 'address': '5412 N CLARK'}
        {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
    07/02/2012
        {'date': '07/02/2012', 'address': '5800 E 58TH'}
        {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}
        {'date': '07/02/2012', 'address': '1060 W ADDISON'}
    07/03/2012
        {'date': '07/03/2012', 'address': '2122 N CLARK'}
    07/04/2012
        {'date': '07/04/2012', 'address': '5148 N CLARK'}
        {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}

This is a great way to group data and extract certain things. You must have
the data sorted before using groupby for it to work though since groupby
combines items that are similiar in a row. Of course, you have to evaluate
your needs and your data first because sorting and iterating to get this
result takes more memory than simply storing a dictionary with the date as the
key.

Another nice feature in the collections module is the ChainMap function which
will allow us to use multiple dictionaries to look up values::

    >>> from collections import ChainMap
    >>> a = {'x': 1, 'z': 3 }
    >>> b = {'y': 2, 'z': 4 }
    >>> c = ChainMap(a, b)
    >>> print(c['x'])
    1
    >>> print(c['y'])
    2
    >>> print(c['z'])
    3

This is better than updating a dictionary with another since this preserves
the original mappings.
