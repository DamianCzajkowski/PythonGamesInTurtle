from turtle import Turtle

ALINGMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_highscore()
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
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALINGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
        self.score = 0
        self._update_scoreboard()

    def save_highscore(self):
        with open("score_data.txt", "w") as file:
            file.write(str(self.high_score))

    def load_highscore(self):
        try:
            with open("score_data.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            pass

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALINGMENT, font=FONT)
