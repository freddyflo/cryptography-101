
ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ENGLISH_WORDS = []

def get_data():
    with open('english_words.txt', 'r') as file:
        for word in file:
            ENGLISH_WORDS.append(word.split('\n')[0])


# count the number of english words in a given text
def count_words(text):
    text = text.upper()

    # transform the text into a list of words (split by spaces)
    words = text.split(' ')
   
    # matches counts the number of english words in the text 
    matches = 0

    # consider all the words in the text and check whether the 
    # given word is english or not

    for word in words:
        # optimise the data structure  
        if word in ENGLISH_WORDS:
            matches += 1

    return matches


# decides whether a given text is english or not
def is_text_english(text):

    matches = count_words(text)
   
    # you can define your own classification algorithm
    # assumption: if 80% of the words in the text are english words then
    # it is an english text
    if ( float(matches) / len(text.split(' ')) ) * 100 >= 70:
        return True
  
    return False

# cracking the caesar encryption algorithm with brute-force
def caesar_crack(cipher_text):

    for key in range(len(ALPHABET)):
        plain_text = ''

        # check the caesar decryption
        for letter in cipher_text:
            index = ALPHABET.find(letter)
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]

        if is_text_english(plain_text):
            print("We have managed to crack caesar cipher, the key is: %s, the message is: %s" % (key, plain_text))

if __name__ == '__main__':
    get_data()
    encrypted_message = 'VJKUBKUBCBOGUUCIG'
    caesar_crack(encrypted_message)