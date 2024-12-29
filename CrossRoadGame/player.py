from turtle import Turtle
MOVE = 15

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.x_cor = 0
        self.y_cor = -280
        self.goto(self.x_cor, self.y_cor)

    def move(self):
        self.y_cor += MOVE
        self.goto(self.x_cor, self.y_cor)

    def restart_position(self):
        self.x_cor = 0
        self.y_cor = -280