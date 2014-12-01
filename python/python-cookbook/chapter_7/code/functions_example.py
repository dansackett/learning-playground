"""
Function that accept any number of args
"""
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3, 4))

# Any number of kwargs
import html
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

print(make_element('item', 'Albatross', size='large', quantity=6))


"""
Keyword-only arguments
"""
def recv(maxsize, *, block):
    pass

print(recv(1024, True))
# TypeError
print(recv(1024, block=True))
# Ok


"""
Returning multiple values
"""
def f():
    return 1, 2, 3

a, b, c = f()


"""
Lambdas
"""
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))


"""
Replacing one-method classes with closures
"""
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

# used like
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
