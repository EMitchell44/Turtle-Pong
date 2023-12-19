from turtle import Turtle
from random import choice, random
from time import sleep


class Ball(Turtle):

    def __init__(self, speed):
        super().__init__()
        # Taste the Rainbow!
        self.skittles = ['red', 'orange', 'yellow', 'lime', 'blue', 'cyan', 'purple', 'hotpink', 'white']
        self.shape('turtle')
        self.color(choice(self.skittles))
        self.penup()
        self.north_south = 1
        self.east_west = 1
        self.y_velocity = random() * 5
        self.move_speed = speed
        self.spin_speed = 0

    def move(self):
        # The spin speed is just made of arbitrary numbers.
        self.spin_speed = self.y_velocity * 2 // 1 + self.move_speed / 3

        # X = (current x + speed) * direction
        # Y = (current y + speed) * direction
        self.goto(self.xcor() + self.move_speed * self.east_west, self.ycor() + self.y_velocity * self.north_south)
        sleep(0.01)

    def return_to_start(self):
        self.goto(0, 0)
        self.north_south = 1
        self.east_west *= -1
        self.y_velocity = random()
        self.color(choice(self.skittles))