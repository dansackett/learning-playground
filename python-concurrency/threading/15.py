"""
Conditions allow one of more threads to wait until they have been notified by
another thread.
"""

import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

def consumer(cond):
    """wait for the condition"""
    logging.debug('starting consumer thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    """set up the resource"""
    logging.debug('starting producer thread')
    with cond:
        logging.debug('making resource available')
        cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(target=consumer, name='c1', args=(condition,))
c2 = threading.Thread(target=consumer, name='c2', args=(condition,))
p = threading.Thread(target=producer, name='p', args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()
