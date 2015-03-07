"""
In most instances, we can easily spin up our clients and servers on different
processes and run it in one call. Multiprocessing is awesome. This of course
wasn't possible when having a running while loop, but when we have a set time
or size then we're OK.
"""
import zmq
import time
import sys
from multiprocessing import Process


def server(port='5559'):
    """Our Server is a reply type"""
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:%s' % port)
    print 'Running server on port: ', port

    for reqnum in range(5):
        message = socket.recv()
        print 'Received request#%s: %s' % (reqnum, message)
        socket.send('World from %s' % port)


def client(ports=['5559']):
    """The client is a request type"""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    for port in ports:
        socket.connect('tcp://localhost:%s' % port)

    for request in range(20):
        print 'Sending request ', request
        socket.send('Hello')
        message = socket.recv()
        print 'Received reply ', request, '[', message, ']'
        time.sleep(1)


if __name__ == '__main__':
    ports = range(5550, 5558, 2)
    for port in ports:
        Process(target=server, args=(port,)).start()

    Process(target=client, args=(ports,)).start()
