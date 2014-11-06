"""
A semaphore manages an internal counter which is decremented by each acquire()
call and incremented by each release() call. The counter can never go below
zero; when acquire() finds that it is zero, it blocks, waiting until some
other thread calls release().
"""

import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('running: %s' % self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('running: %s' % self.active)

def worker(s, pool):
    logging.debug('waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(target=worker, name=str(i), args=(s, pool))
    t.start()
