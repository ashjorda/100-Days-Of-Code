import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(228, 238, 231), (29, 106, 160), (188, 42, 82), (231, 161, 59), (232, 214, 91), (219, 138, 173), (139, 108, 60), (108, 193, 214), (22, 57, 129), (198, 164, 37), (209, 77, 95), (234, 90, 55), (120, 190, 143), (13, 152, 89), (144, 207, 225), (136, 30, 70), (107, 108, 194), (13, 183, 175), (97, 51, 37), (25, 156, 206), (228, 169, 186), (31, 91, 94), (84, 46, 34), (31, 47, 88), (177, 186, 220), (148, 213, 196), (231, 174, 164)]


def plot_dot():
    for _ in range(10):
        dot_color = random.choice(color_list)
        tim.fd(20)
        tim.dot(20, dot_color)
        tim.fd(10)


def new_line():
    tim.left(90)
    tim.forward(30)
    tim.left(90)
    tim.forward(300)
    tim.right(180)


for _ in range(10):
    plot_dot()
    new_line()

#Close window when you click inside of it
t.exitonclick()