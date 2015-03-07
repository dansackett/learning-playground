# ZeroMQ (ØMQ)

ØMQ (also known as ZeroMQ, 0MQ, or zmq) looks like an embeddable networking
library but acts like a concurrency framework. It gives you sockets that carry
atomic messages across various transports like in-process, inter-process, TCP,
and multicast. You can connect sockets N-to-N with patterns like fan-out,
pub-sub, task distribution, and request-reply. It's fast enough to be the
fabric for clustered products. Its asynchronous I/O model gives you scalable
multicore applications, built as asynchronous message-processing tasks. It has
a score of language APIs and runs on most operating systems. ØMQ is from
iMatix and is LGPLv3 open source.


## Install

We can grab ZeroMQ on Ubuntu from the following PPA:

```
$ add-apt-repository ppa:chris-lea/zeromq
$ apt-get update
$ apt-get install zeromq-bin libzmq-dev libzmq0
```

Once we have it, we can find a client library to mess with. In my playing
around I used [pyzmq](https://github.com/zeromq/pyzmq).
