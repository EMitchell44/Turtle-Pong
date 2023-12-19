from turtle import Turtle

class HUD(Turtle):

    def __init__(self, ai_speed, ball_speed):
        super().__init__()
        self.goto(0, 260)
        self.hideturtle()
        self.penup()
        self.color('white')
        self.ai_speed = ai_speed
        self.ball_speed = ball_speed
        self.computer_score = 0
        self.player_score = 0

    def score_for_player(self):
        self.player_score += 1

    def score_for_computer(self):
        self.computer_score += 1

    def display(self):
        display_text = f'Computer Speed: {self.ai_speed}                    '
        display_text += f'Ball Speed: {self.ball_speed}                    '
        display_text += f'\nComputer Score: {self.computer_score}                    '
        display_text += f'Player Score: {self.player_score}               '
        self.clear()
        self.write(display_text, False, 'center', ('Courier', 12, 'normal'))