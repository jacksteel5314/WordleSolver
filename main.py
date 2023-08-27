import suggestion 
import numpy as np

# Print
def main():
    word_bank = []
    with open('wordle-La.txt') as f:
        word_bank = f.readlines()
        i = 0
        while i < len(word_bank):
            word_bank[i] = word_bank[i].replace("\n", "")
            i+=1

    input("Hello, welcome to Wordle Solver. To start, press enter.")
    list = suggestion.best_guess(word_bank)
    print("The best possible choice for a first word is: " + list[0])
    print("Other possible options in descending order are: " + list[1] + ", " + list[2] + ", " + list[3] + ", " + list[4] + ", " + list[5] + ", " + list[6] + ", " + list[7] + ", " + list[8] + ", and " + list[9])
    for i in range(1, 6):
        if len(word_bank) == 1:
            print(f"Congratulations, you found your word: {word_bank}")
            break
        while True:
            word = input(f"Input guess #{i}: ")
            colors = input(f"Input colors #{i}(B = black, Y = yellow, G = green): ")
            try: 
                valid_input = suggestion.valid_input(word_bank, colors, word)
            except ValueError as err:
                print("Your Entry was Invalid. Try Again")
                print(err)
                continue
            break
        colors = colors.lower().strip(" ")
        word = word.lower().strip(" ")
        word_bank = suggestion.remove(word_bank, colors, word)
        list = suggestion.best_guess(word_bank)
        print(f"The best possible choice for word #{i+1} is: " + list[0])
        print("Other possible options in descending order are: ", list[1:10])


    # Fix this loop of inputs. Make sure to add an incorrect input if the combo is impossible!

if __name__ == '__main__':
    main()


