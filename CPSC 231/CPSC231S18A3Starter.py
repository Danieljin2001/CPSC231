import sys
import os
import turtle

WIDTH = 600
HALF_WIDTH = int(WIDTH/2)
HEIGHT = 600
HALF_HEIGHT = int(HEIGHT/2)
TICK = 6
AXISLABEL = 10
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"
def drawXAxis(pointer):
    pointer.hideturtle()
    pointer.color(AXISCOLOR)
    pointer.up()
    pointer.goto(0,HALF_HEIGHT)
    pointer.down()
    pointer.goto(WIDTH, HALF_HEIGHT)
    pointer.up()
    
def drawYAxis(pointer):
    pointer.hideturtle()
    pointer.color(AXISCOLOR)
    pointer.up()
    pointer.goto(HALF_WIDTH,0)
    pointer.down()
    pointer.goto(HALF_WIDTH, HEIGHT)
    pointer.up()
    
def drawXTicksLabel(pointer):
    tickDistance = int(WIDTH/8)
    number = 0.00
    #right side
    for distance in range (0,HALF_WIDTH +1,tickDistance):
        pointer.up()
        pointer.goto(HALF_WIDTH + distance,HALF_HEIGHT)
        pointer.down()
        pointer.goto(HALF_WIDTH + distance,HALF_HEIGHT + TICK)
        pointer.up
        pointer.goto(HALF_WIDTH + distance,HALF_HEIGHT + AXISLABEL)
        if number != 0.00:
            pointer.write(str(number))
        pointer.goto(HALF_WIDTH + distance,HALF_HEIGHT)
        pointer.down()
        pointer.goto(HALF_WIDTH + distance,HALF_HEIGHT - TICK)
        number = number + 0.25
    number = 0.00
    for distance in range (0,HALF_WIDTH +1,tickDistance):
        pointer.up()
        pointer.goto(HALF_WIDTH - distance,HALF_HEIGHT)
        pointer.down()
        pointer.goto(HALF_WIDTH - distance,HALF_HEIGHT + TICK)
        pointer.up
        pointer.goto(HALF_WIDTH - distance,HALF_HEIGHT + AXISLABEL)
        if number != 0.00:
            pointer.write(str(number))
        pointer.goto(HALF_WIDTH - distance,HALF_HEIGHT)
        pointer.down()
        pointer.goto(HALF_WIDTH - distance,HEIGHT/2 - TICK)
        number = number - 0.25
        
def drawYTicksLabel(pointer):
    tickDistance = int(HEIGHT/8)
    number = 0.00
    #top side
    for distance in range (0,HALF_HEIGHT+1,tickDistance):
        pointer.up()
        pointer.goto(HALF_WIDTH,HALF_HEIGHT + distance)
        pointer.down()
        pointer.goto(HALF_WIDTH + TICK,HALF_HEIGHT + distance)
        pointer.up
        pointer.goto(HALF_WIDTH + AXISLABEL,HALF_HEIGHT + distance)
        if number != 0.00:
            pointer.write(str(number))
        pointer.goto(HALF_WIDTH,HALF_HEIGHT + distance)
        pointer.down()
        pointer.goto(HALF_WIDTH,HALF_HEIGHT + distance)
        pointer.goto(HALF_WIDTH - TICK,HALF_HEIGHT + distance)
        number = number + 0.25
    number = 0.00
    for distance in range (0,HALF_HEIGHT+1,tickDistance):
        pointer.up()
        pointer.goto(HALF_WIDTH,HALF_HEIGHT - distance)
        pointer.down()
        pointer.goto(HALF_WIDTH + TICK,HALF_HEIGHT - distance)
        pointer.up
        pointer.goto(HALF_WIDTH + AXISLABEL,HALF_HEIGHT - distance)
        if number != 0.00:
            pointer.write(str(number))
        pointer.goto(HALF_WIDTH,HALF_HEIGHT - distance)
        pointer.down()
        pointer.goto(HALF_WIDTH,HALF_HEIGHT - distance)
        pointer.goto(HALF_WIDTH - TICK,HALF_HEIGHT - distance)
        number = number - 0.25

    
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)
    pointer.up()
    return pointer

def main():
    #Handle arguments
    #Read star information from file (function)
    pointer = setup()
    #Draw Axes (function)
    drawXAxis(pointer)
    drawXTicksLabel(pointer)
    drawYAxis(pointer)
    drawYTicksLabel(pointer)
    pointer.up()
    pointer.goto(300,300-50)
    pointer.fillcolor(STARCOLOR2)
    pointer.color(STARCOLOR2)
    pointer.down()
    pointer.begin_fill()
    pointer.circle(50)
    pointer.end_fill()
    #Draw Stars (function)
    #Loop getting filenames
        #Read constellation file (function)
        #Draw Constellation (function)
        #Draw bounding box (Bonus) (function)

main()
