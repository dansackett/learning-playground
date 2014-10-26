import requests
import re

def request(number):
    return requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(number))

def get_next_number(text):
    return re.findall('\s([0-9]+)', text)[0]

number = '12345'

while True:
    try:
        r = request(number)

        number = get_next_number(r.text)
        print number
    except IndexError:
        number = int(number) / 2
        break

while True:
    try:
        r = request(number)

        number = int(get_next_number(r.text)) / 2
        print number
    except IndexError:
        print r.text
        break
