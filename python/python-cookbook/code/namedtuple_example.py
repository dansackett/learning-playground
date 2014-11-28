from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber(addr='dan@gmail.com', joined='2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
