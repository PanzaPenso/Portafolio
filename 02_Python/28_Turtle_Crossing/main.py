import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.up, "Up")
level = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            level.game_over()
            game_is_on = False
    # Detect successfully crossing
    if player.ycor() > 300:
        player.restart_position()
        level.increase_level()
        car_manager.level_up()

screen.exitonclick()
