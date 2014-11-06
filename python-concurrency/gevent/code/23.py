"""
Gevent subprocesses support cooperative waiting on a subprocess.
"""

import gevent
from gevent.subprocess import Popen, PIPE


def cron():
    while True:
        print 'Cron'
        gevent.sleep(0.2)


g = gevent.spawn(cron)
sub = Popen(['sleep 1; uname'], stdout=PIPE, shell=True)
out, err = sub.communicate()
g.kill()
print out.rstrip()
