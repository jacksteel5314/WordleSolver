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


def suggestions(colors, letters):
    clean_colors = colors.lower().strip(" ")
    clean_letters = letters.lower().strip(" ")
    _valid_input(clean_colors, clean_letters)
    
def _valid_input(colors, letters): 
    if colors.alpha(): 

def _remove(colors, letters):
    for i in range(5):
        if colors[i] == 'b':
            word_bank.remove(word_bank.contains(letters[i]))


def _most_common(word):
    most_common = word_bank
    i = 5
    list = []
    if(len(most_common) < i):
        i = len(most_common)
    for i in range(i):
        list.append(most_common[random.randInt(0, len(most_common))])
    return list
