# Publish / Subscribe Pattern

This is a classic pattern where messages senders (publishers) do not program
the messages to be sent directly to specific receivers (subscribers). Messages
are published without any knowledge of subscribers. In another case,
subscribers listen to the publisher and take messages.

We can see two patterns:

```
-------             -------
| SUB | ----------> | PUB |
-------      |      -------
             |      -------
             -----> | PUB |
                    -------
```

In this scenario, a subscriber looks to multiple channels but the channels
don't really care who's subscribing.

```
-------             -------
| SUB | ----------> | PUB |
-------      |      -------
-------      |
| SUB | ------
-------
```

In this scenario, many subscribers listen to one publisher.
