# Suggestion Method
import string
import numpy as np
import random 

with open('wordle-La.txt') as f:
    word_bank = f.readlines()
    i = 0
    while i < len(word_bank):
        word_bank[i] = word_bank[i].replace("\n", "")
        i+=1

word_bank = np.array(word_bank);


def suggestions(colors, letters):
    clean_colors = colors.lower().strip(" ")
    clean_letters = letters.lower().strip(" ")
    _valid_input(clean_colors, clean_letters)

def first_guess():
    # create a word out of most common words in wordle dictionary
    # most common letters / best positioning (do both)
    first_word_suggestions = []
    for i in range(5):
        letter_counts = {}
        for input in word_bank: 
            letter = input[i]
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    sorted_letters = sorted(letter_counts, key= lambda x: letter_counts[x], reverse=True)
    top_five = sorted_letters[:5]
    list = {}
    value = 0
    for word in word_bank:
        if sorted_letters[0] in word:
            value += 100
        if sorted_letters[1] in word:
            value += 90
        if sorted_letters[2] in word:
            value += 80
        if sorted_letters[3] in word:
            value += 70
        if sorted_letters[4] in word:
            value += 60
        if sorted_letters[5] in word:
            value += 50
        if sorted_letters[6] in word:
            value += 40
        if sorted_letters[7] in word:
            value += 30
        if sorted_letters[8] in word:
            value += 20
        if sorted_letters[9] in word:
            value += 10
        list[word] = value
        value=0
    sorted_words = sorted(list, key=lambda y: list[y], reverse=True)
    return [sorted_words[1], sorted_words[1:10]]

lists = first_guess()
print("Your best first guess is:", lists[0])
print("Here are eight other reasonable guesses: ", lists[1])

