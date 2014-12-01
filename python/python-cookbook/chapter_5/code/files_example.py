"""
Opening a file for read, write, append
"""
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


"""
Managing encoding issues
"""
# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f.read()

# Ignore bad chars entirely
g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
g.read()


"""
Printing with a different separator or line ending
"""
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')


"""
Writing to a file that doesn't exist
"""
with open('test.txt', 'xt') as f:
    f.write('test')


"""
Compressed files
"""
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


"""
Manipulating pathnames
"""
import os
path = '/home/dan/projects/learning-playground/README.rst'

# last component of path
print(os.path.basename(path))

# get directory name
print(os.path.dirname(path))

# join path components
print(os.path.join('tmp', 'data', os.path.basename(path)))

# expand home directory
print(os.path.expanduser('~/projects'))

# split file extension
print(os.path.splitext(path))

# test if path exists
print(os.path.exists(os.path.expanduser('~/projects')))

# Is a regular file
print(os.path.isfile('/etc/passwd'))

# Is a directory
print(os.path.isdir('/etc/passwd'))

# Is a symbolic link
print(os.path.islink('/usr/local/bin/python3'))

# Get the file linked to
print(os.path.realpath('/usr/local/bin/python3'))


"""
Getting a directory listing
"""
import os
names = os.listdir(os.path.expanduser('~/projects'))
print(names)

# glob for finding all files matching pattern
import glob
pyfiles = glob.glob('*.py')
