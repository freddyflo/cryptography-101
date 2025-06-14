
'''
Caesar Cipher

En(x) = ( x + n ) mod 26
'''

# pay attention to white space 
# alphats are converted to numerical values
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3  # private key

def caesar_encrypt(plaintext):

    ''' 
    Encrypt the plaintext using the caesar cipher
    '''
    
    ciphertext = ''
    plaintext = plaintext.upper()
    
    for letter in plaintext:
        letter_index = ALPHABET.find(letter)
        letter_index = ( letter_index + KEY ) % len(ALPHABET)
        ciphertext += ALPHABET[letter_index]
    
    return ciphertext



def caesar_decrypt(ciphertext):

    '''
    Decrypt the ciphertext using the caesar cipher
    '''
    
    plain_text = ''
   
    for cipher_letter in ciphertext:
        cipher_letter_index = ALPHABET.find(cipher_letter)
        cipher_letter_index = ( cipher_letter_index - KEY ) % len(ALPHABET)
        plain_text += ALPHABET[cipher_letter_index]
    
    return plain_text



    
    