from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.sc = 0
        with open("high_score.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.write(f"Score: {self.sc}\t High Score: {self.high_score}", align="center",
                   font=("times new roman", 17, "normal"))

    def inc(self):
        self.clear()
        self.sc += 1
        self.write(f"Score: {self.sc}\t High Score: {self.high_score}", align="center", font=("times new roman", 17, "normal"))

    def sco(self):
        if self.sc > self.high_score:
            self.high_score = self.sc
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("times new roman", 35, "normal"))
