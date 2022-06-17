from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1
RESP_Y_POSITIONS = [x for x in range(260, -280, -20)]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.move_speed = STARTING_MOVE_DISTANCE
        self.refresh()

    def refresh(self):
        random_y = random.choice(RESP_Y_POSITIONS)
        x = -320
        self.setheading(0)
        self.goto(x=x, y=random_y)

    def move(self):
        self.forward(self.move_speed)


class CarManager:

    def __init__(self, player, limit_of_cars):
        self.cars = []
        self.player = player
        self.limit_of_cars = limit_of_cars

    def create_cars(self):
        random_chance = random.randint(1, 20)
        if random_chance == 1 and len(self.cars) < self.limit_of_cars:
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            car.move()

    def is_collision(self):
        for car in self.cars:
            if car.xcor() > 320:
                car.refresh()
            if car.distance(self.player) < 20:
                return False
        return True

    def speed_move(self):
        for car in self.cars:
            car.move_speed += MOVE_INCREMENT
