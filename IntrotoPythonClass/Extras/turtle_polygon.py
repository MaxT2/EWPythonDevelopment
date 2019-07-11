import turtle
number_of_sides = input ("Number of sides ? ")
number_of_sides = int (number_of_sides)
length = input ("Length ? ")
length = int (length)
tom = turtle.Turtle()
for x in range(1,number_of_sides+1):
    print (x)
    tom.forward(length)
    tom.left(360/number_of_sides)
turtle.done()