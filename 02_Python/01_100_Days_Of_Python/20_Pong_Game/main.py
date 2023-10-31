from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
score = Scoreboard()


pad_right = Paddle((350, 0))
pad_left = Paddle((-350, 0))
screen.listen()
screen.onkey(pad_right.move_up, "Up")
screen.onkey(pad_right.move_down, "Down")

screen.onkey(pad_left.move_up, "w")
screen.onkey(pad_left.move_down, "s")
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    if ball.distance(pad_right) < 50 and ball.xcor() > 320 or ball.distance(pad_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
