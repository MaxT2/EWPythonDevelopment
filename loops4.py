# now make it go reverse order

low = int(input("Enter a starting number"))
high = int(input("enter an ending number"))

print("For loop, range with one number")
for x in range(low):
    number = 20 - x
    print("x = %s, x+11-%s"%(x,number))


# TODO FINISH CHALLENGE CODE

print("\nFor loop, range with one number")
for x in range(low+1,high+1):
    print("x = %s"%(20-x))

print("\nWhile loop")
x = low+1
while x <= high:
    print ("x = %s"%(x))
    x = x + 1



