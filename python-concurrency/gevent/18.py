"""
A pool is a structure designed for handling dynamic numbers of greenlets which
need to be concurrency-limited. This is often desirable in cases where one
wants to do many network or IO bound tasks in parallel.
"""

import gevent
from gevent.pool import Pool

pool = Pool(2)

def hello_from(n):
    print 'Size of pool %s' % len(pool)


pool.map(hello_from, xrange(3))
