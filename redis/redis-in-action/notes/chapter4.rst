Chapter 4: Keeping Data Safe and Persisting
===========================================

All about how Redis works behind the scenes and ways to maintain data.

4.1: Persistence
----------------

Two forms of persisting data: snapshotting which take the data at the current
moment and writes it to disk, and AOF (append-only file) which copies incoming
write commands as they happen to disk. You can use them either together or
separately.

With Snapshots, data lost between snapshots will be lost forever in the result
of a failure. We can initiate snapshots by:

- Use the ``BGSAVE`` command. This works on platforms other than Linux and
  will fork the parent process working alongside it to create the snapshot.
- Use the ``SAVE`` command. This is a blocking call and will take the main
  process and use it to create the snapshot.
- ``save`` Config variable will do a ``BGSAVE``. For instance if in config
  ``save 60 10000`` will run if 10000 writes have occurred within the last 60
  seconds of the last successful save.
- When Redis gets the ``SHUTDOWN`` command or it receives a standard ``TERM``
  signal, it will do a blocking ``SAVE`` call.
- If one Redis server connects to another and issues a ``SYNC`` command then
  the master service will do a ``BGSAVE`` call

For applications where losing data is not good, we should not snapshot.
Otherwise, snapshotting is a good approach.

In development, a good setting for snapshotting is ``save 900 1`` which means
if 1 write has occured in the last 15 minutes since the last ``BGSAVE``
succeeded. It's really a touch and feel game here as each project differs.

With AOF, will append our new writes to a file that can be replayed in the
event of a failure. When using the ``appendfsync``, we have three options for
it:

- always: Every write command goes to disc and this slows Redis a lot.
- everysec: Happens once every second
- no: Operating system handles the syncing

A good way to go here is with ``everysec`` so at most we'd only lose a second
of data. It doesn't crush performance in most instances either. Of course
filesize is the big problem when it comes to AOF though. If we're appending
to a file, it will grow exponetially in time. We can use the ``BGREWRITEAOF``
option which will rewrite our AOF file making it less redundant. This also is
like using ``BGSAVE`` which forks the process but the difference is that once
the file is rewritten, the old file must be discarded possibly slowing the
system down more. Thankfully, we have ``auto-aof-rewrite-percentage`` and
``auto-aof-rewrite-min-size`` to allow us to manage the AOF rewrites properly.

A value of 100 for ``auto-aof-rewrite-percentage`` will perform the rewrite
when the AOF is 100% larger than it was when Redis last wrote the AOF. A value
of 64mb for ``auto-aof-rewrite-min-size`` will work when the AOF is at least
64mb in size.

Either way, we have to be concerned about replication if we really want the
data to stick.

4.2: Replication
----------------

With Redis, we can use slave instances to help us manage higher levels of
commands per second. When we connect a slave instance, the ``BGSAVE`` command
will be run to sync the data.

We set up slave instances with the ``slaveof host port`` option. By setting
this up, the work will essentially be done for us with Redis which is nice.
What really happens is the master will start a snapshot and then send that to
the slave instance. It's a good idea to have masters use 50-65% memory for
reads and writes and another 30-45% for ``BGSAVE`` operations.

What's nice is that we can have slaves of slaves to aid performance and
spreadthe load out.

4.3: System Failures
--------------------

When dealing with system failures, we have two commands we can run from the
terminal. ``redis-check-aof --fix`` for AOF and ``redis-check-dump`` for snapshots.

If things hae royally gone to shit, we can replace a master instance. The
scenario is as follows:

- Machine A goes down.
- Machine B is a slave to machine A.
- Machine C is a fresh Redis Server that we want to be the new master.

To make the transition we could do something like::

    Machine-B: $ redis-cli
        redis > SAVE
        OK
        redis > QUIT
    Machine-B: $ scp /var/local/redis/dump.rdb MACHINE_C:/var/local/redis/dump.rdb
    Machine-B: $ ssh MACHINE_C
    Machine-C: $ sudo /etc/init.d/redis-server start
    Machine-C: $ exit
    Machine-B: $ redis-cli
        redis > SLAVEOF MACHINE_C 6379
        OK
        redis > QUIT
    Machine-B: $ exit

We can also choose to make the slave the new master and create a new slave
instance. Either way, the transition isn't too bad. Today, Redis Sentinels can
be used to monitor these things and handle failover which isn't until chapter
10.

4.4: Transactions
-----------------

We can think of Redis transactions as thread locks. They help avoid data
corruption and also can be good for performance. To use them, we start a batch
of commands with ``MULTI`` and the commands aren't run until ``EXEC`` is run.
It is also known as pipelining and helps improve performance because it
reduces the number of round trips back and forth to Redis.

Another command we can use to handle 'thread-safe' like features is the
``WATCH`` command. When we watch a key, if anyone alters the key in the middle
of a transaction block, then the transaction will fail.

4.5: Non-Transational Pipelines
-------------------------------

When we want to send more than one command to Redis, the result of one command
doesn't affect another, and we don't care to execute all of these
transactionally, we can pass false to a ``pipeline`` to save even more on
performance.
