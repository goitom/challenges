from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    text_file = open('dictionary.txt', 'r')
    x = text_file.readlines()
    text_file.close()
    wordlist = [z.rstrip().upper() for z in x]
    return wordlist

def calc_word_value(word):
    """Calculate the value of the word entered into function    using imported constant mapping LETTER_SCORES"""
    scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"), (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z"), (0, "-")]
    letter_scores = {letter: score for score, letters in scrabble_scores for letter in letters.split()}
    # print letter_scores
    letters = list(word)
    # print letters
    word_value = sum([letter_scores[k] for k in letters])
    return word_value

def max_word_value(inputlist):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    value_list = []
    for words in inputlist:
        value_list.append(calc_word_value(words))
    max_value = max(value_list)
    return inputlist[value_list.index(max_value)]

word_list=load_words()
print len(word_list)
# test = word_list[99500:100000]
# print test
max_word_val=max_word_value(word_list)
print max_word_val
if __name__ == "__main__":
    pass # run unittests to validate
