"""
An event manages a flag that can be set to true with the set() method and
reset to false with the clear() method. The wait() method blocks until the
flag is true.
"""

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

def wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s' % event_is_set)

def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug('wait_for_event_timeout started')
        event_is_set = e.wait(t)
        logging.debug('event set: %s' % event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


e = threading.Event()

t1 = threading.Thread(name='block', target=wait_for_event, args=(e,))
t1.start()

t2 = threading.Thread(name='non-block', target=wait_for_event_timeout, args=(e, 2))
t2.start()

logging.debug('waiting to call Event.set()')
time.sleep(3)
e.set()
logging.debug('event is set')
