from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    text_file = open('dictionary.txt', 'r')
    x = text_file.readlines()
    text_file.close()
    wordlist = [z.rstrip() for z in x]
    print wordlist[0:10]
    return wordlist

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate
