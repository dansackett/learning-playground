Unicode Strings
===============

Since unicode strings can be created in a few different ways, it's best to
normalize them before checking against another::

    >>> import unicodedata
    >>>
    >>> s1 = 'Spicy Jalape\u00f1o'
    >>> s2 = 'Spicy Jalapen\u0303o'
    >>> print(s1)
    Spicy Jalapeño
    >>> print(s2)
    Spicy Jalapeño
    >>> print(s1 == s2)
    False
    >>> t1 = unicodedata.normalize('NFC', s1)
    >>> t2 = unicodedata.normalize('NFC', s2)
    >>> print(t1 == t2)
    >>> print(ascii(t1))
    'Spicy Jalape\xf1o'
    >>>
    >>> t3 = unicodedata.normalize('NFD', s1)
    >>> t4 = unicodedata.normalize('NFD', s2)
    >>> print(t3 == t4)
    True
    >>> print(ascii(t3))
    'Spicy Jalapen\u0303o'

In these examples, we see two modes. NFC means characters should be fully
composed or try to use one character. NFD means uncomposed and use multiple
characters. When cleaning, it can be good to get rid of combining characters
so search is in plain english::

    >>> s1 = 'Spicy Jalape\u00f1o'
    >>> t1 = unicodedata.normalize('NFD', s1)
    >>> print(''.join(c for c in t1 if not unicodedata.combining(c)))
    Spicy Jalapeno

This cleans the unicode characters and gives us an easy to search repr. When
working with digits, we are in luck as re.match() already matches on unicode
as we can see here::

    >>> import re
    >>> num = re.compile('\d+')
    >>> print(num.match('123'))
    <_sre.SRE_Match object at 0x7fd0d6c1bb90>
    >>> print(num.match('\u0661\u0662\u0663'))
    <_sre.SRE_Match object at 0x7fd0d6c1bb90>

In the end, regex and unicode can be tough. It's best to look at a third-party
solutions to do it for you.
