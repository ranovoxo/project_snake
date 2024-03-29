from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)


game_is_on = True

snake = Snake()
food = Food()
score_board = Scoreboard()
score_board.load_high_score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detecting food being eaten
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.update_score()
    
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
        score_board.save_high_score()

    # detect collision with tail
    for segment in snake.segments[1:]:
    
        if snake.head.distance(segment) < 10:
            score_board.save_high_score()
            snake.reset()
    

















screen.exitonclick()
