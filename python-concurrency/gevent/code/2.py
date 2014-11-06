"""
Select will block the current greenlet.
"""

import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)


def gr1():
    print 'Started polling: %s' % tic()
    select.select([], [], [], 2)
    print 'Ended polling: %s' % tic()


def gr2():
    print 'Started polling: %s' % tic()
    select.select([], [], [], 2)
    print 'Ended polling: %s' % tic()


def gr3():
    print 'Doing stuff while greenlets poll, %s' % tic()
    gevent.sleep(1)


gevent.joinall([gevent.spawn(gr1), gevent.spawn(gr2), gevent.spawn(gr3),])
