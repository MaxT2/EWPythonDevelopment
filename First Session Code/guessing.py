# guessing game!
# import random so we can use it
import random

# randomly select a winning number
answer = random.randint(1, 10)
# start the user's guess at 0
guess = 0
#
for x in range(6):
    print(x)
    guess = int (input ("Guess ? "))
    if guess == answer:
        print ("You got it!!")
        break
    elif guess > answer:
        print ("Too high")
    else:
        print ("Too low")
print ("End of game")