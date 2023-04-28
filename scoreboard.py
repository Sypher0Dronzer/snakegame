from turtle import Turtle

FONT = ("courier", 16, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            h_score=file.read()
            self.highscore = int(h_score)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=(f"Score: {self.score} Highscore: {self.highscore}"), move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=(f"Score: {self.score} Highscore: {self.highscore}"), move=False, align=ALIGNMENT, font=FONT)

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(arg=(f"GAME OVER"), move=False, align=ALIGNMENT, font=("courier", 22, "normal"))
    def highscore_update(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
