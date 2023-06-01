# import colorgram
import turtle
import random

# colors = colorgram.extract('dot.jpg', 20)


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_rgb.append(new_color)
#
# print(colors_rgb)

colors_rgb = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
              (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72)]

turtle.colormode(255)

raphael = turtle.Turtle()
screen = turtle.Screen()

# raphael.dot(20, "red")
# raphael.penup()
# raphael.forward(50)
# raphael.pendown()
# raphael.dot(20, "blue")

cord_x = 0
cord_y = 0
# raphael.setheading(225)
# raphael.penup()
# raphael.forward(300)
# raphael.setheading(0)

for y in range(5):
    raphael.sety(cord_y)
    for x in range(5):
        raphael.setx(cord_x)
        raphael.dot(20, random.choice(colors_rgb))
        raphael.penup()
        raphael.forward(50)
        cord_x += 50
    cord_x = 0
    cord_y += 50

screen.exitonclick()