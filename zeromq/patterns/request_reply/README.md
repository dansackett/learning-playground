# Request Reply Pattern (Client / Server)

The most basic pattern is a request and reply pattern in which a client sends
a request and the server sends back a response to the request. The main
differences between this and the `zmq.PAIR` socket are:

- `zmq.REQ` can connect to many servers
- The request will be distributed to all servers
- `zmq.REQ` will block on send unless it gets a reply back
- `zmq.REP` will block on recv unless it receives a request

We can see this in a diagram with one client making requests on a
load-balanced server:

```
-------             -------
| REQ | ----------> | REP |
-------     |       -------
            |       -------
            ------> | REP |
                    -------
```

In the diagram, each request is answered with a reply.
