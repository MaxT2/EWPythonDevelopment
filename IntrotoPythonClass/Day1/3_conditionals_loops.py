# Conditionals and loops

# conditionals are very useful. They allow us to check
# what is going on in our program or compare two things
# to each other. We can run a specific bit of code based
# on the condition

# store a value to check
number = 10

# check if the number equals 10
if number == 10:
    print("the number is 10")

# check if the number is not 10
if number != 10:
    print("The number is NOT 10!")

# check if the number is < 5
if number < 5:
    print("The number is less than 5!")
# check if the number is > 5

if number > 5:
    print("The number is greater than 5!")

# notice how the code only runs when the condition is true!
# change the value of number and have the kids tell you if
# each condition is true or false before running the code

# LOOPS
# loops are an important to programming
# they allow us to do many operations easily or run a specific bit of code multiple times
# There are many ways you can write loops in programming

# Basic While Loop With User Input
# lets start with a while loop
# while loops repeat code over and over based on a tested condition
# WHILE the condition is TRUE, the code loops
# WHEN the condition become FALSE then loop stops

# make a variable to store user_input so we can check it in the loop
# start user input variable at y so our condition is True
user_input = "y"
# start your loop code. This loop will run as long and user_input does not equal the letter n
while user_input == "y":
    # every time we loop lets ask the user what they would like to do
    user_input = input("Please enter y to keep looping!")
    # end of loop

# empty line for spacing
print()

# While Loop With Counter
# create variable to store count for how many times we have looped
count = 1
# run our loop as long as our count is less than 10
while count < 10:
    # while looping
    # print current count
    print(count)
    # increase counter by 1 each loop
    count = count + 1
    # end of loop

# empty line for spacing
print()

# Loping over a list of objects can be super usefull and it is something
# python makes super easy. Lets create a list then go over each object in a loop.

# create a list of letters
list_a = ["A", "B", "C", "D", "E", "F"]
# loop over each thing in the list and store each one in the variable element
for element in list_a:
    # print out the current element in the list we are looking at
    print(element)
    # end of for loop

# empty line for spacing
print()

# For Loop using Range(start, end-1,incrementer)
print("range(10)")
for x in range(10):
    # print out the number stored in x
    print(x)

# empty line for spacing
print()

# For Loop using Range(start, end-1,incrementer)
print("range(1, 10, 2)")
for x in range(1, 10, 2):
    # print out the number stored in x
    print(x)

# empty line for spacing
print()

# For Loop using Range(start, end-1,incrementer)
print("range(20, 1, -1)")
for x in range(10, 1, -1):
    # print out the number stored in x
    print(x)


