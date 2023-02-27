import colorgram
import random
import turtle as t
from turtle import Turtle


# rgb_color = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)

t.colormode(255)
ant = Turtle()
ant.speed("fastest")
ant.penup()
ant.hideturtle()
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40),
              (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159),
              (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102),
              (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39),
              (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30),
              (16, 77, 106)]

ant.setheading(225)
ant.forward(300)
ant.setheading(0)
number_of_dots = 101


for dot_count in range(1, number_of_dots):
    ant.dot(20, random.choice(color_list))
    ant.forward(50)

    if dot_count % 10 == 0:
        ant.setheading(90)
        ant.forward(50)
        ant.setheading(180)
        ant.forward(500)
        ant.setheading(0)


screen = t.Screen()
screen.exitonclick()
