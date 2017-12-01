from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    text_file = open('dictionary.txt', 'r')
    x = text_file.readlines()
    text_file.close()
    wordlist = [z.rstrip().upper() for z in x]
    
    return wordlist

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    wordlist = load_words()
    print(wordlist[:10])
calc_word_value()
'''
def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate
'''