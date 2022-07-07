from turtle import Turtle
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.setposition(x=position[0], y=position[1])
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")

    def move_up(self):
        current_y = self.ycor()
        if current_y < int(SCREEN_HEIGHT/2) - 55:
            self.sety(current_y + 20)

    def move_down(self):
        current_y = self.ycor()
        if current_y > int(-SCREEN_HEIGHT/2) + 75:
            self.sety(current_y - 20)


