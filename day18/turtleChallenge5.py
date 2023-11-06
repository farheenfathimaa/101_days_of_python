import turtle as t
import random 
tim=t.Turtle()
t.colormode(255)
tim.ht()

def random_color():
    r= random.randint(0,255)
    b= random.randint(0,255)
    g= random.randint(0,255)
    random_color=(r,g,b)
    return random_color

t.pensize(5)
tim.speed('fastest')
def draw_spirogragh(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading=tim.heading()
        tim.seth(current_heading+size_of_gap)

draw_spirogragh(5)

screen=t.Screen()
screen.exitonclick()