import turtle
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from turtle import Screen,Turtle
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("pong")

r_paddle= Paddle((-350,0))
l_paddle= Paddle((+350,0))

screen.listen()
screen.onkey(r_paddle.go_up ,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")

ball= Ball((0,0))
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:

    time.sleep(0)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 or ball.distance(l_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()