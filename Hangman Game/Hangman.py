import Hangman_appendix

chosen_word = random.choice(words_list)
print(chosen_word)

placeholder = ""
for i in range(0,len(chosen_word)):
    placeholder = placeholder + "_"

print(placeholder)

correct_letters = []

game = False

while game is not True:
    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display = display + letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display = display + letter
        else:
            display = display + "_"
        
        if display == chosen_word:
            game = True
            print("You Won!")

    print(display)
