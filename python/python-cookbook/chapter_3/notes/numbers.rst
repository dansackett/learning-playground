Numbers
=======

We can round numbers easily::

    >>> print(round(1.23, 1))
    1.2
    >>> print(round(1.27, 1))
    1.3
    >>> print(round(-1.27, 1))
    -1.3
    >>> print(round(-1.25432, 3))
    -1.254
    >>> a = 1627731
    >>> print(round(a, -1))
    1627730
    >>> print(round(a, -2))
    1627700
    >>> print(round(a, -3))
    1628000

The round() function will always attempt to round the number to the nearest
whole integer where 2.5 will become 2. If you provide a negative number as the
rounding digit, then it will round to the nearest tens, hundreds, thousands,
etc.

Of course we shouldn't round simply to print a number. We can format it::

    >>> x = 1.23456
    >>> print(format(x, '0.2f'))
    1.23

When dealing with floating point numbers, computers can get things wrong. This
is no different in Python but can be dealt with when using the decimal.Decimal
module::

    >>> from decimal import Decimal
    >>> a = Decimal('4.2')
    >>> b = Decimal('2.1')
    >>> print(a + b)
    6.3
    >>> print((a + b) == Decimal('6.3'))
    True

Do note that the Decimal module is more performance intensive. We can manage
the local presicion with the decimal.localcontext contextmanager::

    >>> from decimal import localcontext
    >>> c = Decimal('1.3')
    >>> d = Decimal('1.7')
    >>> print(c / d)
    0.7647058823529411764705882353
    >>> with localcontext() as ctx:
    ...     ctx.prec = 3
    ...     print(c / d)
    ...
    0.765
    >>> with localcontext() as ctx:
    ...     ctx.prec = 50
    ...     print(c / d)
    ...
    0.76470588235294117647058823529411764705882352941176

While less common in programming, we can work with fractions with the
fractions.Fraction class::

    >>> from fractions import Fraction
    >>> a = Fraction(5, 4)
    >>> b = Fraction(7, 16)
    >>> print(a + b)
    27/16
    >>> print(a * b)
    35/64
    >>> c = a * b
    >>> print(c.numerator)
    35
    >>> print(c.denominator)
    64
    >>> print(float(c))
    0.546875
    >>> print(c.limit_denominator(8))
    4/7
    >>> x = 3.75
    >>> y = Fraction(*x.as_integer_ratio())
    >>> print(y)
    15/4

When we want to really do complex math, we should always lean to the more
performany numpy library. We can pip install numpy to use it and do a lot. It
uses a lot of the techniques that make C fast and is the reason why scientists
can use Python for calculations. For examples, check out
`this sample <https://github.com/dansackett/learning-playground/tree/master/python/python-cookbook/chapter_3/code/numbers_example.py>`_

When we want to deal with randomness, we can use the random module::

    >>> import random
    >>> values = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> print(random.choice(values))
    4
    >>> print(random.sample(values, 3))
    [8, 4, 7]
    >>> random.shuffle(values)
    >>> print(values)
    [6, 5, 7, 8, 2, 1, 3, 4]
    >>> print(random.randint(0, 10))
    2
    >>> print(random.random())
    0.2042380982002564
    >>> print(random.getrandbits(200))
    1336606407196115011942182703983664515591283256287339344053906

Notice that this is not great for crypto and something like the ssl module
should be used instead.
