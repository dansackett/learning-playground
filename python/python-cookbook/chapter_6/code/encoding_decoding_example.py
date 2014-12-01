"""
Encoding / Decoding
"""
s = b'hello'

# Encode / Decode Hex to Bytes
import binascii
h = binascii.b2a_hex(s)
print(h)
print(binascii.a2b_hex(h))

# Encode / Decode Base64 to Hex
import base64
h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))

# Decode byte to ascii
print(h.decode('ascii'))

# Encode / Decode Base64
import base64
a = base64.b64encode(s)
print(a)
print(base64.b64decode(a))
