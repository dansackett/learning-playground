"""
An example using WATCH with transactions.
"""
import time
import redis

from connection import *


def list_item(itemid, sellerid, price):
    """
    We can list an item into the marketplace if it has inventory.
    """
    inventory = 'inventory:%s' % sellerid
    item = '%s.%s' % (itemid, sellerid)
    end = time.time() + 5
    pipe = conn.pipeline()

    while time.time() < end:
        try:
            # We watch for changes to user's inventory
            pipe.watch(inventory)

            # Check if the user still has the item to be listed
            if not pipe.sismember(inventory, itemid):
                pipe.unwatch()
                return None

            pipe.multi()
            pipe.zadd('market:', item, price)
            pipe.srem(inventory, itemid)
            # If execute works without a watch error then it's unwatched automtically
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            # Inventory changed so retry the transaction
            pass

    return False


def purchase_item(buyerid, itemid, sellerid, lprice):
    """
    Purchase an item from the market.
    """
    # Setup keys
    buyer = 'users:%s' % buyerid
    seller = 'users:%s' % sellerid
    item = '%s.%s' % (itemid, sellerid)
    inventory = 'inventory:%s' % buyerid
    end = time.time() + 10
    pipe = conn.pipeline()

    while time.time() < end:
        try:
            # Watch for changes to the market for the buyer
            pipe.watch('market:', buyer)
            # Check for a sold item
            price = pipe.zscore('market:', item)
            funds = int(pipe.hget(buyer, 'funds'))

            if price != lprice or price > funds:
                pipe.unwatch()
                return None

            # Transfer funds from buyer to seller and transfer item
            pipe.multi()
            pipe.hincrby(seller, 'funds', int(price))
            pipe.hincrby(buyer, 'funds', int(-price))
            pipe.sadd(inventory, itemid)
            pipe.zrem('market:', item)
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            pass

    return False
