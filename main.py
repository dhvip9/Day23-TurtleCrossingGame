import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("TurtleCrossing Game")
screen.tracer(0)

man = Player()
level = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(fun=man.front, key="Up")

complete_level = False
while not complete_level:
    screen.update()
    time.sleep(0.05)

    car.car_body()
    car.car_move()

    if man.at_finish_line():
        man.refresh()
        level.increase_level()
        car.speed_increases()

    # For checking car collision
    for Car in car.cars:
        if Car.distance(man) < 25:
            complete_level = True

level.game_over()
screen.exitonclick()
