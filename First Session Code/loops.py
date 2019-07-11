print ("For loop, range with one number")
for x in range(10):
    number = x+11
    print ("x = %s, x+11=%s"%(x,number))

print ("For loop, range with start and end")
for x in range(11,21):
    print ("x = %s"%(x))

print ("While loop")
x = 11
while x < 20:
    print ("x = %s"%(x))
    x = x+1
