# import another_module
from turtle import Turtle, Screen
from prettytable import PrettyTable

# print(another_module.another_variable)
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("SeaGreen4")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)




