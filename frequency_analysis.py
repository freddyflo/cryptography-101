import matplotlib.pyplot as plt



LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(text):

    text = text.upper()
    
    letter_frequencies = {}

    for letter in LETTERS:
        letter_frequencies[letter] = 0

    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies


def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.bar_label(plt.gca().containers[0])
    plt.xlabel('Letter')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Distribution')
    plt.show()


if __name__ == '__main__':

    plain_text = "Shannon defined the quantity of information produced by a source--for example, the quantity in a message--by a formula similar to the equation that defines thermodynamic entropy in physics. In its most basic terms, Shannon's informational entropy is the number of binary digits required to encode a message"
    frequencies = frequency_analysis(plain_text)
    plot_distribution(frequencies)