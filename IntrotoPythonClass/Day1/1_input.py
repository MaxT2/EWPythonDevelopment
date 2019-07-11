# input
# python makes it really easy to get input from the user using the input(prompt) function
# we can then store then input and choose to do something with the information

# store a greeting message
GREETING = "Hello, "

# lets get the name of the user who ran our program!
input_name = input("Please enter your name. ")
print(input_name)

# run the code! To enter the name click your mouse in the console and type in your name.
# press enter when you are done typing

# Challenge: customise the message we say after the user has given us their name!
print(GREETING + input_name + "!")

# challenge: Can you get both the first name and last name of the user and print a message?
first_name = input("Please enter your first name. ")
last_name = input("Please enter your last name. ")
print(GREETING + first_name + " " + last_name + "!")

# lets make a new file to do some math!