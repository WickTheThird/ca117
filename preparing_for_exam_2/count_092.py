#!/usr/bin/env python3

def count_letters(word):
    if word != '':
        word = word[1:]
        return 1 + count_letters(word)
    return 0
