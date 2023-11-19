from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.loop_count = 0
        self.hideturtle()
        self.create_new_car()
        self.speed = STARTING_MOVE_DISTANCE

    def car_operations(self):
        self.move_car_forward()
        if self.loop_count % 6 == 0:
            self.create_new_car()
        self.loop_count += 1

    def move_car_forward(self):
        for _ in self.all_cars:
            _.forward(self.speed)

    def create_new_car(self):
        y_position = random.randint(-250, 250)
        color_selector = random.randint(0, len(COLORS)-1)
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.shape("square")
        new_car.setheading(180)
        new_car.color(COLORS[color_selector])
        new_car.goto(x=350, y=y_position)
        self.all_cars.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT





