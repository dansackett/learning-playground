"""
We can listen for SIGQUIT events to kill long running greenlets.
"""

import gevent
import signal


def run_forever():
    gevent.sleep(1000)


if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.kill)
    thread = gevent.spawn(run_forever)
    thread.join()
