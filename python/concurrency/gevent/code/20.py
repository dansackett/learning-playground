"""
A semphore allows greenlets to limit concurrent access or execution. When a
semaphore reaches 0 it will block until a release is called. A semaphore with
a size of 1 (a bound) is known as a lock.
"""

from gevent import sleep
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore

sem = BoundedSemaphore(2)

def worker1(n):
    sem.acquire()
    print 'Worker %i acquired semaphore' % n
    sleep(0)
    sem.release()
    print 'Worker %i released semaphore' % n

def worker2(n):
    with sem:
        print 'Worker %i acquired semaphore' % n
        sleep(0)
    print 'Worker %i released semaphore' % n


pool = Pool()
pool.map(worker1, xrange(0, 2))
pool.map(worker2, xrange(3, 6))
