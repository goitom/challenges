#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH
NUM_LETTERS = 7

def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.sample(POUCH, NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        word = input("Form a valid word: ")
        valid_word = _validation(word, draw)
        print(valid_word)
        if valid_word == False:
            print("Sorry, either you used letters not drawn, or the word is not valid. Please select again: ")
            valid_word = _validation(word, draw)
            continue
        else:
            break
    return word
        




def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    word_letters = set(word)
    truth_val = word_letters.issubset(draw) & (word.lower() in DICTIONARY)
    return truth_val
    

# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    list_of_permutations = _get_permutations_draw(draw)
    possible_dict_words = []
    for perm in list_of_permutations:
        if perm.lower() in DICTIONARY:
            possible_dict_words.append(perm)
    return possible_dict_words


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    permutations = []
    for i in range(NUM_LETTERS):
        permutations_input = tuple(itertools.permutations(draw, i))
        for perm in permutations_input:
            perm = "".join(perm)
            permutations.append(perm)
    return permutations


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    value_list = []
    for word in words:
        value_list.append(calc_word_value(word))
    max_value = max(value_list)
    return words[value_list.index(max_value)]


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)
    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = float(word_score) / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
