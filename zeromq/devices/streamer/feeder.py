"""
The feeder pushes messages downstream.
"""
import time
import zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.connect('tcp://127.0.0.1:5559')
    for num in xrange(20000):
        work_message = { 'num' : num }
        zmq_socket.send_json(work_message)
        time.sleep(1)

producer()
