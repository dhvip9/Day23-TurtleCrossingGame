from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
PIXEL = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5

    def car_body(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            tom = Turtle("square")
            tom.speed(0)
            tom.penup()
            tom.turtlesize(stretch_wid=1, stretch_len=2)
            tom.color(random.choice(COLORS))
            coordinates = (300, random.randrange(-200, 200, 45))
            tom.goto(coordinates)
            self.cars.append(tom)

    def car_move(self):
        for Car in self.cars:
            Car.back(self.STARTING_MOVE_DISTANCE)

    def speed_increases(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
