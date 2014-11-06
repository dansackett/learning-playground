"""
We can use the "with" statement with a lock to do the acquiring and releasing
automatically.
"""

import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)


def worker_with(lock):
    with lock:
        logging.debug('lock acquired via with')

def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('lock acquired directly')
    finally:
        lock.release()

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()

