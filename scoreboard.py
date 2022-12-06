from turtle import Turtle
FONT = ("Courier", 24, "normal")


class LevelBoard(Turtle):

    def __init__(self):
        """Indicates player level"""
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setposition(-280, 250)
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def new_level(self):
        """Once the tutle cross level gets updated"""
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        """Writes game over in the screen when turtle is run over"""
        self.setposition(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
