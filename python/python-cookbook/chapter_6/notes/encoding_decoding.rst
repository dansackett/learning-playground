Encoding and Decoding Things
============================

For encoding and decoding, there are two simple libraries for people to use.
The first is binascii and the second is base64. The binascii module allows us
to convert hexadecimal strings to byte strings and back::

    >>> import binascii
    >>> s = b'hello'
    >>> h = binascii.b2a_hex(s)
    >>> print(h)
    b'68656c6c6f'
    >>> print(binascii.a2b_hex(h))
    b'hello'

The second is the base64 module which can be done with hexadecimal or to do
basic base64 encoding::

    >>> import base64
    >>> h = base64.b16encode(s)
    >>> print(h)
    b'68656C6C6F'
    >>> print(base64.b16decode(h))
    b'hello'

    >>> import base64
    >>> a = base64.b64encode(s)
    >>> print(a)
    b'aGVsbG8='
    >>> print(base64.b64decode(a))
    b'hello'

When we want to get an ASCII string back, we have to explicitly convert it::

    >>> print(h.decode('ascii'))
    68656C6C6F

It's basic but it works for encoding and decoding.
