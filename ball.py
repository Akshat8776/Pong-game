from turtle import Turtle,Screen
import time
from score import Score
class Ball(Turtle):
    def __init__(self,b):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.right(45)
        self.shapesize(1,1)
        self.score=Score()
        self.b=b
    
        
    def ball_move(self,l,r):
        self.forward(20)
        time.sleep(self.b)
        if self.ycor()>=280:
            if self.heading()==45:
                self.setheading(315)
            else:
                self.setheading(225)
        elif self.ycor()<=-280:
            if self.heading()==315:
                self.setheading(45)
            else:
                self.setheading(135)
        if self.xcor()>=330:
            if r.ycor()-self.ycor()>=-50 and r.ycor()-self.ycor()<=50:
                self.score.inc_score()
                if self.heading()==45:
                    self.setheading(135)
                else:
                    self.setheading(225)
            else:
                return False
        elif self.xcor()<=-330:
            if l.ycor()-self.ycor()>=-50 and l.ycor()-self.ycor()<=50:
                self.score.inc_score()
                if self.heading()==135:
                    self.setheading(45)
                else:
                    self.setheading(315)
            else:
                return False
        return True
        