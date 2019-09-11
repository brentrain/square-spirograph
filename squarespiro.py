import turtle

turtle.speed(0)
turtle.bgcolor("black")

#Loop for multiple squares

for i in range(5):
    for colors in ['red', 'magenta', 'blue', 'orange', 'green', 'yellow', 'white']:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
``        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)

#Loop to change colors
