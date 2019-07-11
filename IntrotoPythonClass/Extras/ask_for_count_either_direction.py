start = input("Starting number ? ")
end = input ("Ending number ? ")
start = int(start)
end = int(end)


# Method 1
if start < end:
    for x in range(start, end + 1):
        print("A Count %s" % (x))

    x = start
    while (x <= end):
        print("B Count %s" % (x))
        x = x + 1
else:
    for x in range(start, end + 1):
        print("C Count %s" % (x))

    x = start
    while (x >= end):
        print("D Count %s" % (x))
        if x == end:
            break
        x = x - 1

# Method 2
if (start < end):
    change = 1
else:
    change = -1

for x in range(start, end+change, change):
    print("E Count %s" % (x))

x = start
while (True):
    print("F Count %s" % (x))
    if x == end:
        break
    x = x + change
