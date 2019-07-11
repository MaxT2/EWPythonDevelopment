import random
secret_number = random.randint(1,5)
guess = 0
while (guess != secret_number):
    guess = input ("Your guess ? ")
    guess = int (guess)
    if (guess == secret_number):
        print ("You got it")
    elif guess > secret_number:
        print ("Too high")
    else:
        print ("Too low")