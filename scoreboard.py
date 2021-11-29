from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(x=-240, y=260)
        self.level = 1
        self.body()

    def body(self):
        """Set Score Body"""
        self.write(arg=f"LEVEL : {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """Set Scoreboard Increase"""
        self.level += 1
        self.clear()
        self.body()

    def game_over(self):
        """Set GameOver Message"""
        self.clear()
        self.home()
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=("Courier", 24, "bold"))
        self.goto(0, 30)
        self.write(arg=f"FINAl LEVEL : {self.level}", align=ALIGNMENT, font=("Courier", 30, "bold"))


