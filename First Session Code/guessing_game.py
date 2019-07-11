import random
secret_number = random.randint(1, 5)
guess = 0
while(guess != secret_number):
    guess = int(input("What is your guess ? "))
    if(guess == secret_number):
        print("You figured it out!")
    if(guess < secret_number):
        print("You are too low!")
    if(guess > secret_number):
        print("You are too high!")