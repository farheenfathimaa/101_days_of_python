from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

def move_forwards():
    '''moves the turtle forwards'''
    tim.forward(10)
def move_backwards():
    '''moves the turtle backwards'''
    tim.backward(10)
def clockwise():
    '''turns the turtle clockwise'''
    current_heading=tim.heading()
    tim.seth(current_heading+10)
def anticlockwise():
    '''turns the turtle anti-clockwise'''
    current_heading=tim.heading()
    tim.seth(current_heading-10)
def clear_screen():
    tim.reset()
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=clockwise)
screen.onkey(key="d",fun=anticlockwise)
screen.onkey(key="c",fun=clear_screen)



screen.exitonclick()

