"""
There are three different ways we can do timeouts with greenlets.

    1. Try / Except catching a Timeout
    2. ContextManager with Timeout
    3. Timeout arguments
"""

import gevent
from gevent import Timeout

################################
# Basic try / except
################################
# seconds = 10

# timeout = Timeout(seconds)
# timeout.start()


# def wait():
#     gevent.sleep(10)


# try:
#     gevent.spawn(wait).join()
# except Timeout:
#     print 'Could not complete'


################################
# Context manager
################################
# time_to_wait = 5 # seconds

# class TooLong(Exception):
#     pass

# with Timeout(time_to_wait, TooLong):
#     gevent.sleep(10)


################################
# Using timeout arguments
################################
def wait():
    gevent.sleep(2)


timer = Timeout(1).start()
thread1 = gevent.spawn(wait)

try:
    thread1.join(timeout=timer)
except Timeout:
    print 'Thread 1 timed out'



timer = Timeout.start_new(1)
thread2 = gevent.spawn(wait)

try:
    thread2.get(timeout=timer)
except Timeout:
    print 'Thread 2 timed out'



try:
    gevent.with_timeout(1, wait)
except Timeout:
    print 'Thread 3 timed out'
