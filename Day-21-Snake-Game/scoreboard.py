from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-10, 280)
        self.counter = 0
        self.pen(shown=False)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:  {self.counter} ", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.counter += 1
        self.clear()
        self.update_scoreboard()



