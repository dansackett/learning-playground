"""
Continuing with synchronous VS. asynchronous, we see that it's useful when
going over HTTP since some items may have longer loads than others and we
won't block our greenlets.
"""

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import json

def fetch(pid):
    response = urllib2.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
