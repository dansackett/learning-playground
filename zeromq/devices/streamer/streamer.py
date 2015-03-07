"""
The streamer helps feed pushes down a pipeline to pullers.
"""
import zmq

def streamer():
    try:
        context = zmq.Context(1)
        frontend = context.socket(zmq.PULL)
        frontend.bind('tcp://*:5559')
        backend = context.socket(zmq.PUSH)
        backend.bind('tcp://*:5560')

        zmq.device(zmq.STREAMER, frontend, backend)
    except Exception, e:
        print e
        print 'Bringing down zmq device'
    finally:
        frontend.close()
        backend.close()
        context.term()

streamer()
