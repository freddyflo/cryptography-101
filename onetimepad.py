# use secret module instead, random module is for demonstration purposes
from random import randint

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain_text):
    pass

def decrypt(cipher_text):
    pass

def random_sequence(text):

    random_numbers = []

    for _ in range(len(text)):
        random_numbers.append(randint(0, len(ALPHABET) - 1 ))
    
    return random_numbers


if __name__ == '__main__':
    print(random_sequence("Hello World"))