"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    sentence = ""
    input_file = open(file_path)
    for line in input_file:
        line = line.rstrip().split(" ")
        for word in line:
            sentence += word + " "
    
    return sentence


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    text_list = text_string.split(" ")
    chains = []
    
    for i in range(len(text_list)-2):
        chains_list = [text_list[i], text_list[i+1]]
        chains.append(chains_list)
    
    chains_tuples = []
    for chain in chains:
        chain = tuple(chain)
        chains_tuples.append(chain)

    dictionary = {}
    for tup in chains_tuples:
        phrase = ""
        phrase += tup[0] + " " + tup[1]
        for j in range(len(text_list)-3):
            for_same_tuple = []
            if text_list[j] == str(tup[0]) and text_list[j+1] == str(tup[1]):
                next_word = text_list[j+2]
                for_same_tuple.append(next_word)

                dictionary[tup] = for_same_tuple
    print(dictionary.items())


    # return chains_tuples


sentence = open_and_read_file("green-eggs.txt")
make_chains(sentence)


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
