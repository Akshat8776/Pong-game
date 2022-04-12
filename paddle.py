from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        
    def goup(self):
        y=self.ycor()
        if y!=240:
            self.goto(self.xcor(),y+20)
        
    def godown(self):
        y=self.ycor()
        if y!=-240:
            self.goto(self.xcor(),y-20)
