"""
We can initialize a greenlet directly or through spawning them.
"""

import gevent
from gevent import Greenlet


def foo(message, n):
    gevent.sleep(n)
    print message


# Initialize a greenlet instance
thread1 = Greenlet.spawn(foo, 'Hello', 1)

# Wrapper for creating and running a new Greenlet
thread2 = gevent.spawn(foo, 'I live!', 2)

thread3 = gevent.spawn(lambda x: (x + 1), 2)

threads = [thread1, thread2, thread3]

# Block until all threads complete
gevent.joinall(threads)
