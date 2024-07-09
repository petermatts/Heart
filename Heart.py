from turtle import *
import math

RAD2DEGREE = math.pi/180

# makes heart with two full semi-circles at top
def draw1(angle: float = 50, length: float = 200, Title: str = "Love") -> None:
    assert angle > 0 and angle <= 90
   
    color('red')
    title(Title)
    begin_fill()

    # calc variables
    circportion = 270 - angle
    radius = length*math.tan(((90-angle)/2)*RAD2DEGREE)

    # draw
    setheading(angle)
    forward(length)
    circle(radius, circportion)
    setheading(90)
    circle(radius, circportion)
    setheading(360-angle)
    forward(length)

    hideturtle()
    end_fill()
    done()

# makes a heart with two semicircles at the top where the angle at the point where
# the semi-circles meet is inpointangle
def draw2(angle: float = 50, inpointangle: float = 90, length: float = 200, Title: str = "Love") -> None:
    assert angle > 0 and angle <= 90
    
    color('red')
    title(Title)
    begin_fill()

    # calc variables
    halfpointang = inpointangle/2
    circportion = 270 - halfpointang - angle
    radius = length*math.cos((angle*RAD2DEGREE))/(math.cos(halfpointang*RAD2DEGREE)+math.sin(angle*RAD2DEGREE))

    height = radius + radius*math.cos(angle*RAD2DEGREE) + length*math.sin(angle*RAD2DEGREE)
    
    penup()
    setposition(position()[0], -height/2)
    pendown()

    # draw
    setheading(angle)
    forward(length)
    circle(radius, circportion)
    setheading(-heading())
    circle(radius, circportion)
    setheading(360-angle)
    forward(length)

    hideturtle()
    end_fill()
    done()


if __name__ == '__main__':
    # draw1(angle=50, length=200)
    draw2(angle=50, inpointangle=70, length=400)
