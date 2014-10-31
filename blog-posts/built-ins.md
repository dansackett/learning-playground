With Python, there is a lot of functionality that you can import to make your
apps better. It also comes with a strong batch of "built-ins" that can help
make your life a lot easier.

[Built-ins](https://docs.python.org/2/library/functions.html) in Python are all simple efficient functions
that give you answers to small programming problems. Without further adieu,
I'll jump directly into the examples to show off their diverse features.

## all

The `all()` function allows us to check if all items in a set are true.

```python
truth_values = []
my_values = [1, 2, '3', 4, 5]

for value in my_values:
    truth_values.append(type(value) is int)

print all(truth_values)
# False

print truth_values
# [True, True, False, True, True]
```

In this example, we do a check on each item in our list to see if they are all
of type "int". We then run the results through the all() function to see if we
have all true values. Since we don't, we see false and printing the truth
values list shows us that our third item, '3', is in fact a string.

## any

If you think of the all() function as an "and", then the `any()` function is
considered an "or". It will return true if it finds any true value in a set.
If we use the same code from above, we will see this result:

```python
any(truth_values)
# True
```

In most cases, this will return the opposite of the all() function unless all
values are in fact true then we'd see the same result.

## dict

We know about dictionaries and that we can create them with the `{ }` syntax
but another thing we can do is use the `dict()` function to essentially type
cast a tuple structure into a dict.

```python
dict([('a', 1), ('b', 2), ('c', 3)])
# {'a': 1, 'c': 3, 'b': 2}
```

Since tuples are immutable types, casting them to a dictionary is a good way
to manipulate values. For instance, we could do something like this:

```python
my_tuple = [('a', 1), ('b', 2), ('c', 3)]

my_tuple[0][1] = 6
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

my_dict = dict(my_tuple)
my_dict['a'] = 6

print list(my_dict.items())
[('a', 6), ('c', 3), ('b', 2)]
```

In this example, we see that changing a tuple value is not allowed, but
changing dict values is. So we transform our tuples to a dictionary, edit the
value, and then transform it back into a list of tuples.

## dir

One of the lesser known functions in my opinion is the `dir()` function. It's
an awesome resource when you want to find out what kind of methods are on a
particular object.

```python
my_dict = {'a': 6, 'c': 3, 'b': 2}

print dir(my_dict)
# ['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
# '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get',
# 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem',
# 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
```

Running the dir() function on an object gives us a list of all the available
ways to work with the object. One of my most common things in Python is
opening up an interactive Python console, running dir() on an object, and see
what I can do.

## filter

The `filter()` function is one way to prune down an iterable based on a
qualifying function. I showed off the equivalent in my [itertools](http://programeveryday.com/post/using-python-itertools-to-save-memory/)
post with the `ifilter()` function.

```python
print filter(lambda x: x < 5, xrange(10))
# [0, 1, 2, 3, 4]
```

Here we say "take all items in my range and create a new list with items less
than 5". This is one thing to consider when deciding how to work with iterables.
Using this function is equivalent to a list comprehension:

```python
print [x for x in xrange(10) if x < 5]
# [0, 1, 2, 3, 4]
```

The choice is yours on which you prefer. You'll have this choice a lot in
Python.

## iter

I've done a few posts about generators and standard data types and how
generators are faster in general since values aren't computed until they're
needed. One thing that we can do is convert our basic data type into an
iterable object with the `iter()`function.

```python
my_list = ['a', 'b', 'c', 'd', 'e']
my_iter = iter(my_list)

print my_list
# ['a', 'b', 'c', 'd', 'e']

print my_iter
# <listiterator object at 0x14b2610>
print list(my_iter)
# ['a', 'b', 'c', 'd', 'e']
print list(my_iter)
# []
```

Looking at this, we create a list with letters and then store the iter version
in a variable. When we print the list we see the values. When we print the
iter, we see it's a listiterator object. When we loop through the iter with
the list function, we get our values but doing so again will be empty. This is
how a generator works and shows that the pointer to the current place is at
the end of the sequence so we get nothing.

## len

The `len()` function is a very common one that allows you to get the length of
an an iterable type. It's great for conditional statements that needs strings
or lists of certain lengths to apply something.

```python
print len(xrange(10))
# 10
```

We can use this on lists, sets, tuples, dictionaries, strings, etc. You'll use
it a lot so enjoy the fact that it's only a three letter function.

## locals

Another cool thing that Python does for us is it stores all of the local
variables in a dictionary. So all of the built-in functions, errors, and user
defined variables can be accessed easily. To get them, we can access them
through the `locals()` function.

```python
x = 10
y = 20

print 'X: {x} Y: {y}'.format(**locals())
# X: 10 Y: 20
```

I'm using unpacking syntax to get the values out for the format string. You
can see though that because we defined both x and y in the local scope, we
have them available through the locals() function and can reference them as
variables in the string like `{x}`.

While this can be a great trick for a small app, this can give you issues with
bigger apps that potentially pollute the namespace with variables. Be careful
with it, but know that it exists if you want fast string formatting.

## map

The `map()` function is another one that we have a sibling to from the
itertools module in imap(). It allows us to pass each value in an iterable
through a function to create a new iterable.

```python
print map(lambda x: x**3, xrange(10))
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

As we can see, we cube each number in our list and return a new list with
cubes. It's a nice and efficient solution to updating values in an iterable.
Again, this is another thing that we have choices with as we can also do this
in list comprehension form.

```python
print [x**3 for x in xrange(10)]
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

Again, this is a judgement thing. I'm going to be doing benchmarks in my post
tomorrow to show off the time it takes to compute with built-ins vs list
comprehensions vs itertools.

## max

The `max()` function will take an iterable and return the highest value in the
iterable.

```python
print max([('a', 3), ('b', 2), ('c', 1)])
# ('c', 1)
```

By default, we see that it returns the highest value and in the terms of a
tuple that means looking at the first value. We can update this with a
key function as the second parameter.

```python
print max([('a', 3), ('b', 2), ('c', 1)], key=lambda x: x[1])
# ('a', 3)
```

By using the key function, I specify the second value in our tuple as the sort
value and we get a different value this time.

## min

Of course the opposite of the max() function is the `min()` function. This
will return the lowest value in the iterable.

```python
print min([('a', 3), ('b', 2), ('c', 1)])
# ('a', 3)

print min([('a', 3), ('b', 2), ('c', 1)], key=lambda x: x[1])
# ('c', 1)
```

I used the same code from above but used the min function as we have the
opposite results for each call.

## open

When we want to open a file and work with it in our projects, we use the
simple `open()` function to do so. This will give us a file object.

```python
file = open('load_me.txt', 'r')
print file
# <open file 'load_me.txt', mode 'r' at 0x152bb70>
print file.read()
# Hello, world!
```

We specify a filename and a file mode and if the file exists we get an object
back. If it doesn't, we'll see an IOError. One thing to note is that when we
open a file, we need to manually close it. This is why it is best practice to
use a context manager to handle opening files. I'll be doing a post about
context managers soon, but for now know that open() has a special context
manager that will close the file when you're done with it. We can use them
like so:

```python
with open('load_me.txt', 'r') as file:
    print file.read()

# Hello, world!
```

This will open it, run our command, and then close it. You should always use
open() like this.

## range

One thing I forget is that I use the `range()` function a lot in my posts but
haven't explained it to people who have never seen it. All it does is make an
actual list of values in memory. We can pass three parameters to it.

```python
# range(START, END, STEP)

print range(5, 25, 5)
# [5, 10, 15, 20]
```

If we only specify one value then that's the end value. My example says
"starting at 5, print every fifth number up to 25". Notice that 25 is not
inclusive.

## raw_input

When first learning Python, one of the first things you learn to use is the
`raw_input()` function. It allows us to accept input from a user and save it
as a string value.

```python
user_answer = raw_input('What is your name?\n')
# What is your name?
# Dan
print user_answer
# Dan
```

This is how we can build interactive Python scripts in the terminal for
instance. Always remember that you should use this over the other built-in
`input()` since input() will not transfer the data into a string format.

## reduce

The `reduce()` function allows us to take an iterable and "reduce" it into one
single value based on a function.

```python
print reduce(lambda x, y: x + y, xrange(10))
# 45
```

Take notice of the lambda I'm using. We define two variables, x and y, and
then we add them in the actual function. Reduce works left to right through an
iterable so our first calculation would be 0 + 1. We then would do 1 + 2. We
would then do 3 + 3. This continues until we get to the end where we have 35 +
10 yielding 45 as the result.

We can also set a default initial value as a third parameter like so:

```python
print reduce(lambda x, y: x + y, xrange(10), 20)
# 65
```

This is good if we have an empty list then we would have 20 returned.

## reversed

When we want to reverse a simple iterable, we can use the `reversed()`
function to do so.

```python
print reversed(range(10))
# <listreverseiterator object at 0x7f7466704910>
print list(reversed(range(10)))
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

This gives us an iterator object but when we loop through it to create a true
list then we see that the values are reversed. Nice and simple.

## slice

Slicing in Python is super easy with the `variable[0:10]` syntax. We can also
use the built-in `slice()` function to define a reusable slice.

```python
my_slice = slice(20, 100, 10)

print range(100)[my_slice]
# [20, 30, 40, 50, 60, 70, 80, 90]
```

Why do this? There might be a point where you want to define your slice and
reuse it in different parts of your app. This allows you to do so. I don't see
it very often, but it's nice to know.

## sum

We saw the reduce() function earlier which gave us a value as the result. The
`sum()` function adds all of the items in an iterable and returns a value.

```python
print sum(range(10))
# 45
```

Notice that this is the same result as our reduce() function from above. It's
best to use the sum() function over reduce() if you plan on simply adding the
numbers. This also takes a second parameter as a start value.

## xrange

I've used this a number of times in this post alone and it's because it's
incredibly efficient. The `xrange()` function is a lazy function that
evaluates as it goes meaning we can generate a huge list without worrying
about it being stored in memory.

```python
print xrange(10)
# xrange(10)

print list(xrange(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

See that we get an "xrange object" returned? It's a special lazy function
essentially. In Python 3, the range() function actually uses the xrange()
functionality as it's more performant.

## zip

The `zip()` function is a great little tool for combining multiple iterables
together into a list of tuples.

```python
my_zip = zip(['a', 'b', 'c', 'd', 'e'], xrange(5))

print my_zip
# [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)]

print dict(my_zip)
# {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3}
```

In this example, I did two things. First, I "zipped" two lists together to get
a list of paired tuples. I then used the dict() function to turn those values
into a dictionary. As you can see, transferring values from dictionaries to
tuples and to lists really isn't too tough in Python.

## Conclusion

If we take away anything from these built-in functions it should be that
Python gives us a few good things for free. A few of these are used very often
and some are not. Either way, it's nice to have them in your repertoire.
