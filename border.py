from turtle import Turtle

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.pensize(5)
        self.hideturtle()
        self.draw_border()


    def draw_border(self):
        self.setposition(int(SCREEN_WIDTH / 2)-15, int(SCREEN_HEIGHT / 2)-5)
        self.pendown()
        self.setheading(180)
        self.forward(SCREEN_WIDTH-20)
        self.setheading(270)
        self.forward(SCREEN_HEIGHT-20)
        self.setheading(0)
        self.forward(SCREEN_WIDTH-20)
        self.setheading(90)
        self.forward(SCREEN_HEIGHT-20)
        self.penup()
        self.pensize(2)
        self.setposition(0, int(SCREEN_HEIGHT / 2)-5)
        self.pendown()
        self.setheading(270)
        self.forward(SCREEN_HEIGHT-20)






