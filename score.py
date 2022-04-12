from turtle import Turtle
import turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("blue")
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score}",move=False,align="center",font=("Arial",20,"bold"))
        self.hideturtle()
        
    def sc_move(self):
        x=self.xcor()
        if(x>=240):
            x=-250
        x+=5
        self.goto(x,270)
        self.clear()
        self.write(f"Score : {self.score}",move=False,align="center",font=("Arial",20,"bold"))
    
    def inc_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score}",move=False,align="center",font=("Arial",20,"bold"))