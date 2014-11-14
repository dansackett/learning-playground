"""
Creating greenlets is simply done with gevent.spawn.
"""

import gevent

def foo():
    print 'Running in foo'
    gevent.sleep(0)
    print 'Context switch to foo again'


def bar():
    print 'Context switch to bar'
    gevent.sleep(0)
    print 'Context switch back to bar'


gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])
