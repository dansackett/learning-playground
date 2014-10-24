While it is easy to say that Python will never compare to C, this can also be said of many other languages.

One thing that's nice in Python however is the fact that there are a large number of built-in constructs available to make your programs much more efficient. With iterables and generators, we have data types that can compute numbers when you need them rather than all in one shot. Building these iterable types can be done in a few ways, but today I wanted to talk about the itertools library.

Itertools comes packaged with Python since version 2.3 and it provides a set of functions for working with iterable data sets. In the end, these are functions that will increase performance and avoid side effects with larger data sets.

For all of these functions, you'll want to import from the itertools library like so:

```python
from itertools import chain
```

In the following examples, note that I'll be casting the results to a list to show the result. In cases outside of this post, you don't need to do this unless you need the actual list for something. Without further ado, let's look at the functions.

## chain

When you stumble upon a case where you have multiple iterables and want to combine them into one, the `chain()` function is where you want to look.

```python
from itertools import chain

print list(chain([1, 2, 3], ['a', 'b', 'c']))
# [1, 2, 3, 'a', 'b', 'c']
```

The chain function can take any number of iterables and will return a new iterable which combines the passed in iterables. So in the case above, we have two lists and chain combines them into a single list. This is very similar to adding lists together, but it will return an itertools chain object which computes values when asked for making it better suited for larger lists.

## izip

In python, we already have a `zip()` function in the standard library which combines elements into tuples. The `izip()` function works the same way, but as you can probably guess, it returns an iterable object for a slight performance boost. We can use it like so:

```python
from itertools import izip

print list(izip([1, 2, 3], ['a', 'b', 'c']))
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

## islice

Python provides a few ways to make slices from data sets including the `slice()` function and bracket notation. When you have a large dataset and want to make a large slice, the itertools `islice()` function can be useful.

```python
from itertools import islice

for i in islice(range(10), 5):
    print i
# 0
# 1
# 2
# 3
# 4

for i in islice(range(10), 5, 10):
    print i
# 5
# 6
# 7
# 8
# 9

for i in islice(range(100), 0, 100, 10):
    print i
