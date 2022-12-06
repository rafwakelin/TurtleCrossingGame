from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    """Creates the player"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Moves the player up"""
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """Moves the player down"""
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        """Moves the player left"""
        x_axis = self.xcor() - MOVE_DISTANCE
        y_axis = self.ycor()
        self.goto(x_axis, y_axis)

    def move_right(self):
        """Moves the player right"""
        x_axis = self.xcor() + MOVE_DISTANCE
        y_axis = self.ycor()
        self.goto(x_axis, y_axis)
