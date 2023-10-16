from turtle import Turtle

FONT = ["Courier", 24, "normal"]



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.shapesize(1, 1)
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", font=FONT, align="center")

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)