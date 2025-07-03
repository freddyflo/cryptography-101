# use secret module instead, random module is for demonstration purposes
from random import randint
from frequencyanalysiscaesar import plot_distribution, frequency_analysis

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain_text, key):

    plain_text = plain_text.upper()
    
    cipher_text = ''

    for index, character in enumerate(plain_text):
        key_index = key[index]
        character_index = ALPHABET.find(character)

        # Ei(xi) = (xi + OTPi) mod 26
        cipher_text += ALPHABET[(character_index + key_index) % len(ALPHABET)]

    return cipher_text

    pass

def decrypt(cipher_text, key):

    plain_text = ''

    for index, character in enumerate(cipher_text):
        
        key_index = key[index]  
        character_index = ALPHABET.find(character)
        
        # Di(xi) = (xi - OTPi) mod 26
        plain_text += ALPHABET[(character_index - key_index) % len(ALPHABET)]

    return plain_text

    pass

def random_sequence(text):

    random_numbers = []

    for _ in range(len(text)):
        random_numbers.append(randint(0, len(ALPHABET) - 1 ))
    
    return random_numbers


if __name__ == '__main__':
    
    message = "Shannon defined the quantity of information produced by a source--for example, the quantity in a message--by a formula similar to the equation that defines thermodynamic entropy in physics. In its most basic terms, Shannon's informational entropy is the number of binary digits required to encode a message"
    sequence = random_sequence(message)
    print("#" * 50)
    print("Original message: %s" % message.upper())
    cipher = encrypt(message, sequence)
    print("#" * 50)
    print("Encrypted message: %s" % cipher) 
    print("#" * 50)
    print("Decrypted message: %s" % decrypt(cipher, sequence))
    print("#" * 50)
    plot_distribution(frequency_analysis(cipher))
    print("#" * 50)