from time import sleep
from turtle import Screen
from ball import Ball
from scoreboard import ScoreBoard
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PongGame")

screen.tracer(0)
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(left_paddle.go_up, "a")
screen.onkey(left_paddle.go_down, "z")

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() >= 330 or \
            ball.distance(left_paddle) < 50 and ball.xcor() <= -330:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
