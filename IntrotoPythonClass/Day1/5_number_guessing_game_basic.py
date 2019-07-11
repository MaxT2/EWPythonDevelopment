# lets create guessing game using loops!
import random

# we will need to:

# pick a random secret number
secret = random.randint(1, 10)

# store the users guess
guess = 0

# loop if the users guess does not equal the secret number
while guess != secret:
    # if the guess DOES NOT equal the secrete number, the user gets to guess again!
    guess = int(input("Please guess the secret number!"))

# after while loop, print a you win message
print("Congratulations, you got it!")


