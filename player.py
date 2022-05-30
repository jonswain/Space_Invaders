from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.all_shots = []

    def left(self):
        if self.xcor() > -280:
            self.setx(self.xcor() - MOVE_DISTANCE)

    def right(self):
        if self.xcor() < 280:
            self.setx(self.xcor() + MOVE_DISTANCE)

    def reload(self):
        time.sleep(0.1)

    def okay_to_shoot(self):
        if len(self.all_shots) <= 9:
            return True
        else:
            return False

    def shoot(self):
        if self.okay_to_shoot():
            new_shot = Turtle()
            new_shot.shape("circle")
            new_shot.color("black")
            new_shot.shapesize(stretch_wid=0.1, stretch_len=1)
            new_shot.penup()
            new_shot.setposition(self.position())
            new_shot.left(90)
            self.all_shots.append(new_shot)


    def shot_move(self):
        for bullet in self.all_shots:
            bullet.forward(10)