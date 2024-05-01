from turtle import Turtle
from random import choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_SPD = 5


class Car:

    def __init__(self, n):
        self.all = []
        self.spawn(n)

    def spawn(self, n):
        for n in range(n):
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=0.85, stretch_len=1.7)
            car.color(choice(COLORS))
            car.goto(randrange(-300, 300, 20), randrange(-240, 240, 20))
            self.all.append(car)

    def move(self):
        for car in self.all:
            car.backward(MOVE_SPD)
            if car.xcor() < -340:
                car.goto(340, randrange(-240, 240, 20))
