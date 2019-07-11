for x in range(20, 10, -1):
    print("A Count %s" % (x))

for x in range(0, 10):
    print("B Count 20-%s = %s" % (x, 20 - x))

x = 20
while (x > 10):
    x = x - 1
    print("C Count %s" % (x))
# Wait, that did not work - how do you fix

x = 20
while (x > 10):
    print("D Count %s" % (x))
    x = x - 1

x = 20
while (x > 10):
    x = x - 1
    print("E Count %s" % (x+1))


