
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
    matches = 1

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
    print(matches)

    # you can define your own classification algorithm
    # assumption: if 80% of the words in the text are english words then
    # it is an english text
    if ( float(matches) / len(text.split(' ')) ) * 100 >= 50:
        return True
  
    return False


if __name__ == '__main__':
    get_data()
    text = "You you you you you you you"
    print(is_text_english(text))
   