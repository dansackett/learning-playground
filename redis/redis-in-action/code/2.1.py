"""
Implementing Login and Cookie Caching
"""
import time

from connection import *


def check_token(token):
    """
    Check that a login exists for the user and get the user
    """
    return conn.hget('login:', token)


def update_token(token, user, item=None):
    """
    Set views, recent views, and logins
    """
    timestamp = time.time()
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


def clean_sessions():
    """
    Clean the actual session information such as views, recent, and logins
    """
    while not QUIT:
        # Find number of known tokens
        size = conn.zcard('recent:')

        if size <= LIMIT:
            time.sleep(1)
            continue

        # Collect tokens to remove
        end_index = min(size - LIMIT, 100)
        sessions = conn.zrange('recent:', 0, end_index - 1)

        # Collect key names for tokens
        session_keys = []
        for sess in sessions:
            session_keys.append('viewed:' + token)
            session_keys.append('cart:' + token)

        # Delete view, login, and recent keys
        conn.delete(*session_keys)
        conn.hdel('login:', *tokens)
        conn.zrem('recent:', *tokens)
