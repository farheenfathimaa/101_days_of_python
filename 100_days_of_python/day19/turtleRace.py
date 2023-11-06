from turtle import Turtle,Screen
import random

all_turtles=[]
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y=[-100,-60,-20,20,60,100]

for turtle_index in range(0,6):
    t=Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230,y=y[turtle_index])
    all_turtles.append(t)


if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
        
    

  




screen.exitonclick()

