# Challenge: Number Loop with User Input
# Lets comebine some of the things we know!
# I want you to write a new program that gets two whole numbers from the user
# and counts between them using a for loop!

# cast input to int for whole numbers
start = int(input("Starting whole number ? "))
end = int(input("Ending whole number ? "))
for x in range(start, end+1):
    print(x)
