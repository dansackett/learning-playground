"""
Implement Database Row Caching
"""
import time
import json

from connection import *


def schedule_row_cache(row_id, delay):
    """
    Create records for scheduler
    """
    # Set a delay for an item
    conn.zadd('delay:', row_id, delay)
    # Schedule the item to be cached now
    conn.zadd('schedule:', row_id, time.time())


def cache_rows():
    """
    Cache the specific database rows
    """
    while not QUIT:
        # Find the next row that should be cached including timestamp as list of tuples
        next = conn.zrange('schedule:', 0, 0, withscores=True)
        now = time.time()

        if not next or next[0][1] > now:
            time.sleep(.05)
            continue

        row_id = next[0][0]
        # Get a delay before the next schedule
        delay = conn.zscore('delay:', row_id)

        if delay <= 0:
            # Remove the item from the cache
            conn.zrem('delay:', row_id)
            conn.zrem('schedule:', row_id)
            conn.delete('inv:' + row_id)
            continue

        # Get the database row and add it to the cache
        row = Inventory.get(row_id)
        conn.zadd('schedule:', row_id, now + delay)
        conn.set('inv:' + row_id, json.dumps(row.to_dict()))
