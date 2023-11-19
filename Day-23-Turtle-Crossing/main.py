import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creates new cars, and sets their speed
    car_manager.car_operations()

    # Collision Detection
    for _ in car_manager.all_cars:
        if player.distance(_) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Sets new level the next level and speed up the cars
    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.increase_level()
        car_manager.increase_speed()


screen.exitonclick()