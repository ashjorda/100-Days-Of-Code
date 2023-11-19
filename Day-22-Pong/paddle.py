from turtle import Turtle


class PADDLE(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(coordinates)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
