# Push Pull Pattern

Push pull often will be another way of saying a pipeline pattern. With the
push and pull sockets, you may distribute messages to multiple workers
arranged in a pipeline. A push socket will distribute messages to its pull
clients evenly. This is very similar to the producer / consumer model except
consumer results are not pushed upstream but rather downstream to another pull
/ consumer socket.

We can see this in the following diagram:

```
                        CONSUMERS
                     ---------------
              -----> | PULL | PUSH | -----        RESULT
PRODUCER      |      ---------------     |       COLLECTOR
--------      |      ---------------     |       --------
| PUSH | ----------> | PULL | PUSH | ----------> | PULL |
--------      |      ---------------     |       --------
              |      ---------------     |
              -----> | PULL | PUSH | -----
                     ---------------

-------------------------------------------------------->
                        DOWNSTREAM
```

This model allows data to always flow down the pipeline with each stage of the
pipeline being connected to at least one other node. In the case of multiple
connected nodes, data is load-balanced among the connected nodes.
