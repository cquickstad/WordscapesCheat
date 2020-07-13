#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from argparse import ArgumentParser
from itertools import permutations  # Find all combinations of letters in a string
import os.path

try:
    from enchant import Dict  # Dictionary to check for words
except ImportError as e:
    Dict = None


def parse_arguments():
    ap = ArgumentParser(description="Wordscapes Cheat Tool")
    ap.add_argument('-d', type=str, default="", help="Specify a text file containing a custom dictionary")
    ap.add_argument('-n', type=int, default=3, help="Minimum number of letters for shortest words")
    ap.add_argument('letters', nargs=1, type=str, default="", help="Letters presented in Wordscapes puzzle")
    return ap.parse_args()


def wordscape_permutations_generator(min_size, letters):
    for n in range(min_size, len(letters) + 1):
        for p in permutations(letters, n):
            yield "".join(p)


def get_word_set_from_file(file_name):
    words = None
    if os.path.isfile(file_name):
        with open(file_name, 'r') as FILE:
            words = [word.rstrip() for word in FILE]
        words = set(words)
    return words


def get_answers(valid_word_func, letters):
    answers = set()
    for permutation_of_letters in wordscape_permutations_generator(args.n, letters):
        if valid_word_func(permutation_of_letters):
            answers.add(permutation_of_letters)
    return answers


if __name__ == '__main__':
    args = parse_arguments()
    ed = Dict('en_US') if Dict is not None else None
    words = get_word_set_from_file(args.d)
    letters = ''.join(args.letters)
    assert len(letters) >= args.n

    def word_in_enchant_dict(w):
        return ed.check(w)

    def word_in_cust_dict(w):
        return w in words

    check_word = word_in_cust_dict if words else word_in_enchant_dict
    answers = get_answers(check_word, letters)
    answers = sorted(answers)
    for a in answers:
        print(a)
