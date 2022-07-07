from turtle import Turtle
import random

SCREEN_X_BOUNDARY = {
                    "min": -390,
                    "max": 380
                     }
SCREEN_Y_BOUNDARY = {
                    "min": -280,
                    "max": 290
                     }


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.increment = 1
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.color("white")
        self.last_direction_x = 0
        self.last_direction_y = 0
        self.next_direction_x, self.next_direction_y = self.random_start_direction()

    def random_start_direction(self):
        direction = [-1, 1]
        return random.choice(direction), random.choice(direction)

    def move_ball(self):

        self.setposition(self.last_direction_x, self.last_direction_y)
        self.next_direction_x, self.last_direction_x = \
            self.shuffle(self.next_direction_x, self.last_direction_x, SCREEN_X_BOUNDARY)
        self.next_direction_y, self.last_direction_y = \
            self.shuffle(self.next_direction_y, self.last_direction_y, SCREEN_Y_BOUNDARY)

    def shuffle(self, next_pos, last_pos, boundary):

        if next_pos > last_pos:
            last_pos = next_pos
            next_pos += self.increment

        elif next_pos < last_pos:
            last_pos = next_pos
            next_pos -= self.increment

        if last_pos > boundary["max"] - 5:
            next_pos -= self.increment + 2

        elif last_pos < boundary["min"] + 5:
            next_pos += self.increment + 2

        return next_pos, last_pos

    def hit_paddle(self, paddle):

        if self.distance(paddle) < 50 and self.xcor() > SCREEN_X_BOUNDARY["max"] - 50:
            self.next_direction_x -= self.increment + 2
            return True
        elif self.distance(paddle) < 50 and self.xcor() < SCREEN_X_BOUNDARY["min"] + 60:
            self.next_direction_x += self.increment + 2
            return True
        else:
            return False

    def outside_boundary_left(self):

        if self.xcor() <= SCREEN_X_BOUNDARY["min"]+5:
            self.reset_position()
            return True
        else:
            return False

    def outside_boundary_right(self):

        if self.xcor() >= SCREEN_X_BOUNDARY["max"]-5:
            self.reset_position()
            return True
        else:
            return False

    def reset_position(self):

        self.last_direction_x = 0
        self.last_direction_y = 0
        self.increment = 1
        self.next_direction_x, self.next_direction_y = self.random_start_direction()

    def speed_increment(self):
        self.increment += 0.25




