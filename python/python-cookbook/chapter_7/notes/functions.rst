Functions
=========

Functions can accept args and kwargs::

    def f(*args, **kwargs):
        # prints a tuple
        print(args)

        # prints a dict
        print(kargs)

We can write functions that are called keyword-only arguments. These are good
for when you have a variable number of arguments and you want specific keyword
arguments::

    def recv(maxsize, *, block):
        pass

    print(recv(1024, True))
    # TypeError
    print(recv(1024, block=True))
    # Ok

Functions can also return any number of values. It does so in the form of a
tuple so they can be unpacked easily::

    def f():
        return 1, 2, 3

    a, b, c = f()

When we have a simple operation that can be written in one line, we can turn
to lambda functions::

    >>> names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
    >>> print(sorted(names, key=lambda name: name.split()[-1].lower()))
    ['Ned Batchelder', 'David Beazley', 'Raymond Hettinger', 'Brian Jones']

Lambda functions are most commonly seen paired with functions. They are used
as key functions a lot.

Oftentimes we can convert simple one-method classes with simple closures like
so::

    # from this
    from urllib.request import urlopen

    class UrlTemplate:
        def __init__(self, template):
            self.template = template

        def open(self, **kwargs):
            return urlopen(self.template.format_map(kwargs))

    # to a closure
    def urltemplate(template):
        def opener(**kwargs):
            return urlopen(template.format_map(kwargs))
        return opener

Closures are functions that we can assign to a variable and then we can use
that assigned function as another function basically. So in this case, we
would use it like this::

    yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line.decode('utf-8'))

In the end, closures are cool and actually run a little faster than a standard
class, but can be more confusing and don't give us access to descriptors and
other useful class features. They're good for some circumstances like
callbacks, but otherwise, classes are better.
