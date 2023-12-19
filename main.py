from turtle import Screen
from paddle import Paddle
from ball import Ball
from hud import HUD
from time import sleep

ball_speed = 10
computer_speed = 8

screen = Screen()

screen.setup(800, 600)
screen.title('TURTLE P0NG!')
screen.bgcolor('black')
screen.tracer(0)

ball = Ball(ball_speed)

right_paddle = Paddle(350, 0, ball, 0)
left_paddle = Paddle(-350, 0, ball, computer_speed)

computer_score = 0
player_score = 0

hud = HUD(left_paddle.computer_speed, ball.move_speed)


def hit(paddle):
    if ball.ycor() > paddle.ycor():
        direction = 1
    elif ball.ycor() < paddle.ycor():
        direction = -1
    else:
        direction = 0

    # Sets the ball's Y velocity. The farther the ball is from the center, the greater the
    # y velocity. The y velocity determines the angle that the ball will travel.
    # If we take A as the absolute difference between the vertical center of the ball and the vertical
    # center of the paddle and B as a number that is negative if the ball is lower than the paddle,
    # then the formula for the Y Velocity is:
    # A // arbitrary number * B * current direction
    ball.y_velocity = abs(ball.ycor() - paddle.ycor()) // 4 * direction * ball.north_south
    ball.east_west *= -1

screen.listen()
screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')

while True:
    ball.move()

    if ball.east_west == 1:
        ball.right(ball.spin_speed)
        left_paddle.return_to_center()
        if left_paddle.ycor() == 0:
            left_paddle.update_contact_point()
    else:
        ball.left(ball.spin_speed)
        left_paddle.chase_ball()
    sleep(0.01)

    # I had to add the third conditions here because there was a bug where the ball would
    # sometimes get stuck behind the paddle.
    right_collide = bool(ball.xcor() >= 335 and ball.distance(right_paddle) <= 50 and ball.xcor() < right_paddle.xcor())
    left_collide = bool(ball.xcor() <= -335 and ball.distance(left_paddle) <= 50 and ball.xcor() > left_paddle.xcor())

    ceiling_collide = bool(ball.ycor() >= 290)
    floor_collide = bool(ball.ycor() <= -290)

    right_miss = bool(ball.xcor() >= 450)
    left_miss = bool(ball.xcor() <= -450)

    if right_collide:
        hit(right_paddle)

    if left_collide:
        hit(left_paddle)

    if ceiling_collide or floor_collide:
        ball.north_south *= - 1

    if right_miss:
        ball.return_to_start()
        hud.score_for_computer()
    if left_miss:
        ball.return_to_start()
        hud.score_for_player()

    hud.display()
    screen.update()
