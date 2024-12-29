from turtle import Turtle, Screen
import random
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

SPEED = 5
COLORS = ["blue1", "brown", "burlywood4", "chocolate", "cyan2", "DarkOrange", "DeepPink", "orchid2"]

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("CrossRoadGame")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.go()
        if car.distance(player) < 20:
            game_is_on = False

    rand = random.randint(1,10)
    if rand == 1 or rand == 2:
        new_car = Car(random.choice(COLORS), random.randint(-240, 240), SPEED)
        cars.append(new_car)

    if player.y_cor > 270:
        scoreboard.level_up()
        player.restart_position()
        SPEED += 2

scoreboard.game_over()
    


screen.exitonclick()