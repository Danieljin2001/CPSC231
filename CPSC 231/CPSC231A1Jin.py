# CPSC 231
# Name: Daniel Jin
# Tutorial: Shauvik Shadman
# ID: 30107081
# Date: 2019-09-26
# Description: This program will determine if a given circle and a given line intersects.
#importing libraries
import turtle
import math
#constants for screen setup
WIDTH = 800
HEIGHT = 600
#screen setup
T = turtle.Turtle() #this is a constant for turtle commands to make things easier
screen = turtle.getscreen()
screen.setup(WIDTH,HEIGHT,0,0)
screen.setworldcoordinates(0,0,WIDTH,HEIGHT)
#no animation for drawing
T.speed(0)
#making x and y lines
T.hideturtle()
T.up()
T.goto(400,0)
T.down()
T.goto(400,600)
T.up()
T.goto(0,300)
T.down()
T.goto(800,300)
T.hideturtle()
#Describing to the user what this program does
#source for code inspiration: https://d2l.ucalgary.ca/d2l/le/content/278087/viewContent/3661006/View
print("This program will draw a circle and a line")
print("After doing so, the program will determine whether the line intersects with the circle.")
print("The bottom left corner of visible screen is (0,0) in cartesian coordinates, the top right corner is (800,600).")
#asking the user for the (x,y) of centre of the circle, and then the radius
xc= int(input("Enter in the x value of the centre of the circle: "))
yc1= int(input("Enter in the y value of the centre of the circle: "))
r= float(input("Enter in the radius of the circle: "))
yc=yc1-r #to draw with the center actually in the center
#this will start drawing the circle
T.pencolor("red")
T.up()
T.goto(xc,yc)
T.down()
T.circle(r,360)
#asking the user for the (x,y) of when the line starts, and then the (x,y) for when it ends
#using integers
x1 = int(input("Enter in the x value of the start of line: "))
y1 = int(input("Enter in the y value of the start of line: "))
x2 = int(input("Enter in the x value of the end of line: "))
y2 = int(input("Enter in the y value of the end of line: "))
#this will start drawing the line
T.pencolor("blue")
T.up()
T.goto(x1,y1)
T.down()
T.goto(x2,y2)
#constants for making quadratic formula
A = (x2-x1)**2 + (y2-y1)**2
B = 2*((x1-xc)*(x2-x1) + (y1-yc1)*(y2-y1)) #have to use yc1 value because that is the real center value
C = (x1-xc)**2 + (y1-yc1)**2 - r**2
RADICAND = B**2 - (4*A*C)
radicandGreaterThanZero = RADICAND > 0
radicandLessThanZero = RADICAND < 0
#checking if the solutions have intersections or not and puts in text if it does. If not, a green dot appears at intersection point.
T.up()
T.color("green")
#these were inspired by codes from https://d2l.ucalgary.ca/d2l/le/content/278087/viewContent/3663578/View
if radicandGreaterThanZero:
    SQUARE = math.sqrt(RADICAND) #square rooting RADICAND
    alphaPositive = (0-B + SQUARE)/(2*A) #first intersect
    alphaNegitive = (0-B - SQUARE)/(2*A) #second intersect
    xValueIntersectionFirst = (1-alphaPositive)*x1 + alphaPositive * x2
    yValueIntersectionFirst = (1-alphaPositive)*y1 + alphaPositive * y2
    T.goto(xValueIntersectionFirst,yValueIntersectionFirst)
    T.down()
    T.begin_fill()
    T.circle(5)
    T.end_fill()
    T.up()
    xValueIntersectionSecond = (1-alphaNegitive)*x1 + alphaNegitive * x2
    yValueIntersectionSecond = (1-alphaNegitive)*y1 + alphaNegitive * y2
    T.goto(xValueIntersectionSecond,yValueIntersectionSecond)
    T.down()
    T.begin_fill()
    T.circle(5)
    T.end_fill()
elif RADICAND == 0: #when RADICAND equals to zero
    ALPHA = (-B)/(2*A) #alpha value, one one because - 0 and + 0 is the same thing
    xValueIntersection = (1-ALPHA)*x1 + ALPHA * x2
    yValueIntersection = (1-ALPHA)*y1 + ALPHA * y2
    T.goto(xValueIntersection,yValueIntersection)
    T.down()
    T.begin_fill()
    T.circle(5)
    T.end_fill()
elif radicandLessThanZero:
    T.goto(400,300)
    T.write("NO INTERSECTION!")
turtle.exitonclick()
