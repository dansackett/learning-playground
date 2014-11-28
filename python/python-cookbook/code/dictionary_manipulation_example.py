from collections import defaultdict, OrderedDict, ChainMap
from operator import itemgetter
from itertools import groupby

"""
Using defaultdict and setdefault
"""
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['c'].append(3)

e = {}
e.setdefault('a', []).append(1)
e.setdefault('b', []).append(2)
e.setdefault('c', []).append(3)


"""
Keeping order with dictionaries
"""
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['baz'] = 3


"""
Calculations
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))


"""
We can use set operations with dictionaries to compare
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}

print(a.keys() & b.keys())
# {'y', 'x'}
print(a.keys() - b.keys())
# {'z'}
print(a.items() & b.items())
# {('y', 2)}
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# {'y': 2, 'x': 1}


"""
Sorting based on keys
"""
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))


"""
Grouping by similiar values
"""
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('   ', i)


"""
Looking up in multiple dictionaries
"""
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a, b)
print(c['x'])
# 1
print(c['y'])
# 2
print(c['z'])
# 3
