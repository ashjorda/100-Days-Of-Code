import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
t.colormode(255)

tim.shape("turtle")
tim.pensize(10)
tim.speed(9)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


#Close window when you click inside of it
t.exitonclick()

#Draw a circle, and each time make the circle tilt a little for a overalpping effect using a rnadom color for each new circle