import time
from turtle import Screen
from player import Player
from cars import Car
from ux import UX

SCR_WIDTH = 600
SCR_HEIGHT = 600
SCR_TOP = SCR_HEIGHT / 2 - 20
SCR_BOTTOM = SCR_HEIGHT / 2 * -1 + 20

screen = Screen()
screen.title("Worst Crossing Game Ever")
screen.setup(SCR_WIDTH, SCR_HEIGHT)
screen.bgcolor("white")
screen.tracer(0)

ux = UX()
player = Player(SCR_BOTTOM)
cars = Car(20)

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1 * ux.sleep_mult)
    screen.update()

    cars.move()

    for car in cars.all:
        if car.distance(player) < 20:
            game_is_on = False
            ux.game_over()

    if player.ycor() > SCR_TOP:
        cars.spawn(10)
        player.reset_pos()
        ux.next_lvl()

screen.exitonclick()
