import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

direction = 0

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(100):
    tim.color(random_color())
    tim.circle(100)
    tim.tilt(direction)
    tim.setheading(direction)
    direction += 5


#Close window when you click inside of it
t.exitonclick()