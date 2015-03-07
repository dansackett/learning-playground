"""
The forwarder allows pub / sub pairs to communicate through a single middleman
instance.
"""
import zmq

def forwarder():
    try:
        context = zmq.Context(1)
        frontend = context.socket(zmq.SUB)
        frontend.bind("tcp://*:5559")

        frontend.setsockopt(zmq.SUBSCRIBE, "")

        backend = context.socket(zmq.PUB)
        backend.bind("tcp://*:5560")

        zmq.device(zmq.FORWARDER, frontend, backend)
    except Exception, e:
        print e
        print "bringing down zmq device"
    finally:
        frontend.close()
        backend.close()
        context.term()

forwarder()
