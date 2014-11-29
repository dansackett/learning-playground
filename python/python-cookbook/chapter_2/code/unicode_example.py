"""
Normalizing Unicode Strings
"""
import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))


"""
Utility testing unicode
"""
s1 = 'Spicy Jalape\u00f1o'
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))


"""
Unicode Digits
"""
import re
num = re.compile('\d+')
print(num.match('123'))
print(num.match('\u0661\u0662\u0663'))
