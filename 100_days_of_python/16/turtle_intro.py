from turtle import *
timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.shapesize(2)
my_screen=Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
timmy.color('cyan4')
for i in range(20):
    timmy.forward(i)
for steps in range(30):
    for c in ('blue','black'):
        color(c)
        backward(steps)
        left(20)
my_screen.exitonclick()
timmy.circle(5)

