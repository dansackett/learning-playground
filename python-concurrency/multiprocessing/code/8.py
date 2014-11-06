"""
We can use multiprocessing built-in logging to give us a detailed look at
what's happening with our processes.
"""

import multiprocessing
import sys
import logging

def worker():
    print 'Doing work'
    # Flushing stdout will ensure that the message is printed when we want it to
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    # logger = multiprocessing.get_logger()
    # logger.setLevel(logging.INFO)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
