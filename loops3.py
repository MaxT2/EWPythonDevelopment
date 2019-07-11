# Challenge: make it so that the range is input from the user

low = int(input("Enter a starting number"))
high = int(input("enter an ending number"))

print("For loop, range with one number")
for x in range(low):
    number = x + 11
    print("x = %s, x+11-%s"%(x,number))


print("\nFor loop, range with one number")
for x in range(low+1,high+1):
    print("x = %s"%(x))

print("\nWhile loop")
x = low+1
while x <= high:
    print ("x = %s"%(x))
    x = x + 1



