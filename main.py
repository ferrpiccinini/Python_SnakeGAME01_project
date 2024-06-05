import scoreboard
from turtle import *
import time
import random
game_is_on = True
from dots import Dots
from snake import Snake
from scoreboard import Scoreboard

snake = Snake()
dots = Dots()
score = Scoreboard()
screen = Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

for _ in range(3):
    snake.add_snake()

dots.move_dots()

while game_is_on == True:
    screen.update()
    time.sleep(0.01)
    snake.move_snake()
    if abs(snake.list_of_snakes[0].xcor() - dots.list_of_dots[0].xcor()) < 15 and abs(snake.list_of_snakes[0].ycor() - dots.list_of_dots[0].ycor()) < 15:
        dots.move_dots()
        snake.add_snake()
        score.add_score()
    for segment in snake.list_of_snakes:
        if snake.list_of_snakes[0].xcor() > 280 or snake.list_of_snakes[0].xcor() < -280 or snake.list_of_snakes[0].ycor() > 280 or snake.list_of_snakes[0].ycor() < -280:
            snake.reset_snake()
            score.reset_score()
        if segment != snake.list_of_snakes[0]:
            if snake.list_of_snakes[0].distance(segment) < 10:
                snake.reset_snake()
                score.reset_score()

screen.exitonclick()
