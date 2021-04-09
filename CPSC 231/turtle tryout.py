
import turtle
WIDTH = 800
HEIGHT = 600
TICK = 5
textLocation = 20
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    return pointer 

def getColor(colorCounter):
    newColor = colorCounter % 3
    if newColor == 0:
        pen = "red"
    elif newColor == 1:
        pen = "green"
    else:
        pen = "blue"
    return pen
            
def screenCoor(xo, yo, ratio, x, y):
    screenX = (xo + ratio * x)
    screenY = (yo + ratio * y)
    return screenX, screenY

def drawXAxis(pointer, xo, yo, ratio):
    pointer.up()
    pointer.goto(xo,yo)
    x = 0
    y = 0
    while x <= 10: #for now
        newX, newY = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(newX,yo)
        drawXAxisLabelTick(pointer, newX, newY, x)
        x += 1
    xmax = x
    x = 0
    while x >= -10:
        newX, newY = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(newX,yo)
        drawXAxisLabelTick(pointer, newX, newY, x)
        x -= 1
    xmin = x
    return xmin, xmax

def drawXAxisLabelTick(pointer, newX, newY, x):
    pointer.goto(newX,newY)
    pointer.down()
    pointer.goto(newX,newY + TICK)
    pointer.goto(newX,newY)
    pointer.goto(newX,newY - TICK)
    pointer.goto(newX,newY)
    pointer.up()
    pointer.goto(newX, newY - textLocation)
    if x != 0:
        pointer.write(str(x))
    pointer.goto(newX,newY)

def drawYAxis(pointer, xo, yo, ratio):
    pointer.goto(xo,yo)
    x = 0
    y = 0
    while y <= 10: #for now
        newX, newY = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(xo,newY)
        drawYAxisLabelTick(pointer, newX, newY, y)
        y += 1
    ymax = y
    y = 0
    while y >= -10:
        newX, newY = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(xo,newY)
        drawYAxisLabelTick(pointer, newX, newY, y)
        y -= 1
    ymin = y
    return ymin, ymax
def drawYAxisLabelTick(pointer, newX, newY, y):
    pointer.goto(newX,newY)
    pointer.down()
    pointer.goto(newX + TICK, newY)
    pointer.goto(newX,newY)
    pointer.goto(newX - TICK, newY)
    pointer.goto(newX,newY)
    pointer.up()
    pointer.goto(newX - textLocation, newY)
    if y != 0:
        pointer.write(str(y))
    pointer.goto(newX,newY)
    
def drawExpr(pointer, xo, yo, ratio, XMIN, XMAX, expr):
    for x in range (XMIN,XMAX):
        y = eval(expr)
        pointer.goto(x*ratio + xo,y*ratio + yo)
        pointer.down()
pointer = setup()
xo = int(input("put in x vaule for oirigin: "))
yo = int(input("put in y vaule for origin :"))
ratio = int(input("put in ratio value: "))

XMIN, XMAX = drawXAxis(pointer, xo, yo, ratio)
YMIN, YMAX = drawYAxis(pointer, xo, yo, ratio)


expr = input("Enter an arithmetic expression: ")
counter = 0
while expr != "":
    pointer.color(getColor(counter))
    drawExpr(pointer, xo, yo, ratio, XMIN, XMAX, expr)
    pointer.up()
    expr = input("Enter an arithmetic expression: ")
    counter += 1
    
    
turtle.exitonclick()
