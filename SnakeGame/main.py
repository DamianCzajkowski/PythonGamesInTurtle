import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

is_on = True


def exit_game():
    global is_on
    is_on = False


screen = Screen()
screen.setup(width=610, height=610)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)


snake = Snake(color="white", shape="square")
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(exit_game, "q")

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.score_up()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()
        food.refresh()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()
            food.refresh()

screen.exitonclick()
