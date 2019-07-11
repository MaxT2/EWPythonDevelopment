import random

secret_number = random.randint(1, 10)
#guess = 0
#while guess != secret_number:
y=3
for x in range (0,y):
    guess = int(input("What is your guess, smarty pants? "))

    if guess == secret_number:
        print("Nice job, you got it!")
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")

    if y-x == 1 :
        print("you ran out of guesses")
    else:
        print("guesses left: %s" % (6 - x))
