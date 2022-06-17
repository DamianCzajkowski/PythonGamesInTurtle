import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager(player, 60)
score_board = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.0045)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    game_is_on = car_manager.is_collision()
    if not game_is_on:
        score_board.game_over()

    if player.ycor() > 300:
        score_board.level_up()
        car_manager.speed_move()
        player.restart()

screen.exitonclick()
