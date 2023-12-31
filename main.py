'''
Main Method File
'''
import suggestion

def main():
    '''
    Main Method
    '''
    input("Hello, welcome to Wordle Solver. To start, press enter.")
    list1 = suggestion.best_guess()
    print("The best possible choice for a first word is: " + list1[0])
    strg = "Other possible options in descending order are: "
    for i in range(1, 10):
        strg += (list1[i] + ", ")
    print(strg[0:len(strg)-2])
    for i in range(1, 6):
        if len(suggestion.word_bank) == 1:
            print(f"Congratulations, you found your word: {suggestion.word_bank[0]}")
            break
        while True:
            word = input(f"Input guess #{i}: ")
            colors = input(f"Input colors #{i}(B = black, Y = yellow, G = green): ")
            try:
                valid_input = suggestion.valid_input(colors, word)
            except ValueError as err:
                print("Your Entry was Invalid. Try Again")
                print(err)
                continue
            break
        try:
            suggestion.suggestions(colors, word)
        except ValueError as err:
            print(err)
            break
        list1 = suggestion.best_guess()
        if len(list) == 1:
            continue
        print(f"The best possible choice for word #{i+1} is: " + list1[0])
        print("Other possible options in descending order are: ", list1[1:10])


if __name__ == '__main__':
    main()