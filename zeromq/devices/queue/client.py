"""
The client simply sends messages to the device.
"""
import zmq
import sys
import random

port = '5559'
context = zmq.Context()
print 'Connecting to server...'
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:%s' % port)
client_id = random.randrange(1, 10005)

for request in range(1, 10):
    print 'Sending request ', request, '...'
    socket.send('Hello from %s' % client_id)
    message = socket.recv()
    print 'Received reply ', request, '[', message, ']'
