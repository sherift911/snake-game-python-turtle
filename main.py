from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

window = Screen()
window.setup(width=800, height=800)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

food = Food()
snake = Snake()
score = Scoreboard()

game_on = True
while game_on:
    snake.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake.move_up, "Up")
    window.onkey(snake.move_down, "Down")
    window.onkey(snake.move_left, "Left")
    window.onkey(snake.move_right, "Right")
    if snake.turtles[-1].distance(food) < 15 :
        food.appear()
        snake.extend()
        score.increase_scoreboard()
    if snake.turtles[-1].xcor() > 370 or snake.turtles[-1].xcor() < -370 or snake.turtles[-1].ycor() > 370 or snake.turtles[-1].ycor() < -370 :
        game_on = False   
        score.game_over()
    for segment in snake.turtles[0:-1]: 
        if snake.turtles[-1].distance(segment) < 10:
            game_on = False
            score.game_over()   
print(snake)        
        












window.exitonclick()