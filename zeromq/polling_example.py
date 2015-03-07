"""
In the case that we have many socket connections we want to satisfy, polling
is the best way to handle this. In this example, we have a server that signals
when a worker should exit.
"""
import zmq
import time
import sys
import random
from multiprocessing import Process


def server_push(port='5556'):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind('tcp://*:%s' % port)
    print 'Running server on port: ', port

    for reqnum in range(10):
        if reqnum < 6:
            socket.send('Continue')
        else:
            socket.send('Exit')
            break
        time.sleep(1)


def server_pub(port='5558'):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:%s' % port)
    publisher_id = random.randrange(0, 9999)
    print 'Running server on port: ', port

    for reqnum in range(10):
        topic = random.randrange(8, 10)
        messagedata = 'server#%s' % publisher_id
        print '%s %s' % (topic, messagedata)
        socket.send('%d %s' % (topic, messagedata))
        time.sleep(1)


def client(port_push, port_sub):
    context = zmq.Context()
    socket_pull = context.socket(zmq.PULL)
    socket_pull.connect('tcp://localhost:%s' % port_push)
    print 'Connected to server with port %s' % port_push
    socket_sub = context.socket(zmq.SUB)
    socket_sub.connect('tcp://localhost:%s' % port_sub)
    socket_sub.setsockopt(zmq.SUBSCRIBE, '9')
    print 'Connected to publisher with port %s' % port_sub

    poller = zmq.Poller()
    poller.register(socket_pull, zmq.POLLIN)
    poller.register(socket_sub, zmq.POLLIN)

    should_continue = True
    while should_continue:
        socks = dict(poller.poll())
        if socket_pull in socks and socks[socket_pull] == zmq.POLLIN:
            message = socket_pull.recv()
            print 'Received control command %s' % message
            if message == 'Exit':
                print 'Received exit command, client will stop receiving messages'
                should_continue= False

        if socket_sub in socks and socks[socket_sub] == zmq.POLLIN:
            string = socket_sub.recv()
            topic, messagedata = string.split()
            print 'Processing...', topic, messagedata


if __name__ == '__main__':
    server_push_port = '5556'
    server_pub_port = '5558'
    Process(target=server_push, args=(server_push_port,)).start()
    Process(target=server_pub, args=(server_pub_port,)).start()
    Process(target=client, args=(server_push_port, server_pub_port,)).start()
