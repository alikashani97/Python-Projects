from Hangman_appendix import *

lives = 6

chosen_word = random.choice(words_list)

placeholder = ""
for i in range(0,len(chosen_word)):
    placeholder = placeholder + "_"

print(placeholder)

game = False
correct_letters = []

while game is not True:
    print(f"You have got {lives} lives left!")
    display = ""
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess} before!")
    for letter in chosen_word:
      if letter == guess:
        display += letter
        correct_letters.append(letter)
      elif letter in correct_letters:
          display += letter
      else:
          display = display + "_"
    print(display)
        
    if display == chosen_word:
        game = True
        print("*******  You Won!  *******")
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game = True
            print("*******  You Lost!  *******")

    print(stages[lives])