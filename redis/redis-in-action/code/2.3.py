"""
Implement web page caching
"""
import time

from connection import *


def cache_request(request, callback):
    """
    Cache a page request
    """
    # Catch if we can't cache the request
    if not can_cache(request):
        return callback(request)

    page_key = 'cache:' + hash_request(request)
    # Get the cached content
    content = conn.get(page_key)

    # If we don't have the content in the cache, cache it for 5 minutes
    if not content:
        content = callback(request)
        conn.setex(page_key, content, 300)

    return content
