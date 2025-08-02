from Crypto.Hash import SHA256

# ECC elliptic curve cryptogrpahy 
from Crypto.PublicKey import ECC

# DSS digital signature standard
from Crypto.Signature import DSS


key = ECC.generate(curve='P-256')

# print(key.export_key(format='PEM'))
# print(key.public_key().export_key(format='PEM'))

message = "Transaction #322212 is sent from A to B in Bitcoin"

# convert any message to 256 bits long hash
message_hash = SHA256.new(message.encode())

signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(message_hash)

print(signature)

# verify signature
verifier = DSS.new(key.public_key(), 'fips-186-3')
try:
    verifier.verify(message_hash, signature)
    print("The signature is valid.")
except ValueError:
    print("The signature is not valid.")
    pass