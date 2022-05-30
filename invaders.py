from turtle import Turtle, Screen

STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
x_positions = (-280, -240, -200, -160, -120, -80, -40)
y_positions = (240, 200, 160, 120, 80, 40)

sc = Screen()
sc.register_shape("spaceinvaders.gif")

class Invaders:
    def __init__(self):
        self.all_invaders = []
        self.invaders_speed = STARTING_MOVE_DISTANCE
        self.count = 1

    def create_invaders(self):
        for x_pos in x_positions:
            for y_pos in y_positions:
                new_invader = Turtle()
                new_invader.shape("square")
                new_invader.color("red")
                new_invader.penup()
                new_invader.setposition(x_pos, y_pos)
                self.all_invaders.append(new_invader)

    def move(self):
        if self.count % 32 == 0:
            self.move_closer()
            self.count +=1
        elif self.count % 64 > 32:
            self.move_right()
            self.count += 1
        else:
            self.move_left()
            self.count +=1

    def move_count_reset(self):
        self.count = 1

    def speed_up(self):
        self.invaders_speed += MOVE_INCREMENT

    def move_left(self):
        for invader in self.all_invaders:
            invader.setx(invader.xcor()+10)

    def move_right(self):
        for invader in self.all_invaders:
            invader.setx(invader.xcor()-10)

    def move_closer(self):
        for invader in self.all_invaders:
            invader.sety(invader.ycor()-20)