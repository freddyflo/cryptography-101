
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenere_encrypt(plaintext, private_key):

    plaintext = plaintext.upper()
    private_key = private_key.upper()

    ciphertext = ''
    key_index = 0

    for character in plaintext:
        # number of shifts = index of the character in the plain text
        # index of the character in the key

        index = (ALPHABET.find(character) + ALPHABET.find(private_key[key_index])) % len(ALPHABET)
        ciphertext += ALPHABET[index]
        key_index += 1

        if key_index == len(private_key):
            key_index = 0
    
    return ciphertext




def vigenere_decrypt(cipher_text, private_key):

    cipher_text = cipher_text.upper()
    private_key = private_key.upper()

    plaintext = ''
    key_index = 0

    for character in cipher_text:
        index = (ALPHABET.find(character) - ALPHABET.find(private_key[key_index])) % len(ALPHABET)
        plaintext += ALPHABET[index]
        key_index += 1

        if key_index == len(private_key):
            key_index = 0

    return plaintext


if __name__ == '__main__':
    plain_text = "Vigenere cipher"
    key = "secret"
    print("Encrypted message: %s " % vigenere_encrypt(plain_text, key))
    print("Decrypted message: %s " % vigenere_decrypt(vigenere_encrypt(plain_text, key), key))