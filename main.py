import suggestion 

# Print
def main():
    input("Hello, welcome to Wordle Solver. To start, press enter.")
    list = suggestion.first_guess()
    print("The best possible choice for a first word is: " + list[0])
    print("Other possible options in descending order are: " + list[1] + ", " + list[2] + ", " + list[3] + ", " + list[4] + ", " + list[5] + ", " + list[6] + ", " + list[7] + ", " + list[8] + ", and " + list[9])
    input("Press enter when a word is submitted")
    word = input("Input your first guess: ")
    colors = input("Input the colors (B = black, Y = yellow, G = green): ")
    first_guess = suggestion.suggestions(word, colors)
    print(first_guess[0], first_guess[1:10])

if __name__ == '__main__':
    main()


