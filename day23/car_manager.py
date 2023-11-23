from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()
        self.car_move()
        self.car_speed =STARTING_MOVE_DISTANCE

    def create_car(self):
            random_chance=random.randint(1,6)
            if random_chance==1: 
                car = Turtle()
                car.shape("square")
                car.shapesize(stretch_len=2,stretch_wid=1)
                car.penup()
                car.color(random.choice(COLORS))
                random_y=random.randint(-250,250)
                car.goto(x=300,y=random_y)
                self.cars.append(car)
    
    def car_move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


