from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, alignment):

        super().__init__()
        self.alignment = alignment
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.setposition(0, 230)
        self.score = 0
        self.display_score()

    def display_score(self):

        self.clear()
        self.write(f" {self.score} ", move=False, align=self.alignment, font=('Courier', 50, 'normal'))
        self.score += 1

