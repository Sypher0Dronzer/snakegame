from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

score = Score()
snake = Snake()
food = Food()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #to detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()

    #to dertect wall collision
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()<-285 or snake.head.ycor()>285:
        score.highscore_update()
        snake.reset()


    #to detect collision of head wirth its tail
    tail=snake.segments[1:]
    for segments in tail:
        if snake.head.distance(segments)<10:
            score.highscore_update()
            snake.reset()


