"""
An example PAIR Server Socket which sends and listens for messages from a
Client Socket.
"""
import zmq
import random
import sys
import time

port = '5556'
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind('tcp://*:%s' % port)

while True:
    socket.send('Server message to client')
    msg = socket.recv()
    print msg
    time.sleep(1)
