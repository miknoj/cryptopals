"""
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.
If your function works properly, then when you feed it the string:
    
    1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
    
    686974207468652062756c6c277320657965

... should produce:

    746865206b696420646f6e277420706c6179
"""
import binascii

from ch1 import unhex

EXPECTED_OUTPUT = '746865206b696420646f6e277420706c6179'

def xor(bytes1, bytes2):
    return bytes([l^r for l, r in zip(bytes1,bytes2)])

def hex(bytes_in):
    return binascii.hexlify(bytes_in)

if __name__ == '__main__':
    first_bytes  = unhex(bytes('1c0111001f010100061a024b53535009181c', 'utf-8'))
    second_bytes = unhex(bytes('686974207468652062756c6c277320657965', 'utf-8'))
    result = hex(xor(first_bytes, second_bytes))
    result = result.decode('utf-8') # Turn it back into a string representation.

    if result == EXPECTED_OUTPUT:
        expected = 'Yes' 
    else:
        expected = 'No'
    print('Is this the expected output? {0}!'.format(expected))