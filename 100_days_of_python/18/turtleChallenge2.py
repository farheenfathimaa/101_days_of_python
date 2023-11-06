from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")
for i in range(30):
    if i%2!=0: 
        timmy.forward(5) 
        timmy.color("black")
    else: 
        timmy.forward(5) 
        timmy.color("white")


#or you can do this
for _ in range(10):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()


screen=Screen()
screen.exitonclick()
