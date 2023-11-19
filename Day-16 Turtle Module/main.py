# from turtle import Turtle, Screen
#
# leah = Turtle()
# print(leah)
# leah.shape("turtle")
# leah.color("coral")
# leah.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtal", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)

