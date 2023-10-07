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

tim.pensize(10)
pos=[0,90,180,270]
tim.speed('fastest')
for _ in range(100):
    tim.color(random_color())
    dir=random.choice(pos)
    tim.setheading(dir)
    tim.forward(30)



screen=Screen()
screen.exitonclick()