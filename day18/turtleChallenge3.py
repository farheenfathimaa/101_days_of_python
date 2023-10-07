from turtle import Turtle,Screen
import random as r
timmy=Turtle()
colours=['pink','blue','red','green','black']
for i in range(3,11):
    color=r.choice(colours)
    timmy.color(color)
    for _ in range(i):
        timmy.forward(50)
        timmy.right(360/i)


screen=Screen()
screen.exitonclick()