"""
A group is a collection of running greenlets which are managed and scheduled
together as group. It also doubles as parallel dispatcher that mirrors the
Python multiprocessing library.
"""

import gevent
from gevent.pool import Group


def talk(msg):
    for i in xrange(3):
        print msg

g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')
g3 = gevent.spawn(talk, 'fizz')

group = Group()
group.add(g1)
group.add(g2)
group.join()

group.add(g3)
group.join()
