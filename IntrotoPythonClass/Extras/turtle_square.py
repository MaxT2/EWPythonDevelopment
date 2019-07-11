import turtle
tom = turtle.Turtle()
tom.forward(30)
tom.left(90)
tom.forward(30)
tom.left(90)
tom.forward(30)
tom.left(90)
tom.forward(30)
tom.left(90)

# variation 2 - what don't you like?  color and shape
tom = turtle.Turtle()
tom.color("red")
tom.shape("turtle")
tom.forward(30)
tom.left(90)
tom.forward(30)
tom.left(90)
tom.forward(30)
tom.left(90)
tom.forward(30)
tom.left(90)

# variation 3 - let's use loops
tom = turtle.Turtle()
tom.color("red")
tom.shape("turtle")
for x in range (1,5):
    tom.forward(30)
    tom.left(90)

