# Input!

# Challenge: get two numbers from the user and then add them together printing the result!
input_1 = input("Please enter a number: ")
input_2 = input("Please enter a second number: ")
print(input_1 + input_2)
# Challenge: make the output message better

# Wait why is it saying 22 instead of 4?
# when we take input from the user it saves it as a string. So our two numbers are the
# string version of the number, not the mathematical number
# we should cast our input to an int or float using int() and float() functions

input_1 = int(input("Please enter a whole number: "))
input_2 = int(input("Please enter a second whole number: "))
print(input_1 * input_2)

# Challenge: Create a message to output with your math operation
# multiplication
print(input_1, "*", input_2, "=", input_1 * input_2)

# Challaenge: create a print statement for + - * /
# addition
print(input_1, "+", input_2, "=", input_1 + input_2)
# subtraction
print(input_1, "-", input_2, "=", input_1 - input_2)

# division
print(input_1, "/", input_2, "=", input_1 / input_2)
# Write a print statement to output the addition, subtraction, multiplication and division
# of the two input numbers

# you can also store the result of the number_1 + number_2 into a new variable
number_3 = input_1 + input_2
# then print the stored result
print(number_3)
