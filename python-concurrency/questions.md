## What is the GIL and Why Does it Matter?
The GIL (Global Interpreter Lock) exists in CPython which prevents multiple
native threads from executing Python bytecodes at once. It is there because
memory management in CPython is not thread-safe.

The GIL sucks because it prevents multithreaded programs to take advantage of
multiprocesser systems.

## When should you use each of these: **threads**, **greenlets**, **multiprocessing**?
http://learn-gevent-socketio.readthedocs.org/en/latest

## What is the difference between a **thread** and a **greenlet**?
First, we have to define concurrency and parallelism. Concurrecy is when code
can run independently of other code. Parallelism is the execution of
concurrent code simultaneously. So basically, running multiple concurrent
pieces if parellelism. Concurrency is great for breaking problems apart to
allow pieces to be scheduled in parallel. Parallelism is great for CPU-Heavy
things.

Greenlets provide this concurrency but they do not provide parallelism.

The best case to use a Greenlet is when doing network programming. This is
because working with sockets can happen independently. An example of this
would be a proxy.

Threads are concurrent but not parallel. They are best for IO related items
such as webservers but very bad for CPU related items.
