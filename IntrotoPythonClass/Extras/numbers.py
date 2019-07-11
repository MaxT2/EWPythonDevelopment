# print the result of adding two numbers together
#number variables
num1 = 8
num2 = 4

print(num1 + num2)
# print("8 + 4 = " + num1 + num2)
# doesnt work because numbers are not strings so you cannot concatenate
# instead do..
print("8 + 4 = " + str(num1 + num2))
# print the string of (num1 + num2)
# now add the result of subtraction, multiplication and
print("8 - 4 = " + str(num1 - num2))
print("8 * 4 = " + str(num1 * num2))
print("8 / 4 = " + str(num1 / num2))

# test, is the math correct
# the cool thing about using variables is that you can change them!



# now change your variables and test different numbers
# but our messages are all wrong now! We are not adding 8 and 4
# lets print out our numbers before we do the math
num1 = 10
num2 = 5
print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))


# now make it so the user enters two numbers
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

# this wont work becuase when we add them python doesn't know how to do math
# with strings. These are not numbers yet. We have to store them as numbers
# by converting them into inteter using the int() function
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))