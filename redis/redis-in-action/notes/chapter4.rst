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



4.4: Transactions
-----------------



4.5: Non-Transational Pipelines
-------------------------------



4.6: Performance Considerations
-------------------------------


