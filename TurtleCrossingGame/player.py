from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)