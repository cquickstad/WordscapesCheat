#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from argparse import ArgumentParser
from enchant import Dict  # Dictionary to check for words
from itertools import permutations  # Find all combinations of letters in a string


MIN_WORD_SIZE = 3


def parse_arguments():
    ap = ArgumentParser(description="Wordscape Cheat Tool")
    ap.add_argument('letters', nargs=1, type=str, default="", help="Letters presented in Wordscape puzzle")
    return ap.parse_args()


def wordscape_permutations_generator(letters):
    for n in range(MIN_WORD_SIZE, len(letters) + 1):
        for p in permutations(letters, n):
            yield "".join(p)


if __name__ == '__main__':
    args = parse_arguments()
    dict = Dict('en_US')
    letters = ''.join(args.letters)
    assert len(letters) >= MIN_WORD_SIZE
    answers = set()
    for permutation_of_letters in wordscape_permutations_generator(letters):
        if dict.check(permutation_of_letters):
            answers.add(permutation_of_letters)

    answers = sorted(answers)
    for a in answers:
        print(a)
