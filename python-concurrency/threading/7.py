"""
We can check if a thread is alive with isAlive()
"""

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                   format='(%(threadName)-10s) %(message)s',)

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

d.join(1)
print d.isAlive()
t.join()
