from turtle import Turtle
import random
from snake import Snake


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5)
        self.speed(0)
        self.refresh_food()

    def refresh_food(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.goto(x, y)