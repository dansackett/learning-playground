"""
When joining all greenlets, we get an asynchronous result where things can
happen when they're ready.
"""

import gevent
import random


def task(pid):
    gevent.sleep(random.randint(0, 2) * 0.001)
    print 'Task %s done' % pid


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)


print 'Synchronous'
synchronous()

print 'Asynchronous'
asynchronous()
