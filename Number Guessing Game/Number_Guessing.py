from Number_Guessing_appendix import *

Answer = random.randint(1,100)

print(Answer)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if diff == 'hard':
    TRY = 5
elif diff == 'easy':
    TRY = 10
else:
    print("Please try again!")


while TRY > 0:
    print(f"you have {TRY} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    if guess < Answer:
        print("Too low.")
    elif guess == Answer:
        print(f"You got it! The answer was {Answer}")
        break
    else:
        print("Too High.")
    TRY -= 1

print("You've run out of guesses. Refresh the page to run again.")