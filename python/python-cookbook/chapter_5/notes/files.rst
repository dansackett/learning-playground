File Operations
===============

When reading and writing files, we should use a contextmanager to managing
opening and closing. This way we don't have memory leaks::

    # Reading
    with open('README.rst', 'rt') as f:
        for line in f:
            print line,
        # data = f.read()

    # Writing
    with open('test.rst', 'wt') as f:
        f.write('Test')

    # Appending
    with open('test.rst', 'at') as f:
        data = f.read()

The different file modes correspond to "read text", "write text", and "append
text". When we are worried about encoding errors, we can set some parameters
to help us::

    # Replace bad chars with Unicode U+fffd replacement char
    f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
    f.read()

    # Ignore bad chars entirely
    g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
    g.read()

Here, we can either replace the errors with a character or we can ignore them
entirely. Either way, we will avoid encoding errors.

Randomly in this chapter, we have a note on the print function and ways we can
use it to output different line endings and separators::

    >>> print('ACME', 50, 91.5)
    ACME 50 91.5
    >>> print('ACME', 50, 91.5, sep=',')
    ACME,50,91.5
    >>> print('ACME', 50, 91.5, sep=',', end='!!\n')
    ACME,50,91.5!!

In Python 2.7, this is a manual thing you have to handle so it's nice to see
in Python 3.3. Also in Python 3 only, we have an 'xt' filemode which will
create and write to a file if it doesn't exist::

    with open('test.txt', 'xt') as f:
        f.write('test')

Working with compressed files of bz2 and gzip can be done with the similiarly
named modules::

    # gzip compression
    import gzip
    with gzip.open('somefile.gz', 'rt') as f:
        text = f.read()

    with gzip.open('somefile.gz', 'wt') as f:
        f.write(text)

    # bz2 compression
    import bz2
    with bz2.open('somefile.bz2', 'rt') as f:
        text = f.read()

    with bz2.open('somefile.bz2', 'wt') as f:
        f.write(text)

When working with paths in the operating system, we can use the os.path module
and the various functions available in it::

    >>> import os
    >>> path = '/home/dan/projects/learning-playground/README.rst'
    >>> print(os.path.basename(path))
    README.rst
    >>> print(os.path.dirname(path))
    /home/dan/projects/learning-playground
    >>> print(os.path.join('tmp', 'data', os.path.basename(path)))
    tmp/data/README.rst
    >>> print(os.path.expanduser('~/projects'))
    /home/dan/projects
    >>> print(os.path.splitext(path))
    ('/home/dan/projects/learning-playground/README', '.rst')
    >>> print(os.path.exists(os.path.expanduser('~/projects')))
    True
    >>> print(os.path.isfile('/etc/passwd'))
    True
    >>> print(os.path.isdir('/etc/passwd'))
    False
    >>> print(os.path.islink('/usr/local/bin/python3'))
    False
    >>> print(os.path.realpath('/usr/local/bin/python3'))
    /usr/local/bin/python3

This is elegant because os.path knows the differences between unix and windows
file systems. When working with directories, we can get a listing of it::

    import os
    names = os.listdir(os.path.expanduser('~/projects'))
    print(names)

    # glob for finding all files matching pattern
    import glob
    pyfiles = glob.glob('*.py')

Glob is best for pattern matching but we can also use fnmatch.fnmatch() as
well. listdir will give us all files/directories in the directory.

Most of the chapter deals with binary files and binary text. I'm not
particularly interested in this right now so I'll come back to it someday.
