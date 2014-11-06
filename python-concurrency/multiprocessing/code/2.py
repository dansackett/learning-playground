"""
Passing args to a process is different than passing args to a thread. The
argument must be able to be serialized for it to work correctly.
"""

import multiprocessing

def worker(num):
    print 'Worker %s' % num
    return

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
