from turtle import Turtle

FONT = ("Comic Sans MS", 20, "bold")
SLEEP_DECR = 0.2


class UX(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("grey25")
        self.lvl = 1
        self.goto(-280, 260)
        self.write(f"Level: {self.lvl}", font=FONT)
        self.sleep_mult = 1

    def next_lvl(self):
        self.sleep_mult -= SLEEP_DECR
        self.lvl += 1
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.lvl}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
