import turtle
import random
'''
import colorgram
# Extract the colours of an image
palette = colorgram.extract("image.jpg", 30)
colours = []
for i in palette:
    tuple_c = (i.rgb[0], i.rgb[1], i.rgb[2])
    colours.append(tuple_c)
'''

colours = [(189, 214, 234), (247, 167, 40), (81, 177, 235), (203, 247, 189), (39, 77, 183), (158, 97, 18),
           (177, 96, 151), (111, 97, 185), (153, 163, 155), (168, 65, 116), (248, 147, 185), (3, 98, 90), (4, 7, 78),
           (239, 81, 70), (100, 134, 99), (61, 1, 7), (74, 146, 174), (196, 142, 169), (52, 11, 9), (233, 201, 118),
           (108, 139, 108), (28, 59, 136), (239, 174, 163), (179, 184, 220), (177, 224, 159), (124, 145, 80),
           (154, 204, 224), (5, 75, 61)]

# Making the painting
t = turtle.Turtle()
turtle.colormode(255)
t.hideturtle()
t.shape("turtle")
t.speed("fastest")
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)


def return_to_position():
    t.goto(initial_pos[0], initial_pos[1])
    t.left(90)
    t.forward(50)
    t.right(90)


for i in range(10):
    initial_pos = t.position()
    for j in range(10):
        t.dot(15, random.choice(colours))
        t.forward(50)

    return_to_position()

s = turtle.Screen()
s.exitonclick()
