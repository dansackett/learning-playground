"""
Result collectors are PULL sockets and act as the end consumer grabbing all
results from consumers.
"""
import time
import zmq
import pprint

def result_collector():
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.bind('tcp://127.0.0.1:5558')
    collector_data = {}
    for x in xrange(1000):
        result = receiver.recv_json()
        if collector_data.has_key(result['consumer']):
            collector_data[result['consumer']] = collector_data[result['consumer']] + 1
        else:
            collector_data[result['consumer']] = 1
        if x == 999:
            pprint.pprint(collector_data)

result_collector()
