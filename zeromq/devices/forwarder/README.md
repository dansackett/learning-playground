# Forwarder Device

A forwarder device is the middleman to pub / sub connections. It collects
messages from all publishers and distributes them to subscribers. The model is
exactly the same as the Queue as can be seen below.

```
-------                                       -------
| PUB | -----                           ----- | SUB |
-------     |                           |     -------
-------     |       -------------       |     -------
| PUB | ----------> | FORWARDER | <---------- | SUB |
-------     |       -------------       |     -------
-------     |                           |     -------
| PUB | -----                           ----- | SUB |
-------                                       -------
```

One important thing to note in this model is that we will not want to
subscribe to a particular channel. In this case, the forwarder will send all
subscribers messages from the subscriber.
