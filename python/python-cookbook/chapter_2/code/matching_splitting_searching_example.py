"""
Splitting a string
"""
import re
line = 'asdf, fjgh; afed, fjek,asdf,        foo'
print(re.split(r'[;,\s]\s*', line))



"""
Matching text at the start or end
"""
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

import os
filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in filenames))


"""
Matching with wildcards
"""
from fnmatch import fnmatch

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

from fnmatch import fnmatchcase
print(fnmatchcase('foo.txt', '*.TXT'))
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])


"""
More Regex
"""
date1 = '11/27/2012'
date2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', date1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', date2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(date1):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match(date1)
print(m.group(0))
print(m.group(1))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()

print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))


"""
Replacing strings
"""
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)


"""
Case insensitive regex
"""
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


"""
Stripping Text
"""
s = '     hello world  \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))
