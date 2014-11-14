"""
Threads can pass args to their target functions.
"""

import threading

def worker(n):
    print 'Worker %s' % n
    return

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
