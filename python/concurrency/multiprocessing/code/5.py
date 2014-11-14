"""
When we want to wait for the background processes to finish, we can join them.
"""

import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    time.sleep(2)
    print 'Exiting :', p.name, p.pid

def non_daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    print 'Exiting :', p.name, p.pid

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()
