"""
An example of how you'd create a pool for gevent which handles many socket
connections.
"""

from gevent.pool import Pool

class SocketPool(object):

    def __init__(self):
        self.pool = Pool(1000)
        self.pool.start()

    def listen(self, socket):
        while True:
            socket.recv()

    def add_handler(self, socket):
        if self.pool.full():
            raise Exception('At maximum pool size')
        else:
            self.pool.spawn(self.listen, socket)

    def shutdown(self):
        self.pool.kill()
