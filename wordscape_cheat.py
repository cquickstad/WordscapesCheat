#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from argparse import ArgumentParser
from enchant import Dict  # Dictionary to check for words
from itertools import permutations  # Find all combinations of letters in a string


def parse_arguments():
    ap = ArgumentParser(description="Wordscape Cheat Tool")
    ap.add_argument('-n', type=int, default=3, help="Minmum number of letters for shortest words")
    ap.add_argument('letters', nargs=1, type=str, default="", help="Letters presented in Wordscape puzzle")
    return ap.parse_args()


def wordscape_permutations_generator(min_size, letters):
    for n in range(min_size, len(letters) + 1):
        for p in permutations(letters, n):
            yield "".join(p)


if __name__ == '__main__':
    args = parse_arguments()
    dict = Dict('en_US')
    letters = ''.join(args.letters)
    assert len(letters) >= args.n
    answers = set()
    for permutation_of_letters in wordscape_permutations_generator(args.n, letters):
        if dict.check(permutation_of_letters):
            answers.add(permutation_of_letters)

    answers = sorted(answers)
    for a in answers:
        print(a)
