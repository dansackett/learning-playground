"""
Gevent allows you to patch a lot of blocking calls to allow them to become
non-blocking.
"""

import socket
print socket.socket

print 'After monkey patching'
from gevent import monkey
monkey.patch_socket()
print socket.socket

import select
print select.select
monkey.patch_select()
print 'After monkey patching'
print select.select
