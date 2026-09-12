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

# from turtle import *
# bgclr = input("Bg color [HTML]: ")
# bgcolor(bgclr)
# def growing_shape(s, length, sides, repeat, distance):
#     speed(s)
#     clr = input("Color [HTML]: ")
#     color(clr)
#     angles = 360 / sides
#     for i in range(repeat):
#         pendown()
#         for j in range(sides):
#             forward(length)
#             left(angles)
#         penup()
#         backward(distance)
#         right(90)
#         forward(distance)
#         left(90)
#         length += distance * 2
# growing_shape(0, 10, 4, 20, 10)
# done()

# from turtle import *
# bgclr = input("Bg color [HTML]: ")
# hideturtle()
# speed(0)
# bgcolor(bgclr)
# def draw_spiral(step, angles, repeat):
#     clr = input("Color [HTML]: ")
#     color(clr)
#     step_distance = step * 2
#     for i in range(repeat):
#         forward(step)
#         left(angles)
#         forward(step_distance)
#         left(angles)
#         step += step_distance
# draw_spiral(0.25, 25, 500)
# done()

# from turtle import *
# speed(0)
# bgclr = input("Bg color [hex]: ")
# bgcolor(bgclr)
# def draw_polygon(x, y, sides, side_length, hex_color, fill):
#     penup()
#     goto(x, y)
#     pendown()
#     color(hex_color)
#     angles = 360 / sides
#     if fill == "y":
#         begin_fill()
#         for i in range(sides):
#             forward(side_length)
#             left(angles)
#             end_fill()
#     elif fill == "N":
#         for i in range(sides):
#             forward(side_length)
#             left(angles)
# draw_polygon(0, 0, 5, 40, "#0000FF", "y")
# draw_polygon(-100, -100, 4, 50, "#00FF00", "N")
# draw_polygon(100, -100, 6, 60, "#00FF00", "N")
# draw_polygon(-100, 100, 4, 50, "#FF0000", "y")
# draw_polygon(100, 100, 8, 50, "#0000FF", "N")
# done()
