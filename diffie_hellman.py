import random

def generate_private_key(n, g):

    # random number for Alice where alice random_number < n - 1
    alice_random_number = random.randint(1, n)

    # random number for Alice where bob random_number < n - 1
    bob_random_number = random.randint(1, n)

    # calculate g^x mod n which is Alice's k1
    k1 = pow(g, alice_random_number, n)

    # calculate g^x mod n which is Bob's k2
    k2 = pow(g, bob_random_number, n)

    # if an attacker wants to get alice_random_number and bob_random_number (the private keys) which is the discrete 
    # logarithm problem it is an exponentially slow process
    print("Alice's private key %s " % (pow(k2, alice_random_number, n)))
    print("Bob's private key %s " % (pow(k1, bob_random_number, n)))


if __name__ == '__main__':
    
    # it should be a huge prime number
    n = 37
    # g is the primitive root of n
    g = 13

    # using Diffie-Hellman cryptosystem for generating private key ( for DES and AES )
    generate_private_key(n, g)





