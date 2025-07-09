# Advanced Encryption Standard

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import binascii
import sys

# size of the private key must be 128 bits ( 16 bytes )
key = b'mysecretpassword'

# encrypt the plaintext
cipher = AES.new(key, AES.MODE_CBC)
plaintext = b"This is a message"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size)) # pad to get the same block size
print(binascii.hexlify(ciphertext))


# decrypt the ciphertext
decrpyt_cipher = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted_text = unpad(decrpyt_cipher.decrypt(ciphertext), AES.block_size)
print(decrypted_text.decode())





