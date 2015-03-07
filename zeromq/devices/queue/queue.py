"""
The Queue Device provides an interface for both clients and servers to pass
data back and forth through it.
"""
import zmq

def queue():
    try:
        context = zmq.Context(1)
        frontend = context.socket(zmq.XREP)
        frontend.bind('tcp://*:5559')
        backend = context.socket(zmq.XREQ)
        backend.bind('tcp://*:5560')

        zmq.device(zmq.QUEUE, frontend, backend)
    except Exception, e:
        print e
        print 'Bringing down mq device'
    finally:
        frontend.close()
        backend.close()
        context.term()

queue()
