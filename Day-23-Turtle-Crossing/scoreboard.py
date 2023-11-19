from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.refresh_level()

    def refresh_level(self):
        self.clear()
        self.goto(-290, 270)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.refresh_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="left", font=FONT)