import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import LevelBoard

# Sets up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Creates the player and cars
player = Player()
car = CarManager()
level_board = LevelBoard()

# Listens to keyboard entry and moves the player
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # Creates a new car and moves them every 0.1 seconds
    car.create_car()
    car.cars_move()

    # Detects when turtle is run over by a car
    for limo in car.all_cars:
        if limo.distance(player) < 20:
            level_board.game_over()
            game_is_on = False

    # Detects when turtle reaches a level and increases car speed
    if player.ycor() > 280:
        car.next_level()
        level_board.new_level()
        player.goto(0, -280)

    screen.update()
screen.exitonclick()
