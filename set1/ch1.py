'''
Convert hex to base64

The string:

    49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:

    SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
'''

import binascii
import base64

CHALLENGE_STRING = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
EXPECTED_OUTPUT  = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def unhex (bytes_in):
	return binascii.unhexlify(bytes_in)

def ascii2base64 (bytes_in):
    return base64.b64encode(bytes_in)

if __name__ == '__main__':
    bytes_in = bytes(CHALLENGE_STRING, 'utf-8')
    bytes_out = ascii2base64(unhex(bytes_in))
    ans = bytes_out.decode('utf-8')

    if ans == EXPECTED_OUTPUT:
        expected = 'Yes' 
    else:
        expected = 'No'
    
    print('Is this the expected output? {0}!'.format(expected))
