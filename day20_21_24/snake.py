from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
        def __init__(self):
            self.segments=[]
            self.create_snake()
            self.head=self.segments[0]

        def create_snake(self):
            for index in POSITIONS:
                self.add_seg(index)

        def add_seg(self,index):
            t=Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(index)
            self.segments.append(t)
        
        def reset(self):
            for seg in self.segments:
                seg.goto(1000,1000)
            self.segments.clear()
            self.create_snake()
            self.head=self.segments[0]

        def extend(self):
            self.add_seg(self.segments[-1].position()) 
        
        def move(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x=self.segments[seg_num-1].xcor()
                new_y=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.head.forward(MOVE_DIST)
        def right(self):
            if self.head.heading()!=LEFT:
                self.head.seth(RIGHT)
        def up(self):
            if self.head.heading()!=DOWN:
                self.head.seth(UP)
        def left(self):
            if self.head.heading()!=RIGHT:
                self.head.seth(LEFT)
        def down(self):
            if self.head.heading()!=UP:
                self.head.seth(DOWN)