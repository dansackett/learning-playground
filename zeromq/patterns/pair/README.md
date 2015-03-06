# PAIR Pattern

Provides sockets that act similar to convetional sockets meaning:

- Only strict one-to-one (two peers)
- Many-to-one (many clients, one server)
- One-to-many (multicast)

# Exclusive PAIR Pattern

Communication in a PAIR is bidirectional with no specific state stored in the
socket itself. Only one connected peer where the server listens on a port and
the client connects through that port.

```
-----------------        -----------------
| Client (PAIR) | -----> | Server (PAIR) |
-----------------        -----------------
```

In general, this means that it's easy to setup and we can be sure that we get
the full message on delivery.
