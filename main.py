from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
food = Food()
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
scoreboard = Score()
current_score = 0
flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 16:
        food.refresh_food()
        snake.extend_snake()
        scoreboard.score()

    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        scoreboard.reset_high_score()
        flag = False

    for _ in snake.tim_segments[1:]:
        if snake.head.distance(_) < 5:
            scoreboard.reset_high_score()
            flag = False


screen.exitonclick()