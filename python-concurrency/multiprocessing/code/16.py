"""
The Manager is responsible for coordinating shared information state between
all of its users.

By creating the list through the manager, it is shared and updates are seen in
all processes. Dictionaries are also supported.
Any named value added to the Namespace is visible to all of the clients that receive the Namespace instance.
"""

import multiprocessing

def worker(d, key, value):
    d[key] = value

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(d, i, i*2)) for i in
           range(10)]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print 'Results:', d
