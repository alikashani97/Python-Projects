print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Welcome to the Number Guessing Game!")

diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if diff == 'hard':
    TRY = 5
elif diff == 'easy':
    TRY = 10
else:
    print("Please try again!")