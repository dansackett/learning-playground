"""
Requires you to download http://www.pythonchallenge.com/pc/def/channel.zip and
place in a directory called 6.

"""

import re
import zipfile

zip = zipfile.ZipFile('channel.zip')

def open_folder(number):
    name = '6/{0}.txt'.format(number)
    file = open(name)
    print zip.getinfo(name)
    return file.read()

def get_next_number(text):
    return re.findall('\s([0-9]+)', text)[0]

number = '90052'

while True:
    try:
        r = open_folder(number)
        number = get_next_number(r)
    except IndexError:
        print r
        break
