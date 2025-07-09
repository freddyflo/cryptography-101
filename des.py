# Data Encryption Standard

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import binascii


# size of the key must be 64 bits ( 8 bytes )
# ask for a password from the user and then keep the first 8 bytes
# password - we transform this password with SHA (hashing) into 8 bytes
key = b'mysecret'

# DES generates an initialisation vector automatically if not provided explicitly 
cipher = DES.new(key, DES.MODE_CBC)

plaintext = b"This is a message"
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
print(binascii.hexlify(ciphertext))

decrypt_cipher = DES.new(key, DES.MODE_CBC, cipher.iv)
decrypted_text = unpad(decrypt_cipher.decrypt(ciphertext), DES.block_size)

print(ciphertext)
print(decrypted_text.decode())


