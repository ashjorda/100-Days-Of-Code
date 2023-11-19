import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)
def move_backwards():
    tim.backward(10)

def turn_lef():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    turtle.resetscreen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_lef)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)


#Closes screen when clicked
screen.exitonclick()