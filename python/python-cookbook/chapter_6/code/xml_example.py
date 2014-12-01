"""
Parsing Simple XML Data
"""
from urllib import request
from xml.etree.ElementTree import parse

u = request.urlopen('http://programeveryday.com/feed')
doc = parse(u)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    link = item.findtext('link')
    print(title)
    print(link)
    print()


"""
Parsing Huge XML Files
"""
from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


"""
Turning a dictionary into XML
"""
from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
        return elem

s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
print(e)

from xml.etree.ElementTree import tostring
print(tostring(e))

e.set('_id','1234')
print(tostring(e))


"""
Reading and Editing an XML File
"""
from xml.etree.ElementTree import parse, Element

doc = parse('chapter_6/pred.xml')
root = doc.getroot()
print(root)

# Removing items
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert after
print(root.getchildren().index(root.find('nm')))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

# Write back to file
doc.write('chapter_6/newpred.xml', xml_declaration=True)
