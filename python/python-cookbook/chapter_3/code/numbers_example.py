"""
Rounding
"""
print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(-1.25432, 3))
a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))


"""
Decimals
"""
from decimal import Decimal, localcontext
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))

c = Decimal('1.3')
d = Decimal('1.7')
print(c / d)
with localcontext() as ctx:
    ctx.prec = 3
    print(c / d)

with localcontext() as ctx:
    ctx.prec = 50
    print(c / d)


"""
Fractions
"""
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)
c = a * b
print(c.numerator)
print(c.denominator)
print(float(c))
print(c.limit_denominator(8))
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)


"""
Numpy
"""
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

def f(x):
    return 3*x**2 - 2*x + 7
print(f(ax))
print(np.sqrt(ax))
print(np.cos(ax))

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])
print(a[:,1])
print(a[1:3, 1:3])


"""
Random
"""
import random
values = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choice(values))
print(random.sample(values, 3))
random.shuffle(values)
print(values)
print(random.randint(0, 10))
print(random.random())
print(random.getrandbits(200))
