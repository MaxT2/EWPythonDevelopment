start = input("Starting number ? ")
end = input ("Ending number ? ")
start = int(start)
end = int(end)

for x in range(start, end+1):
    print("A Count %s" % (x))

for x in range(end, start-1, -1):
    print("B Count %s" % (x))

x = start
while (x <= end):
    print("C Count %s" % (x))
    x = x + 1

x = end
while (x >= start):
    print("D Count %s" % (x))
    x = x - 1


