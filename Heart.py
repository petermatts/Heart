# from turtle import *
import turtle
import tkinter as tk
import math
import os
import sys


def set_icon() -> None:
    root = turtle.Screen()._root

    IS_BUNDLED = hasattr(sys, "_MEIPASS")
    if IS_BUNDLED: # if pyinstaller executible
        BUNDLE_DIR = getattr(
            sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__))
        )
        IMAGE_PATH = "Heart.png"
        imagepath = os.path.abspath(os.path.join(BUNDLE_DIR, IMAGE_PATH))
    else:
        imagepath = "./images/Heart.png"

    icon = tk.PhotoImage(file=imagepath)
    root.iconphoto(True, icon)


RAD2DEGREE = math.pi/180


# makes heart with two full semi-circles at top
def draw1(angle: float = 50, length: float = 200, Title: str = "Love") -> None:
    assert angle > 0 and angle <= 90
   
    turtle.color('red')
    turtle.title(Title)
    set_icon()
    turtle.begin_fill()

    # calc variables
    circportion = 270 - angle
    radius = length*math.tan(((90-angle)/2)*RAD2DEGREE)

    # draw
    turtle.setheading(angle)
    turtle.forward(length)
    turtle.circle(radius, circportion)
    turtle.setheading(90)
    turtle.circle(radius, circportion)
    turtle.setheading(360-angle)
    turtle.forward(length)

    turtle.hideturtle()
    turtle.end_fill()
    turtle.done()

# makes a heart with two semicircles at the top where the angle at the point where
# the semi-circles meet is inpointangle
def draw2(angle: float = 50, inpointangle: float = 90, length: float = 200, Title: str = "Love") -> None:
    assert angle > 0 and angle <= 90
    
    turtle.color('red')
    turtle.title(Title)
    set_icon()
    turtle.begin_fill()

    # calc variables
    halfpointang = inpointangle/2
    circportion = 270 - halfpointang - angle
    radius = length*math.cos((angle*RAD2DEGREE))/(math.cos(halfpointang*RAD2DEGREE)+math.sin(angle*RAD2DEGREE))

    height = radius + radius*math.cos(angle*RAD2DEGREE) + length*math.sin(angle*RAD2DEGREE)
    
    turtle.penup()
    turtle.setposition(turtle.position()[0], -height/2)
    turtle.pendown()

    # draw
    turtle.setheading(angle)
    turtle.forward(length)
    turtle.circle(radius, circportion)
    turtle.setheading(-turtle.heading())
    turtle.circle(radius, circportion)
    turtle.setheading(360-angle)
    turtle.forward(length)

    turtle.hideturtle()
    turtle.end_fill()
    turtle.done()


if __name__ == '__main__':
    # draw1(angle=50, length=200)
    draw2(angle=50, inpointangle=70, length=400)
