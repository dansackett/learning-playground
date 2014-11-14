"""
Implementing a shopping cart design
"""
import time

from connection import *


def add_to_cart(session, item, count):
    if count <= 0:
        conn.hrem('cart:' + session, item)
    else:
        conn.hset('cart:' + session, item, count)
