# RSA (public key and private key)
# RSA encrypts a session key (AES)
# https://pycryptodome.readthedocs.io/en/latest/src/introduction.html
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

# generate the keys
key = RSA.generate(2048)
private_key = key 
public_key = key.public_key()

## RSA encryption
data = "This is a message".encode()

# This is the private key in AES (16 bytes for the private key)
session_key = get_random_bytes(16)


# encrypt the session key with the public RSA key
# PKCS - https://en.wikipedia.org/wiki/PKCS_1
# OAEP - https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding
encrypt_rsa = PKCS1_OAEP.new(public_key)
encrypted_session_key = encrypt_rsa.encrypt(session_key)

# introduces secure communication 
# encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_GCM)

# digest can be used for authentication
cipher_text, tag = cipher_aes.encrypt_and_digest(data)

# RSA decryption
decrypt_rsa = PKCS1_OAEP.new(private_key)
decrypted_session_key = decrypt_rsa.decrypt(encrypted_session_key)

# decrypt the data with the AES
decrypt_aes = AES.new(decrypted_session_key, AES.MODE_GCM, cipher_aes.nonce)
plain_text = decrypt_aes.decrypt_and_verify(cipher_text, tag)
print(plain_text.decode())