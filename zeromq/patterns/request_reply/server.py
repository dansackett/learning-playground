"""
A basic reply server will wait for a request and send back a message once it
receives that request.
"""
import zmq
import time
import sys

port = '5556'
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:%s' % port)

while True:
    # This will block until reply comes
    message = socket.recv()
    print 'Received Request: ', message
    time.sleep(1)
    socket.send('World from %s' % port)
