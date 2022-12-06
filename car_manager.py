import random
from turtle import Turtle
COLORS = ["red", "orange", "cyan", "green", "blue", "purple", "magenta"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.05


class CarManager:
    """Reunites the cars that are created"""
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a new car in case a random number equals 1"""
        chance = random.randint(1, 10)
        if chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            car_y = new_car.ycor() + random.randint(-250, 250)
            new_car.goto(300, car_y)
            self.all_cars.append(new_car)

    def cars_move(self):
        """Moves the cars forwards"""
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def next_level(self):
        """Increases car speed once player reaches edge"""
        for car in self.all_cars:
            self.car_speed += MOVE_INCREMENT
