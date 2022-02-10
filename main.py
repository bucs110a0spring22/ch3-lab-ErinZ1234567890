import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here

# Race 1:
michelangelo.forward(random.randint(1, 100))
leonardo.forward(random.randint(1, 100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
#Race 2:
for i in range(10):
  michelangelo.forward(random.randint(1, 10))
  leonardo.forward(random.randint(1, 10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# Part B - complete part B here

michelangelo.clear()
#numSides is the number of sides of the polygon
numSides = 6
#deg is the degrees in each angle of polygon
deg = 360 / numSides
#sideLength is an arbitrary length of the sides. 50 was chosen so that the shape can be seen
sideLength = 50

michelangelo.down()

#creates a regular polygon by iterating through movement of forward and turning. iterates through the number of sides
for i in range(numSides):
  michelangelo.forward(sideLength)
  michelangelo.right(deg)
michelangelo.up()

window.exitonclick()
