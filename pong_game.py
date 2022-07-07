from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from border import Border

LEFT_PADDLE_COORDINATES = (-350, 0)
RIGHT_PADDLE_COORDINATES = (350, 0)
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = Screen()
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("black")
screen.title("Pong Game")

l_paddle = Paddle(LEFT_PADDLE_COORDINATES)
r_paddle = Paddle(RIGHT_PADDLE_COORDINATES)
ball = Ball()
border = Border()
scoreboard_left = Scoreboard("left")
scoreboard_right = Scoreboard("right")

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_running = True
while is_running:

    ball.move_ball()

    if ball.hit_paddle(l_paddle):
        ball.speed_increment()

    if ball.hit_paddle(r_paddle):
        ball.speed_increment()

    if ball.outside_boundary_right():
        scoreboard_right.display_score()

    if ball.outside_boundary_left():
        scoreboard_left.display_score()

screen.exitonclick()





