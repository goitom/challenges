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
        word = raw_input("Form a valid word: ")
        valid_word = _validation(word, draw)
        print(valid_word)
        if valid_word == False:
            print("Sorry, either you used letters not drawn, or the word is not valid. Please select again: ")
            valid_word = _validation(word, draw)
            continue
        else:
            break
    return word