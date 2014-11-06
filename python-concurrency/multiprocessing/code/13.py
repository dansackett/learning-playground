"""
In situations when a single resource needs to be shared between multiple
processes, a Lock can be used to avoid conflicting accesses.
"""

import multiprocessing
import sys

def worker(lock, stream):
    with lock:
        stream.write('Lock acquired\n')

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    w1 = multiprocessing.Process(target=worker, args=(lock, sys.stdout))
    w2 = multiprocessing.Process(target=worker, args=(lock, sys.stdout))

    w1.start()
    w2.start()

    w1.join()
    w2.join()
