"""
Producers are PUSH types and are bound to a port for consumers to connect to.
"""
import time
import zmq

def producer():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind('tcp://127.0.0.1:5557')
    for num in xrange(2000):
        message = { 'num': num }
        socket.send_json(message)

producer()
