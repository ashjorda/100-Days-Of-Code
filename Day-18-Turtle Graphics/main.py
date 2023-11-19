import turtle as t

tim = t.Turtle()
t.setup(width=200, height=200, startx=None, starty=None)

########### Challenge 2 - Draw a Dashed Line ########
tim.shape("turtle")
tim.pencolor("red")
tim.down()
tim.forward(200)

#Draw a Blue Triangle

for sides in range(3):
    tim.right(120)
    tim.forward(200)

#Draw a square
tim.pencolor("blue")
for sides in range(4):
    tim.right(90)
    tim.forward(200)

#Draw a Pentagon
tim.pencolor("brown")
for sides in range(5):
    tim.right(72)
    tim.forward(200)

# #Draw a Hexagon
tim.pencolor("purple")
for sides in range(6):
    tim.right(60)
    tim.forward(200)

#Draw a Hepatgon
tim.pencolor("green")
for sides in range(7):
    tim.right(51.43)
    tim.forward(200)

#Draw a Octagon
tim.pencolor("yellow")
for sides in range(8):
    tim.right(45)
    tim.forward(200)


#Draw a Nonagon
tim.pencolor("orange")
for sides in range(9):
    tim.right(40)
    tim.forward(200)

#Draw a decagon
tim.pencolor("grey")
for sides in range(10):
    tim.right(36)
    tim.forward(200)

#Close window when you click inside of it
t.exitonclick()