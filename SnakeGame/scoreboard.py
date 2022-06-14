from turtle import Turtle

ALINGMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self._update_scoreboard()

    def score_up(self):
        self.score += 1
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALINGMENT, font=FONT)
