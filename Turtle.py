from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# draw a square
# for _ in range(4):
#    timmy.forward(90)
#    timmy.right(90)

# for _ in range(50):
#     timmy.pendown()
#     timmy.forward(3)
#     timmy.penup()
#     timmy.forward(3)

# for i in range(3,10):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     timmy.pencolor(r, g, b)
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)


# colors = ["green yellow", "green", "dark orange", "dark slate blue", "magenta", "yellow", "medium blue"]
# move = ["forward", "right", "left", "backward"]

# for i in range(100):
#     timmy.color(random.choice(colors))
#     timmy.pensize(20)
#     destination = random.choice(move)
#     if destination == "forward":
#         timmy.setheading(90)
#     elif destination == "right":
#         timmy.setheading(0)
#     elif destination == "left":
#         timmy.setheading(180)
#     elif destination == "backward":
#         timmy.setheading(270)
#     timmy.forward(40)

timmy.speed("fastest")
number = int(input("How many circles do you want to be drawn? "))
for i in range(number):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor(r, g, b)
    timmy.circle(80)
    timmy.right(360/number)


screen = Screen()
screen.exitonclick()