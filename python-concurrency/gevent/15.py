"""
In this example we have the boss running simultaneously to the workers and
have a restriction on the Queue preventing it from containing more than three
elements. This restriction means that the put operation will block until there
is space on the queue. Conversely the get operation will block if there are no
elements on the queue to fetch, it also takes a timeout argument to allow for
the queue to exit with the exception gevent.queue.Empty if no work can be
found within the time frame of the Timeout.
"""

import gevent
from gevent.queue import Queue, Empty

tasks = Queue(maxsize=3)


def worker(name):
    try:
        while True:
            task = tasks.get(timeout=1) # decements queue size by 1
            print 'Worker %s got task %s' % (name, task)
            gevent.sleep(0)
    except Empty:
        print 'Quitting time!'


def boss():
    """
    Boss will wait to hand out work until an individual worker is free since
    the maxsize of the task queue is 3.
    """

    for i in xrange(1, 10):
        tasks.put(i)
    print 'Assigned all work in iteration 1'

    for i in xrange(10, 20):
        tasks.put(i)
    print 'Assigned all work in iteration 2'


gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'bob'),
])
