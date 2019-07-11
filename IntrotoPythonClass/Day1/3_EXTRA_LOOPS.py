# OTHER EXAMPLES IF YOU NEED THEM

# empty line for spacing
print()

for number in [1, 2, 3, 4, 5]:
    print(number)

# blank line
print()

for letter in ["A", "B", "C", "D", "E"]:
    print(letter)

# blank line
print()

print("range(3)")
for number in range(3):
    print(number)

print()
# you can also give two number parameters to range which define
# the number to start at and the number to end right before
# this loop starts at 5 and goes until 9
print("range(5, 10)")
for number in range(5, 10):
    print(number)

print()
print("range(10)")
# challenge: use one of theses two loops to create a loop that runs 10 times
for x in range(10):
    print(x)

print()
# or
print("range(0, 10)")
for x in range(0, 10):
    print(x)

print()
# challenge: create a loop that number starts at 10 and ends at 20
print("range(10, 21)")
for x in range(10, 21):
    print(x)

print()
# you can also define what happens to the variable when we loop
# by default the variable will increment (count up) by 1
# this loop counts up by 2
print("range(0,21,2")
for x in range(0, 21, 1):
    print(x)

print()

# challenge: Create a loop that counts backwards from 20 to 10

print("20-10")
for x in range(20, 9, -1):
    print(x)

print()