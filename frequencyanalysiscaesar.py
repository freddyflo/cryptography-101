import matplotlib.pylab as plt 


LETTERS  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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


def caesar_crack(cipher_text):
    frequencies = frequency_analysis(cipher_text)
    letter_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    print(letter_frequencies)
    print("The possible key value: %s " % ( LETTERS.find(letter_frequencies[0][0]) - LETTERS.find('E')) )

    #print(frequencies)
    #plot_distribution(frequencies)


if __name__ == "__main__":
    # key = 8 to get chipher text 
    cipher_text = 'UGVIUMQAJITIHAPWTKHMZQIUNZWUJCLIXMABPCVOIZGQIUYCITQNQMLIAIXPGAQKQABIBBPMUWUMVBQIUEWZSQVOIAIAQUCTIBQWVMVOQVMMZIBIUCTBQVIBQWVITKWUXIVGQPIDMJMMVQVBMZMABMLQVITOWZQBPUAIVLLIBIABZCKBCZMAIVLQBAQUXTMUMVBIBQWVAMAXMKQITTGQVRIDIAQVKMCVQDMZAQBGTIBMZWVQOWBIKYCIQVBMLEQBPUIKPQVMTMIZVQVOBMKPVQYCMAIZBQNQKQITQVBMTTQOMVKMVCUMZQKITUMBPWLAIVLZMKQXMAACKPIAAWTDQVOLQNNMZMVBQITMYCIBQWVATQVMIZITOMJZIQVBMZXWTIBQWVIVLMFBZIXWTIBQWVBPMAMBPQVOAUIGXZWDMBWJMDMZGDMZGQUXWZBIVBQVAMDMZITNQMTLAAWNBEIZMMVOQVMMZQVOZMAMIZKPIVLLMDMTWXUMVBWZQVDMABUMVBJIVSQVOQPIDMIAXMKQITILLQKBQWVBWYCIVBQBIBQDMUWLMTAACKPIABPMJTIKSAKPWTMAUWLMTWZBPMUMZBWVUWLMT'
    caesar_crack(cipher_text)
