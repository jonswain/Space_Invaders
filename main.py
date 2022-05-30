import time
from turtle import Screen
from player import Player
from invaders import Invaders
from scoreboard import Scoreboard

#Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Space Invaders")
screen.tracer(0)

#Create objects
player = Player()
invaders = Invaders()
invaders.create_invaders()
score_board = Scoreboard()

#Configure controls
screen.listen()
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")
screen.onkey(player.shoot, "w")

#Start game
game_is_on = True
difficulty = 0.1
while game_is_on:
    time.sleep(difficulty)
    screen.update()

    invaders.move()
    player.shot_move()

    #If bullet hits invader remove bullet and invader
    for bullet in player.all_shots:
        for invader in invaders.all_invaders:
            if bullet.distance(invader.position()) < 20:
                player.all_shots.remove(bullet)
                invaders.all_invaders.remove(invader)
                bullet.hideturtle()
                invader.hideturtle()

    #If bullet goes off screen remove bullet
    for bullet in player.all_shots:
        if bullet.ycor() >= 300:
            player.all_shots.remove(bullet)
            bullet.hideturtle()

    #If all invaders killed increase level
    if invaders.all_invaders == []:
        difficulty *= 0.8
        invaders.create_invaders()
        invaders.move_count_reset()
        invaders.speed_up()
        score_board.increase_level()

    #If invaders reach player end game
    for invader in invaders.all_invaders:
        if invader.ycor() <= -260:
            game_is_on = False

score_board.game_over()

screen.exitonclick()