# 0
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
```

The islice() function works the same as the slice() function. The first parameter is an iterable object. The second parameter is a starting index. The third parameter is the end index. The final parameter is a step or a number to skip after each iteration. Above are three examples on how these results look.

## tee

With iterables, looping through them once will exhaust the values leaving us with an empty list. We can of course create a new iterable if we need it or we can create multiple instances of the same iterable. For the second option, the itertools `tee()` function can help us.

```python
from itertools import tee
i1, i2, i3 = tee(xrange(10), 3)
print i1
# <itertools.tee object at 0x2a1fc68>
print list(i1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print list(i1)
# []
print list(i2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print list(i2)
# []
print list(i3)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print list(i3)
# []
```

The tee() function takes two parameters. The first is an iterable and the second is the number of copies you'd like to make. With Python's multiple assignment, we can assign each created iterable to a different variable. As we can see, each iterable that we create can be iterated through separately giving us a few instances to play with in the case that we exhaust one.

One thing to be careful with is if you assign your base iterable to a variable like so:

```python
from itertools import tee
r = (x for x in range(10) if x < 6)
print r
# <generator object <genexpr> at 0x2a22870>
i1, i2, i3 = tee(r, 3)
print list(r)
# [0, 1, 2, 3, 4, 5]
print list(i1)
# []
print list(i2)
# []
print list(i3)
# []
```

If you don't see what's happened, let me explain. We assign the variable r to a generator. When we call the `tee()` function we use the variable r to copy our generator to new variables. The issue is that since we have assigned r as our generator, all new variables will be a reference to r. When we exhaust r then all of our other tee variables are exhausted as well. 

Always, always, always be careful with references!

## imap

Like the izip() function, the itertools `imap()` function matches its counterpart `map()` but provides a more memory efficient interface. If you haven't used the map() function, the purpose of it is to send each item in an iterable through a function to create a new iterable. 

```python
from itertools import imap

print list(imap(lambda x: x * x, xrange(10)))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## starmap

Carrying similar functionality as the imap() function, the `starmap()` function provides a different way of using functions across iterables. In this case, the starmap() function expects a list of tuples to manipulate.

```python
from itertools import starmap
print list(starmap(lambda x,y: (x, y, x * y), [(1, 4), (2, 4), (3, 4), (4, 4)]))
# [(1, 4, 4), (2, 4, 8), (3, 4, 12), (4, 4, 16)]
```

In our lambda, we define x and y as the pieces of the tuple and create a resulting tuple with the third entry being the product of the two.

## count

There are times in programming where we don't necessarily know the max number we want to iterate. For instance, we may not know the upper bound to finding a high prime number through iteration. For this, we need an indefinite counter object that can continue producing output for us. This is what the `count()` function does.

```python
from itertools import count
for number, letter in izip(count(0, 10), ['a', 'b', 'c', 'd', 'e']):
    print '{0}: {1}'.format(number, letter)
# 0: a
# 10: b
# 20: c
# 30: d
# 40: e
```

In this example, we can see how the count() function is similar to the range function except it only accepts two arguments compared to three. This is because we can define the start and a step but we cannot define a stop since count() is continuous until stopped. We stop it in this example by zipping it with a list of defined items.

## cycle

Like the count() function, the `cycle()` function is continuous. Instead of progressing in a sequence though, it takes an iterable and loops through it over and over until the function is stopped. 

```python
from itertools import cycle
for number, letter in izip(cycle(range(2)), ['a', 'b', 'c', 'd', 'e']):
    print '{0}: {1}'.format(number, letter)
# 0: a
# 1: b
# 0: c
# 1: d
# 0: e
```

We define our cycle() function with a `range(2)` iterable to give us numbers zero and one. We zip that with our list of letters a-e and can see that the range function cycles to accommodate the size of our list. Pretty cool.

## repeat

Ever need to print the same thing on every line? The itertools `repeat()` function creates an iterable with items that are repeated either indefinitely or with a limit.

```python
from itertools import repeat
print list(repeat('Hello, world!', 3))
# ['Hello, world!', 'Hello, world!', 'Hello, world!']
```

In this example, we define a limit of three times to repeat. Our end result is a list with "Hello, world!" three times. Again, this works similarly as the count() and cycle() function in that without a limit, it will indefinitely repeat.

## dropwhile

Getting into the filtering functions from the itertools module, the first is the `dropwhile()` function which takes a filtering function as the first argument and an iterable for the second. The end result is a little funny as it doesn't filter by the condition exactly. It returns items only after the condition is false. An example can make this clearer:

```python
from itertools import dropwhile
print list(dropwhile(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1]))
# [11, 34, 66, 100, 1]
```

Our condition is numbers less than 10. As we loop through our iterable, we see that the first number greater than 10 is in fact 11. So our new iterable picks up with 11 and continues through the end of the list. See how it also picked up 1 at the end? This is because we aren't filtering the function based on numbers less than 10, but really we want all numbers after the condition is false.

## takewhile

The `takewhile()` function is the exact opposite of the dropwhile() function from above. It will return an iterable with numbers that meet the condition but once the condition is false then it will stop.

```python
from itertools import takewhile
print list(takewhile(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1]))
# [1, 4, 6, 7]
```

Looking at the end result, we stopped at 7 because 11 is larger than 10. We never make it to the 1 on the end of the iterable.

## ifilter

For filtering like you're used to with the filter() function, we have the equivalent `ifilter()` function. Like it's built-in counterpart, it will create a new iterable based on items that match a condition.

```python
from itertools import ifilter
print list(ifilter(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1]))
# [1, 4, 6, 7, 1]
```

Unlike the above two functions, the ilfilter() function gives us our final 1 since the condition doesn't stop after it is false.

## ifilterfalse

The opposite of the ifilter() function which doesn't have a counterpart in the built-ins is the `ifilterfalse()` function. This will return an iterable with items that do not match the condition.

```python
from itertools import ifilterfalse
print list(ifilterfalse(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1]))
# [11, 34, 66, 100]
```

Very straightforward stuff.

## groupby

One of the coolest functions for me in the itertools module is the `groupby()` function. This function allows us to group items based on a key. So for instance, I wrote a [post](http://programeveryday.com/post/writing-better-python-code/) where one of my examples was a list of tuples that had a test taker's name and their score for a test. They could take the test any number of times so the problem was we wanted to group the test takers scores. This was what we did in that example:

```python
from collections import defaultdict

counts = defaultdict(list)
attempts = [('dan', 87), ('erik', 95), ('jason', 79), ('erik', 97), ('dan', 100)]

for (name, score) in attempts:
    counts[name].append(score)

print counts
# defaultdict(<type 'list'>, {'dan': [87, 100], 'jason': [79], 'erik': [95, 97]})
```

This example is clean and elegant in my opinion. We can do this same thing with the itertools groupby() function. 

```python
from operator import itemgetter
from itertools import groupby

attempts = [
    ('dan', 87),
    ('erik', 95),
    ('jason', 79),
    ('erik', 97),
    ('dan', 100)
]

# Sort the list by name for groupby
attempts.sort(key=itemgetter(0))

# Create a dictionary such that name: scores_list
print {key: sorted(map(itemgetter(1), value)) for key, value in groupby(attempts, key=itemgetter(0))}
# {'dan': [87, 100], 'jason': [79], 'erik': [95, 97]}
```

Looking at our above example, we see a few things. For one, I'm using the `operator.itemgetter()` function for key functions. I prefer this syntax over lambda when I can use it. If you've never seen it before, it essentially equates to `lambda x: x[0]` where in a key function, this would use the item at the zero index as the point of sorts / grouping.

Before I get to the groupby in this example, I sort the attempts by the name. This is essential with groupby which is somewhat of a drawback. The groupby() function will cosume items as it goes and if you want it to properly group then you need the items sorted.

Getting to the meat of it, I have a dictionary comprehension which does a few things. Let's break it down some:

* Our for loop is creating a key and a value from attempts that we want grouped by the first item in the tuple, the name.
* Once we have those values, we define our item output which is a new dictionary with a name as the key.
* Our value is going to be sorted. This will allow us to return test scores in a list from low to high.
* We use the map function to specify what the value looks like. By default, the value from the groupby is actually the individual tuples from attempts. We only want to show the score in our resulting list so we use the map() function to say return a new list comprised of the score only.

All of this gets us to the same place as we were with the defaultdict (minus the sorting).

The question begs to be asked, why do this over the defaultdict solution?

In reality, the defaultdict solution is probably the better solution if you have a smaller dataset. It is efficient and will save you some thinking when it comes to your final result. That said, if you have an entire school district worth of SAT score attempts, you may want to think about performance. These could be tens of thousands of records depending on your local population and using some of the c-like functions will compute much more efficiently in the end. 

It all comes down to what you're processing.

## Conclusion

I wanted to end on that last point because when you are looking at these functions, it's easy to say that you can do these computations in other ways. While true, think about these as big data processors that will give you a boost on performance and save your system from potential locks. These functions are all very simple and when combined can be incredibly powerful tools.

If you're interested in learning more about the itertools module, check out the [Python Module of the Week](http://pymotw.com/2/itertools/) page for it. It has everything that I talked about with some other examples.
