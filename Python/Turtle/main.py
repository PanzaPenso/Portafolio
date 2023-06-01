from turtle import Turtle, Screen
from random import choice

mike = Turtle()
board = Screen()
board.screensize(400, 400)
mike.speed(4)
mike.pensize(8)

color_bank = ['blue', 'black', 'yellow', 'green', 'red', 'brown']


def forward(distance):
    mike.forward(distance)


def backward(distance):
    mike.backward(distance)


def left(distance):
    mike.left(90)
    mike.forward(distance)


def right(distance):
    mike.right(90)
    mike.forward(distance)


options = [1, 2, 3, 4]

for i in range(200):
    move = choice(options)
    mike.color(choice(color_bank))
    if move == 1:
        forward(50)
    elif move == 2:
        backward(50)
    elif move == 3:
        right(50)
    else:
        left(50)

# cont = 8
# sides = 3
# angle = 0
# while cont > 0:
#     angle = 360 / sides
#     leonardo.pencolor(choice(color_bank))
#     for i in range(sides):
#         leonardo.right(angle)
#         leonardo.forward(70)
#     sides += 1
#     cont -= 1

#
# for i in range(40):
#     if i % 2 == 0:
#         leonardo.penup()
#         leonardo.forward(5)
#     else:
#         leonardo.pendown()
#         leonardo.forward(5)


board.exitonclick()
