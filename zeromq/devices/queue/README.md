# Queue Device

A queue device is an intermediary that sits between a client and server. It
forwards requests to servers and relays replies back back to clients. It
allows you to place the device on a well known port while allowing the client
and server to be dynamic and connect to it.

We can see it here:

```
-------                                   -------
| REQ | -----                       ----- | REP |
-------     |                       |     -------
-------     |       ---------       |     -------
| REQ | ----------> | QUEUE | <---------- | REP |
-------     |       ---------       |      -------
-------     |                       |     -------
| REQ | ----                        ----- | REP |
-------                                   -------
```

This shows the queue essentially as a middleman.
