"""
The basics of creating a new process. With processes, we want to make sure
that we wrap the process spawning in a "main block" so that the program is not
run recursively in each child as the target module is imported.
"""

import multiprocessing

def worker():
    print 'Worker'
    return

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        p.start()
