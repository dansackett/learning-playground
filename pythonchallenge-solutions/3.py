import re

with open('3.txt') as file:
    string = file.read()

with open('/usr/share/dict/words') as file:
    dict = set(file.read())

matches = re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', string)
print ''.join(matches)
