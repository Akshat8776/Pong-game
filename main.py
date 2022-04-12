from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import os
def clear():
    os.system('cls')
sc=Screen()
sc.bgcolor("black")
sc.setup(width=800,height=600)
sc.title("Pong game")
sc.tracer(0)

r_paddle=Paddle((360,0))
l_paddle=Paddle((-360,0))
sc.tracer(1)


def takespeed():
        
        a=sc.numinput(title="Difficulty level",prompt=f"0 - easy\n1 - medium\n2 - hard\n3 - Pro\n4 - superpro")
        
        if a==0:
            return 0.1
        elif a==1:
            return 0.09
        elif a==2:
            return 0.075
        elif a==3:
            return 0.02
        else:
            return 0.01
ball=Ball(takespeed())
sc.listen()
sc.onkeypress(l_paddle.goup,"w")
sc.onkeypress(l_paddle.godown,"s")

sc.onkeypress(r_paddle.goup,"Up")
sc.onkeypress(r_paddle.godown,"Down")
game_on=True
while(game_on):
    game_on=ball.ball_move(l_paddle,r_paddle)
sc.reset()
sc.textinput(title="Game over",prompt=f"Your score is : {ball.score.score}")
clear()
print(f"Your score is : {ball.score.score}")





        


sc.exitonclick()