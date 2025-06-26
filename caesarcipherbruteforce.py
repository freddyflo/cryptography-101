
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = ''

def crack_casear(cipher_text):

    for key in range(len(ALPHABET)):
        plain_text = ''

        # check the caesar decryption
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]
    
        # print decrypted message and given key 
        print('with key %s the result is %s' % (key, plain_text))


if __name__ == '__main__':
    ENCRYPTED_MESSAGE = 'VJKUBKUBCBOGUUCIG'
    crack_casear(ENCRYPTED_MESSAGE)

