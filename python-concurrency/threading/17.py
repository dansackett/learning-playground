"""
Thread-local data are data whose values are thread specific.
"""

import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('no value yet')
    else:
        logging.debug('value=%s' % val)

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

local_data = threading.local()
show_value(local_data)
local_data.value = 1000
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()
