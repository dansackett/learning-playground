"""
An example using WATCH with transactions.
"""
import time
import redis

from connection import *


def update_token(token, user, item=None):
    """
    Set views, recent views, and logins
    """
    timestamp = time.time()
    # Start a non-transactional pipeline
    conn.pipeline(False)
    # Make sure the mapping from login to user is available
    conn.hset('login:', token, user)
    # Record time when token was last seen
    conn.zadd('recent:', token, timestamp)

    if item:
        # Note that a user viewed an item and when
        conn.zadd('viewed:' + token, item, timestamp)
        # Only keep 25 views
        conn.zremrangebyrank('viewed:' + token, 0, -26)
        # Decrease view count for item by one giving us most viewed with lowest score
        conn.zincrby('viewed:', item, -1)
    pipe.execute()
