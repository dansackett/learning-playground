# Streamer Device

A streamer devices is the middleman to pipeline patterns. It acts as a broker
that collects tasks from task feeders and supplies them to task workers.

We can see this below:

```
--------                                       --------
| PUSH | ------                         -----> | PULL |
--------      |                         |      --------
--------      |       ------------      |      --------
| PUSH | -----------> | STREAMER | ----------> | PULL |
--------              ------------      |      --------
                                        |      --------
                                        -----> | PULL |
                                               --------
```

In this example we have two sockets pushing data and three consuming it thanks
to the middleman.
