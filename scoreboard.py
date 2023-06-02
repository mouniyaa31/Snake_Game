from turtle import Turtle


class Score(Turtle):
    current_score: int

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shapesize()
        self.goto(0, 275)
        self.current_score = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        with open("high_score.txt") as file:
            high_score = file.read()
        self.write(f"Score: {self.current_score}  High_Score: {high_score}", align="center", font=("Courier", 20, "normal"))

    def score(self):
        self.current_score += 1
        self.clear()
        self.update_score()

    def reset_high_score(self):
        with open("high_score.txt") as file:
            high_score = file.read()
            high_score = int(high_score)

        if self.current_score > high_score:
            high_score = self.current_score
            with open("high_score.txt", mode="w") as file:
                file.write(str(high_score))
        self.current_score = 0
        self.update_score()

