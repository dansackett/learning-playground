Matching, Splitting, and Searching Text
=======================================

We can split strings in two ways. The first is the simple string.split
method::

    >>> word = 'piano'
    >>> word.split('i')
    ['p', 'ano']

This is useful if all the delimeter are the same but not good when you have a
range of different delimeters. For this we can import the re module for regex
calculations::

    >>> import re
    >>>
    >>> line = 'asdf, fjgh; afed, fjek,asdf,        foo'
    >>> re.split(r'[;,\s]\s*', line)
    ['asdf', 'fjgh', 'afed', 'fjek', 'asdf', 'foo']

Only thing to be careful for is adding a matching group since it will group
them all together with delimeters.

Another nice thing to do with strings is checking what they start and end
with. We have convenient features in string.startswith() and string.endswith()
to make this easy::

    >>> filename = 'spam.txt'
    >>> print(filename.endswith('.txt'))
    True
    >>> print(filename.startswith('file:'))
    False
    >>> url = 'http://www.python.org'
    >>> print(url.startswith('http:'))
    True

This also works with multiple strings::

    >>> import os
    >>> filenames = os.listdir('.')
    >>> print(filenames)
    ['chapter_10', 'chapter_14', 'chapter_4', 'chapter_12', 'chapter_7', 'chapter_9', 'chapter_13', 'chapter_1', 'README.rst', 'chapter_15', 'chapter_8', 'chapter_2', 'chapter_3', 'chapter_11', 'chapter_5', 'chapter_6']
    >>> print([name for name in filenames if name.endswith(('.c', '.h'))])
    []
    >>> print(any(name.endswith('.py') for name in filenames))
    False

Be sure to include the multiple matches in tuple. Anything else will throw and
error oddly enough. We also have access to wildcard searching where we can find matches based on
wildcard string like in a terminal::

    >>> from fnmatch import fnmatch
    >>>
    >>> print(fnmatch('foo.txt', '*.txt'))
    True
    >>> print(fnmatch('foo.txt', '?oo.txt'))
    True
    >>> print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
    True
    >>> names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    >>> print([name for name in names if fnmatch(name, 'Dat*.csv')])
    ['Dat1.csv', 'Dat2.csv']

This won't be work well if case matters. For that, we have the fnmatchcase
function::

    >>> from fnmatch import fnmatchcase
    >>> print(fnmatchcase('foo.txt', '*.TXT'))
    False
    >>> addresses = [
    ...     '5412 N CLARK ST',
    ...     '1060 W ADDISON ST',
    ...     '1039 W GRANVILLE AVE',
    ...     '2122 N CLARK ST',
    ...     '4802 N BROADWAY',
    ... ]
    >>> print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
    ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
    >>> print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] * CLARK')])
    []
    >>> print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
    ['5412 N CLARK ST']

With these tools, searching text becomes much more powerful. Getting back to
regex, the re module has a lot to offer us when we need to solve regex
problems. For instance::

    >>> import re
    >>> date1 = '11/27/2012'
    >>> date2 = 'Nov 27, 2012'
    >>>
    >>> if re.match(r'\d+/\d+/\d+', date1):
    ...     print('yes')
    ... else:
    ...     print('no')
    ...
    yes
    >>> if re.match(r'\d+/\d+/\d+', date2):
    ...     print('yes')
    ... else:
    ...     print('no')
    ...
    no

In this example we use the same pattern twice to find if a match exists. When
we want to reuse a pattern, we can do so with re.compile()::

    >>> datepat = re.compile(r'\d+/\d+/\d+')
    >>> if datepat.match(date1):
    ...     print('yes')
    ... else:
    ...     print('no')
    ...
    yes

When we want to find all matches, we can use re.findall()::

    >>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    >>> print(datepat.findall(text))
    ['11/27/2012', '3/13/2013']

This will return a list of all matches in our string so we can iterate over
them later. When we work with regex though, it's common to want to capture
specific pieces though and for that we can write regular regex capture
strings::

    >>> datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    >>> m = datepat.match(date1)
    >>> print(m.group(0))
    11/27/2012
    >>> print(m.group(1))
    11
    >>> print(m.group(3))
    2012
    >>> print(m.groups())
    ('11', '27', '2012')
    >>> month, day, year = m.groups()
    >>> month
    '11'
    >>> day
    '27'
    >>> year
    '2012'

And when we have multiple instances in our string::

    >>> print(datepat.findall(text))
    [('11', '27', '2012'), ('3', '13', '2013')]
    >>> for month, day, year in datepat.findall(text):
    ...     print('{}-{}-{}'.format(year, month, day))
    ...
    2012-11-27
    2013-3-13

How about replacing strings in strings? We have a few options::

    >>> text = 'yeah, but no, but yeah, but no, but yeah'
    >>> print(text.replace('yeah', 'yep'))
    yep, but no, but yep, but no, but yep
    >>>
    >>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    >>> print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
    Today is 2012-11-27. PyCon starts 2013-3-13.

The first method is string.replace() which will replace all occurances for us.
When we want to do something more complicated though, we can go back to the
trusty re module and use re.sub(). For very complicated replacements and clean
code, we can also use callback functions to work for us::

    >>> from calendar import month_abbr
    >>> def change_date(m):
    ...     mon_name = month_abbr[int(m.group(1))]
    ...     return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
    ...
    >>> print(datepat.sub(change_date, text))
    Today is 27 Nov 2012. PyCon starts 13 Mar 2013.

One last thing we can do is see how many substitutions were made::

    >>> newtext, n = datepat.subn(r'\3-\1-\2', text)
    >>> print(newtext)
    Today is 2012-11-27. PyCon starts 2013-3-13.
    >>> print(n)
    2

The re.subn() functions gives us the amount which could be useful in an
application. When we have to deal with upper and lower case, we can also use
the re module::

    >>> text = 'UPPER PYTHON, lower python, Mixed Python'
    >>> print(re.findall('python', text, flags=re.IGNORECASE))
    ['PYTHON', 'python', 'Python']
    >>> print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
    UPPER snake, lower snake, Mixed snake

When we want to strip text off the beginning and end of a string, we can use
the string.strip() method::

    >>> s = '     hello world  \n'
    >>> print(s.strip())
    hello world
    >>> print(s.lstrip())
    hello world

    >>> print(s.rstrip())
         hello world
    >>>
    >>> t = '-----hello====='
    >>> print(t.lstrip('-'))
    hello=====
    >>> print(t.strip('-='))
    hello

There are a few variations and what's nice is we can specify a string to
strip. This keeps in mind that this is only for beginning and end of the
string. If we want to do anything in the middle, we need to use the
string.replace() method.
