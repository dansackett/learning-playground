import pickle

with open('5.txt') as file:
    string = file.read()

unpickled = pickle.loads(string)

for x in unpickled:
    my_string = ''

    for y in x:
        my_string += y[0] * y[1]

    print my_string
