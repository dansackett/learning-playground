"""
Threads take a target function to do the work as the thread runs.
"""

import threading

def worker():
    print 'Worker'
    return

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
