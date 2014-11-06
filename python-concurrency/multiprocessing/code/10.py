"""
A simple way to communicate between process with multiprocessing is to use a
Queue to pass messages back and forth. Any pickle-able object can pass through
a Queue.
"""

import multiprocessing

class MyFancyClass(object):
    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print 'Doing something fancy in %s for %s' % (proc_name, self.name)

def worker(q):
    obj = q.get()
    obj.do_something()

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    queue.put(MyFancyClass('Fancy Dan'))

    queue.close()
    queue.join_thread()
    p.join()
