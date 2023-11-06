# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(rgb)

# print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list=[(136, 164, 184), (103, 76, 78), (162, 143, 157), (169, 153, 39), (233, 240, 235), (52, 42, 48), (48, 121, 88), (231, 175, 164), (182, 204, 170), (12, 96, 68), (196, 91, 73), (29, 59, 75), (200, 162, 112), (144, 17, 19), (83, 147, 128), (168, 99, 102), (227, 220, 223), (137, 27, 17), (140, 178, 155), (9, 68, 61), (64, 99, 124), (18, 85, 88), (106, 127, 152), (176, 192, 207), (27, 68, 102), (72, 39, 31), (172, 74, 58), (211, 200, 144)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()