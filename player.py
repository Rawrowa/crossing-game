from turtle import Turtle


class Player(Turtle):

    def __init__(self, y):
        super().__init__()
        self.spawn_pos = (0, y)
        self.penup()
        self.shape("circle")
        self.color("grey25")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.setheading(90)
        self.goto(self.spawn_pos)

    def move(self):
        self.forward(20)

    def reset_pos(self):
        self.goto(self.spawn_pos)
