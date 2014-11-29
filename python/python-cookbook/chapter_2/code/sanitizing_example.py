import unicodedata
import sys

"""
Translating data
"""
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}

# Convert tabs, carriage returns, etc
a = s.translate(remap)
print(a)

# Create map for all combining unicode characters to None
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

# Normalize mappings into combinations
b = unicodedata.normalize('NFD', a)
print(b)

# Apply mapping
c = b.translate(cmb_chrs)
print(c)


"""
Using Encoding
"""
print(a)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))
