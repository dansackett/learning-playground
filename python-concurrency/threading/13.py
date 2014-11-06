"""
More on using locks.
"""

import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

def lock_holder(lock):
    logging.debug('starting')
    while True:
        lock.acquire()
        try:
            logging.debug('holding')
            time.sleep(0.5)
        finally:
            logging.debug('not holding')
            lock.release()
        time.sleep(0.5)
    return

def worker(lock):
    logging.debug('starting')
    num_tries = 0
    num_acquires = 0

    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d acquired' % num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteration %d not acquired' % num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations' % num_tries)

lock = threading.Lock()
holder = threading.Thread(target=lock_holder, args=(lock,), name='LockHolder')
holder.setDaemon(True)
holder.start()

worker = threading.Thread(target=worker, args=(lock,), name='Worker')
worker.start()
