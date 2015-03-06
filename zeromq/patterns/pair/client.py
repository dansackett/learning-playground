"""
An example PAIR Client Socket which sends and listens for messages from a
Server Socket.
"""
import zmq
import random
import sys
import time

port = '5556'
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect('tcp://localhost:%s' % port)

while True:
    msg = socket.recv()
    print msg
    socket.send('Client message to server')
    socket.send('Client message 2 to server')
    time.sleep(1)
