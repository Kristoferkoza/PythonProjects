from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, y_cor, speed):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.x_cor = 280
        self.y_cor = y_cor
        self.goto(280, self.y_cor)
        self.speed = speed

    def go(self):
        x = self.xcor()
        x = x - self.speed
        self.goto(x, self.y_cor)
