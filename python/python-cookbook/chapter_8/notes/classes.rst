All About Classes
=================

When working with a class, we can set the string representation of it with two
methods. The first is the __str__ method which converts the instance to a
string and is used when str() is called on the class or when used with print().
The second is __repr__ which is the code representation of the class. The
repr() function returns this as does the interpretor.

When working with the format() function, we can define the __format__ method
on our class::

    _formats = {
        'ymd' : '{d.year}-{d.month}-{d.day}',
        'mdy' : '{d.month}/{d.day}/{d.year}',
        'dmy' : '{d.day}/{d.month}/{d.year}'
    }

    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

        def __format__(self, code):
            if code == '':
                code = 'ymd'
            fmt = _formats[code]
            return fmt.format(d=self)

    d = Date(2012, 12, 21)
    print(format(d))
    print(format(d, 'mdy'))
    print('The date is {:ymd}'.format(d))
    print('The date is {:mdy}'.format(d))

This is useful and makes sense.

One nice thing is making your own contextmanagers. Contextmanagers are using
the with keyword and open and close things typically. What we have to do is
define an __enter__ and __exit__ method on our class to support the
contextmanager. As well, we can use the contextlib module and write a
generator that handles this.

When we have a class that primarily serves as a data structure, we can define
a __slots__ method on it to help reduce memory::

    class Date:
        __slots__ = ['year', 'month', 'day']

        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

The __slots__ attribute will store the attributes in a simple data structure
like a tuple instead of a dictionary. One side effect of this is that you
cannot add new attributes without placing the attributes in the __slots__
list. This isn't an every day solution, but really good for a class you
frequently use as a data structure.

For classes that want to create private methods through encapsulation, we go
by honor rather than convention. Python doesn't support true encapsulation, so
instead Python programmers stick to the following conventions:

* A single underscore before for attrs and methods means private (internal)
* A double underscore before for attrs and methods that may be private and subclassed
* A single underscore after for a Python builtin override

When these occur, programmers should know that their use is internal and if
used outside of that scope then results may vary.

Another thing we can do with classes are create managed attributes. For this,
we use the @property decorator::

    class Person:
        def __init__(self, first_name):
            self.first_name = first_name

        # Getter function
        @property
        def first_name(self):
            return self._first_name

        # Setter function
        @first_name.setter
        def first_name(self, value):
            if not isinstance(value, str):
                raise TypeError('Expected a string')
            self._first_name = value

        # Deleter function (optional)
        @first_name.deleter
        def first_name(self):
            raise AttributeError("Can't delete attribute")

We should do this when we want to add built-in validation and tests before
settings, deleting, etc. Also, it allows us to do more complex logic when
getting an attribute. The setter and deleter attrs on the property will not
exist without defining the property itself first. You should only define a
property like this if you need to do checking as this will add complexity for
no reason and slow down the processing. They are however good for computed
attributes::

    import math
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @property
        def area(self):
            return math.pi * self.radius ** 2

        @property
        def perimeter(self):
            return 2 * math.pi * self.radius

These are dynamic and a property is great for this cases to make calculations
less complex.

When we want to subclass a class, we can call the super() function like so::

    class A:
        def __init__(self):
            self.x = 0

    class B(A):
        def __init__(self):
            super().__init__()
            self.y = 1

This calls the parent instance for us which allows us to do the original
function and then do what we want to after it so we don't break anything.

One awesome feature in Python are descriptors. A descriptor is a class that
implements the three core attribute access operations (get, set, and delete)
in the form of __get__(), __set__(), and __delete__() special meth‐ ods. These
methods work by receiving an instance as input. The underlying dictionary of
the instance is then manipulated as appropriate.

To use a descriptor, instances of the descriptor are placed into a class
definition as class variables. For example::

    class Integer:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError('Expected an int')
            instance.__dict__[self.name] = value

        def __delete__(self, instance):
            del instance.__dict__[self.name]

    class Point:
        x = Integer('x')
        y = Integer('y')
        def __init__(self, x, y):
            self.x = x
            self.y = y

When you do this, all access to the descriptor attributes (e.g., x or y) is
captured by the __get__(), __set__(), and __delete__() methods. For example::

    >>> p = Point(2, 3)
    >>> p.x
    # Calls Point.x.__get__(p,Point)
    2
    >>> p.y = 5
    # Calls Point.y.__set__(p, 5)
    >>> p.x = 2.3
    # Calls Point.x.__set__(p, 2.3)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "descrip.py", line 12, in __set__
    raise TypeError('Expected an int')
    TypeError: Expected an int

This is a POWERFUL feature. You can customize the getter, setter, and deleter
methods and get a lot of control. One important note is that a descriptor must
be a class attribute rather than formulated in an __init__() method.

The reason __get__() looks somewhat complicated is to account for the
distinction between instance variables and class variables. If a descriptor is
accessed as a class vari‐ able, the instance argument is set to None. In this
case, it is standard practice to simply return the descriptor instance itself
(although any kind of custom processing is also allowed).

It should be stressed that you would probably not write a descriptor if you
simply want to customize the access of a single attribute of a specific class.
For that, it’s easier to use a property instead. Descriptors are more useful
in situations where there will be a lot of code reuse (i.e., you want to use
the functionality provided by the descriptor in hundreds of places in your
code or provide it as a library feature).

Moving on, something that happens a lot is setting up multiple __init__()
methods that are very boilerplate. We can avoid this with a common base
class::

    class Structure:
        # Class variable that specifies expected fields
        _fields= []

        def __init__(self, *args):
            if len(args) != len(self._fields):
                raise TypeError('Expected {} arguments'.format(len(self._fields)))

            # Set the arguments
            for name, value in zip(self._fields, args):
                setattr(self, name, value)

    # Example class definitions
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x','y']

    class Circle(Structure):
        _fields = ['radius']

        def area(self):
            return math.pi * self.radius ** 2

    s = Stock('ACME', 50, 91.1)
    p = Point(2, 3)
    c = Circle(4.5)

This allows us to define classes faster. Another pattern is defining a true
abstract base class::

    from abc import ABCMeta, abstractmethod

    class IStream(metaclass=ABCMeta):
        @abstractmethod
        def read(self, maxbytes=-1):
            pass

        @abstractmethod
        def write(self, data):
            pass

This acts more like an interface in the end and any class that inherits from
it will require the @abstractmethods. We can also check if classes are
instances of this with::

    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')

This gives us control over what we should expect for this class.
