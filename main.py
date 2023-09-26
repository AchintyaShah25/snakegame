from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen=Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Achintya's game")
screen.tracer(0)
game = True
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()
while game:
    screen.update()
    time.sleep(0.08)
    snake.move()
    if snake.head.distance(food) < 15:
        score.inc()
        snake.extend()
        food.loc_food()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 275 or snake.head.ycor() < -290:
        score.sco()
        score.game_over()
        game = False
    for body_parts in snake.snakes[1:]:
        if snake.head.distance(body_parts) < 9:
            game = False
            score.sco()
            score.game_over()

screen.exitonclick()
