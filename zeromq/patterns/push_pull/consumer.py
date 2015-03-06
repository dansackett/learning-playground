"""
Consumers are PULL types and connect to producer ports pushing results to a
collector.
"""
import time
import zmq
import random

def consumer():
    consumer_id = random.randrange(1, 10005)
    print 'I am consumer #%s' % consumer_id
    context = zmq.Context()

    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://127.0.0.1:5557')

    sender = context.socket(zmq.PUSH)
    sender.connect('tcp://127.0.0.1:5558')

    while True:
        work = receiver.recv_json()
        data = work['num']
        result = { 'consumer': consumer_id, 'num': data }
        if data % 2 == 0:
            sender.send_json(result)

consumer()
