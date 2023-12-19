from turtle import Turtle
from random import randint


class Paddle(Turtle):

    def __init__(self, x, y, ball, ai_speed):
        super().__init__(shape='square')
        self.shapesize(stretch_len=5)
        self.color('white')
        self.penup()
        self.right(90)
        self.goto(x, y)

        # The opponent needs this to chase the ball.
        self.ball = ball
        self.computer_speed = ai_speed

        # When the computer reaches the center, it randomly chooses a new contact point.
        # This adds a level of unpredictability, as the computer will randomly go for steep shots.
        self.contact_point = randint(-40, 40)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 10)

    def chase_ball(self):
        """The computer attempts to adjust its center so that its contact point is lined up with the ball.
        """
        paddle_height = self.ycor()
        ball_height = self.ball.ycor()
        if ball_height > paddle_height + self.contact_point:
            self.goto(self.xcor(), self.ycor() + self.computer_speed)
        elif ball_height < paddle_height - self.contact_point:
            self.goto(self.xcor(), self.ycor() - self.computer_speed)

    def return_to_center(self):
        """The computer returns to the center while the ball is heading the other way."""
        if self.ycor() > 0:
            self.goto(self.xcor(), self.ycor() - self.computer_speed)
        elif self.ycor() < 0:
            self.goto(self.xcor(), self.ycor() + self.computer_speed)

    def update_contact_point(self):
        self.contact_point = randint(-40, 40)