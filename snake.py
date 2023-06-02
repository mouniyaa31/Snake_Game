from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.tim_segments = []
        self.length = 0
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in positions:
            self.add_segments(position)
        self.head = self.tim_segments[0]

    def add_segments(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.goto(position)
        tim.color("white")
        self.tim_segments.append(tim)

    def extend_snake(self):
        self.add_segments(self.tim_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.tim_segments) - 1, 0, -1):
            new_x = self.tim_segments[seg_num - 1].xcor()
            new_y = self.tim_segments[seg_num - 1].ycor()
            self.tim_segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)