"""
Reading and writing JSON data
"""
import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data)
data = json.loads(json_str)

# working with files
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)

from pprint import pprint
pprint(json_str)


"""
Reading JSON into a Python object
"""
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_hook=JSONObject)
print(data.name)
