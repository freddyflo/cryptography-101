import random
from math import floor 
from math import sqrt 

RANDOM_START = 1000
RANDOM_END = 100000

def is_prime(num):

    if num < 2:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, floor(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    
    return True


# Euclid greatest common divisor algorithm: this is how we can verify 
# whether (e, phi) are coprime ... with the gcd(e, phi)=1 condition
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# extended Euclid's algorithm to find modular inverse in O(log m) so in linear time 
# this is how we can find the d value which is the modular inverse of e in the RSA cryptosystem
def modular_inverse(a, b):
   
   # of course because gcd(0, b)=b and a*x+b*y=b - so x=0 and y = 1
   if a == 0:
       return b, 0, 1
   
   # so we use the Euclidean algorithm for gcd()
   # b%a is always the smaller number - and 'a' is the smaller integer always in this implementation
   div, x1, y1 = modular_inverse(b % a, a)

   # and we update the parameters for x, y accordingly
   x = y1 - (b // a) * x1
   y = x1

   return div, x, y


def generate_large_prime(start=RANDOM_START, end=RANDOM_END):
   
    num = random.randint(start, end)
    
    while not is_prime(num):
        num = random.randint(start, end)
    
    return num


def generate_rsa_keys():
    p = generate_large_prime()
    q = generate_large_prime()

    # this is the trapdoor function: multiplying is fast but getting p and q 
    # from n is an exponenetially slow operation
    n = p * q

    # Euler's totient phi function
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    # we must make sure gcd(e, phi) = 1 so e and phi are coprime otherwise we cannot find d
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # d is the modular inverse of e 
    d = modular_inverse(e, phi)[1]

    # private key and the public key 
    return ((d, n), (e, n))



def encrypt(public_key, plain_text):

    # e and n are needed for encryption ( these are public )
    e, n = public_key

    # use ASCII representations for the characters and the transformation
    # of every character is stored in an array 
    cipher_text = []

    # modular exponentiation
    for char in plain_text:
        cipher_text.append(pow(ord(char), e, n))  # ( ( ord(char) * e ) % n )
    
    return cipher_text

def decrypt(private_key, cipher_text):

    # d and n are needed for decryption ( private keys )
    d, n = private_key

    plain_text = []

    for char in cipher_text:
        plain_text.append(chr(pow(char, d, n)))
    
    return ''.join(plain_text)


if __name__ == '__main__':
    
    private_key, public_key = generate_rsa_keys()

    message = "This"
    print("Original message: %s " % message)
   
    cipher = encrypt(public_key, message)
    print("Encrypted message: %s " % cipher)

    plain = decrypt(private_key, cipher)
    print("Decrypted message: %s " % plain)
    









 