import suggestion 

# Print
def main():
    input("Hello, welcome to Wordle Solver. To start, press enter.")
    list = suggestion.best_guess()
    print("The best possible choice for a first word is: " + list[0])
    print("Other possible options in descending order are: " + list[1] + ", " + list[2] + ", " + list[3] + ", " + list[4] + ", " + list[5] + ", " + list[6] + ", " + list[7] + ", " + list[8] + ", and " + list[9])
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
        list = suggestion.best_guess()
        if len(list) == 1:
            continue
        print(f"The best possible choice for word #{i+1} is: " + list[0])
        print("Other possible options in descending order are: ", list[1:10])

        

    


    # Fix this loop of inputs. Make sure to add an incorrect input if the combo is impossible!

if __name__ == '__main__':
    main()

