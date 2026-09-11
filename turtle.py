# from turtle import *
# green = "#007A5E"
# red = "#CE1126"
# yellow = "#FCD116"
# shape("turtle")
# hideturtle()
# speed(0)
# def rectangle(clr):
#     color(clr)
#     begin_fill()
#     for i in range(2):
#         forward(50)
#         left(90)
#         forward(100)
#         left(90)
#     end_fill()
# def star(clr):
#     color(clr)
#     begin_fill()
#     for i in range(5):
#         forward(40)
#         left(144)
#     end_fill()
# stripe_colors = [green, red, yellow]
# for clr in stripe_colors:
#     rectangle(clr)
#     penup()
#     forward(50)
#     pendown()
# penup()
# goto(87, 35)
# setheading(106)
# pendown()
# star(yellow)
# done()

# import turtle
# screen = turtle.Screen()
# screen.title = ("My Colorful House")
# screen.bgcolor("skyblue")
# pen = turtle.Turtle()
# pen.shape("classic")
# pen.speed(5)
# pen.pensize(3)
# def draw_rectangle(width, height, color):
#     pen.fillcolor(color)
#     pen.begin_fill()
#     for side in range(2):
#         pen.forward(width)
#         pen.left(90)
#         pen.forward(height)
#         pen.left(90)
#     pen.end_fill()
# pen.penup()
# pen.goto(-100, -100)
# pen.pendown()
# draw_rectangle(200, 150, "lightyellow")
# pen.penup()
# pen.goto(-120, 50)
# pen.pendown()

# from turtle import *
# hideturtle()
# def draw_polygon(sides, length, pen_size, s):
    # clr = input("Color [HTML]: ")
    # color(clr)
    # pensize(pen_size)
    # speed(s)
    # angles = 360 / sides
    # try:
        # fill = input("Fill (y/N): ")
        # if fill == "y":
            # begin_fill()
            # for i in range(sides):
                # forward(length)
                # left(angles)
            # end_fill()
        # elif fill == "N":
            # for i in range(sides):
                # forward(length)
                # left(angles)
        # else:
            # raise ValueError("ERROR] Invalid answer")
    # except ValueError as e:
        # print("[ERROR] Invalid answer")
# draw_polygon(4, 100, 2, 0)
# done()