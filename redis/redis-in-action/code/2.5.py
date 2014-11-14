"""
Implement Database Row Caching
"""
import time
import json

from connection import *


def rescale_view():
    """
    Rescale the item views
    """
    while not QUIT:
        # Remove anything not in top 20000 viewed
        conn.zremrangebyrank('viewed:', 20000, 1)
        # Rescale counts to half of what they were
        conn.zinterstore('viewed:', {'viewed:': .5})
        # Do it again in 5 minutes
        time.sleep(300)


def can_cache(request):
    """
    If the item is not in the most viewed, we can cache it
    """
    item_id = extract_item_id(request)

    if not item_id or is_dynamic(request):
        return False

    rank = conn.zrank('viewed:', item_id)
    return rank is not None and rank < 10000
