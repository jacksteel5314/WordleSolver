# SuggestionMethod
import string
import numpy as np
import random 


def suggestions(word_bank, colors, letters):
    clean_colors = colors.lower().strip(" ")
    clean_letters = letters.lower().strip(" ")
    new_word_bank = remove(word_bank, clean_colors, clean_letters)
    return best_guess(new_word_bank)


def valid_input(word_bank, colors, letters):
    if (len(colors) != 5) & (len(letters) != 5):
        raise ValueError(f"Colors input and letters input must be five characters in length.")
    elif len(colors) != 5:
        raise ValueError(f"Colors input must be five characters in length.")
    elif len(letters) != 5:
        raise ValueError(f"Letters input must be five characters in length.")
    for i in range(len(colors)):
        if (colors[i] != 'b') & (colors[i] != 'g') & (colors[i] == 'y'):
            raise ValueError(f"Colors can only be 'b', for black, 'y', for yellow, or 'g', for green.")
    if letters not in word_bank: 
        raise ValueError(f"The inputted word is not in the word bank. Try a suggested word.")
    return
    

def remove(word_bank, colors, letters):
    for i in range(5):
        if colors[i] == 'b':
            for word in word_bank:
                if letters[i] in word:
                    word_bank.remove(word)
        elif colors[i] == 'y':
            for word in word_bank:
                if letters[i] not in word:
                    word_bank.remove(word)
                if letters[i] == word[i]:
                    word_bank.remove(word)
        elif colors[i] == 'g':
            for word in word_bank:
                if word[i] != letters[i]:
                    word_bank.remove(word)
    return word_bank


def best_guess(word_bank):
    ideal_word = ""
    letter_counts = {}
    # Iterate through each letter
    for i in range(5):
        indiv_letter_counts = {}
        
        # Iterate through each word and add to total letter counts and positional letter counts 
        for input in word_bank: 
            letter = input[i]
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
            indiv_letter_counts[letter] = indiv_letter_counts.get(letter, 0) + 1

        # Sort the positional letter counts and add the first ranking count to ideal word
        new_counts = sorted(indiv_letter_counts, key=lambda x: indiv_letter_counts[x], reverse=True)
        ideal_word += new_counts[0]

    # Sort the total letter count
    sorted_letters = sorted(letter_counts, key= lambda x: letter_counts[x], reverse=True)

    # Iterate through each word
    list = {}
    value = 0
    for word in word_bank:

        # Check if the top ten ranking letters are in the word, and add values descending by 10 from 100 to value
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

        # If the letters of the word match the top positional letters, then add 50 
        if ideal_word[0] == word[0]:
            value += 50
        if ideal_word[1] == word[1]:
            value += 50
        if ideal_word[2] == word[2]:
            value += 50
        if ideal_word[3] == word[3]:
            value += 50
        if ideal_word[4] == word[4]:
            value += 50
        list[word] = value
        value=0

    # Sort list by value and return a list containing the first ten words
    sorted_words = sorted(list, key=lambda y: list[y], reverse=True)
    letter_counts.clear()
    sorted_letters.clear()
    list.clear()
    new_counts.clear()
    indiv_letter_counts.clear()
    ideal_word = ""
    return sorted_words[:10]






