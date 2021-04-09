#CPSC 231
#Name: Daniel Jin
#Tutorial: Shauvik Shadman
#ID: 30107081
#Date: 2019-11-12
#Description: This program will first either draw stars or star names at a givin location given from a file. If the arguments inputed with this module includes "-names" and a star file,
#it will not ask for a star input
#after the stars or star names are drawn, it will ask for a constellation a draw the given constellation file.

import sys
import os
import turtle

WIDTH = 600
HEIGHT = 600
AXISCOLOR = "blue"
#constant for making tick lines on axis
TICK = 6 
#text distance apart from axis
AXISLABEL = 12
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"
#this function is used to get the values and scale it to 300 (so that the decimal values can be spaced on a 600x600 window
def convert (x,y):
    newX = 300 + x*300 
    newY = 300 + y*300
    return newX, newY
#this function is used to get the pen color, which changes everytime a new constellation is inuputed
def penColor(colorCounter):
    newColor = colorCounter % 3
    if newColor == 0:
        pen = "red"
    elif newColor == 1:
        pen = "green"
    else:
        pen = "yellow"
    return pen
#this function is used to draw the ticks and values for each tick on the x axis
def drawXTickLabel(pointer):
    x = 0
    y = 0
    #positive side (rightside)
    while x <= 1:
        newX, newY = convert(x,y)
        pointer.goto(newX,newY)
        pointer.down()
        pointer.goto(newX, newY + TICK)
        pointer.goto(newX,newY - TICK)
        pointer.up()
        pointer.goto(newX,newY + AXISLABEL)
        if x != 0:
            pointer.write(str(x))
        x += 0.25
    x = 0
    y = 0
    #negative side (leftside)
    while x >= -1:
        newX, newY = convert(x,y)
        pointer.goto(newX,newY)
        pointer.down()
        pointer.goto(newX, newY + TICK)
        pointer.goto(newX,newY - TICK)
        pointer.up()
        pointer.goto(newX,newY + AXISLABEL)
        if x != 0:
            pointer.write(str(x))
        x -= 0.25
#this function is used to draw the ticks and values for each tick on the y axis       
def drawYTickLabel(pointer):    
    x = 0
    y = 0
    #positive side (rightside)
    while y <= 1:
        newX, newY = convert(x,y)
        pointer.goto(newX,newY)
        pointer.down()
        pointer.goto(newX + TICK, newY)
        pointer.goto(newX - TICK,newY)
        pointer.up()
        pointer.goto(newX + AXISLABEL,newY)
        if y != 0:
            pointer.write(str(y))
        y += 0.25
    x = 0
    y = 0
    #negative side (left side)
    while y >= -1:
        newX, newY = convert(x,y)
        pointer.goto(newX,newY)
        pointer.down()
        pointer.goto(newX + TICK, newY)
        pointer.goto(newX - TICK,newY)
        pointer.up()
        pointer.goto(newX + AXISLABEL,newY)
        if y != 0:
            pointer.write(str(y))
        y -= 0.25
#this function is used to draw both axis (x and y) with the origin at 300,300 (WIDTH/2.HEIGHT/2)        
def drawAxis(pointer):
    pointer.color(AXISCOLOR)
    pointer.goto(WIDTH/2,0)
    pointer.down()
    pointer.goto(WIDTH/2,HEIGHT)
    pointer.up()
    pointer.goto(0,HEIGHT/2)
    pointer.down()
    pointer.goto(WIDTH,HEIGHT/2)
    pointer.up
    drawXTickLabel(pointer)
    drawYTickLabel(pointer)
    
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)
    pointer.speed(0)
    pointer.up()
    return pointer
#this function checks if the given file is located in the same directory as this module, and if it exists or not
#if the file cannot be found it asks the user to input one until the input nothing("")
def errorCheck(file):
    error_code = 1
    while file != "":
        if os.path.isfile(file) == True:
            return file
        else:
            print(f"File {file} could not be found.")
            file = input("Input a valid star location file: ")
    sys.exit(1)
#this function is used to check the given arguments
#if the argument(s) is just this module, then it asks the user for a starlocation file
#if the argument(s) is 1, it first identifies if it's either a starlocation file or "-name". If neither, it sends an error (if its an invalid file it asks until the user enters in nothing("")),
#If the given argument given is "-names" it prompts a question asking for the star location file, until "" is entered.
#If the argument(s) is 2, if identifies whether the first or second argument is a file or "-names". if any of the arguments is invalid, it will say so and exit
#if the argument(s) is more than 2, it will say that there are too many arguments and exit
#Every argument is also checked if its a valid file or not, or if it is "-names"
def readArg():
    length = len(sys.argv)
    if length == 1:
        file = input("Input in a star location file: ")
        file = errorCheck(file)
        names = False
        return file, names
    if length == 2:
        if sys.argv[1] == "-names":
            file = input("Input in a star location file: ")
            file = errorCheck(file)
            names = True
            return file, names
        else:
            star_file = sys.argv[1]
            star_file = errorCheck(star_file)
            names = False
            return star_file, names
    if length == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        check1 = os.path.isfile(arg1)
        check2 = os.path.isfile(arg2)
        if (check1 == True) and (check2 == True):
            print("Neither arguments included '-names'")
            sys.exit(0)
        if (check1 == False) and (check2 == False):
            print("Invalid input")
            sys.exit(0)   
        if (check1 == True) or (arg1 == "-names"):
            if arg1 == "-names":
                file = errorCheck(arg2)
                names = True
                return file,names
            if check1 == True:
                file = errorCheck(arg1)
                if arg2 == "-names":
                    names = True
                    return file,names
        if (check1 == True) and (check2 == False):
            print(f"Second argument:'{arg2}' is invalid")
            sys.exit(0)
        if (check1 == False) and (check2 == True):
            print(f"First argument:'{arg1}' is invalid")
            sys.exit(0)
    if length > 3:
        print("Too many arguments")
        sys.exit(0)
#This function gets the given star file and splits it for each coma.
#After spliting it, each entity is sorted by either x or y or mag or name
#it also strips "\n" at the end of each line, to keep the name of stars consistent
#finally, if there is a name for the star, it splits it for each semi-colon (just in case) and then if there is a semi-colon, the name is sorted as: firstname,secondname
#This is meant to make it easier to read in dictionary, and also to print it in a clearner way
#However if the given file is not a star location file it will exit the program
def starData (data):
    try:
        data = data.split(",")
        x = float(data[0])
        y = float(data[1])
        mag = float(data[4])
        names = data[6].strip("\n")
        namelist = names.split(";")
        listlength = len(namelist)
        if listlength == 1:
            name = namelist[0].lstrip(" ")
        else:
            name = ""
            for i in namelist:
                name += i.lstrip(" ")
                if i != namelist[listlength-1]:
                    name += ", "
        return x,y,mag,name
    except:
        print("The given file was not a star location file")
        exit()

#This function first identifies if the given arguments had "-names" or not.
#If the arguments inputed did not have "-names" it draws stars
#If the arguments inputed did have "-names" it draws star names
def readDrawStars (file,pointer,names):
    if names == False:
        stars = open(file)
        starlist = stars.readlines()
        length = len(starlist)
        counter = 1
        while counter <= length:
            data = starlist[counter-1]
            x,y,mag,name = starData(data)
            drawStar(x,y,mag,name,pointer)
            counter += 1
        stars.close()
    if names == True:
        stars = open(file)
        starlist = stars.readlines()
        length = len(starlist)
        counter = 1
        while counter <= length:
            data = starlist[counter-1]
            x,y,mag,name = starData(data)
            drawNames(x,y,name,pointer)
            counter += 1
        stars.close()
#this function first indentifies if the given star has a name or not.
#if there is a name, it draws a white star
#if there is no name, it draws a grey star
def drawStar(x,y,mag,name,pointer):
    newX, newY = convert(x, y)
    radius = (10/(mag+2))/2
    pointer.up()
    pointer.goto(newX,newY-radius)
    if name.strip("\n") != "":
        pointer.fillcolor(STARCOLOR)
        pointer.color(STARCOLOR)
        pointer.down()
        pointer.begin_fill()
        pointer.circle(radius)
        pointer.end_fill()
    else:
        pointer.fillcolor(STARCOLOR2)
        pointer.color(STARCOLOR2)
        pointer.down()
        pointer.begin_fill()
        pointer.circle(radius)
        pointer.end_fill()
    pointer.up()
#this function is used to draw the name of the stars at a given location   
def drawNames(x,y,name,pointer):
    newX, newY = convert(x,y)
    pointer.up()
    pointer.color(STARCOLOR)
    pointer.goto(newX,newY)
    pointer.write(name,font=("Arial",5,"normal"))
    pointer.up()
#this function is used to draw a line, it takes the first point and then the end point, and draws a line in between them.    
def drawConstell(x,y,newX,newY,pointer,counter):
    startX,startY = convert(x,y)
    endX, endY = convert(newX,newY)
    pointer.up()
    pointer.color(penColor(counter))
    pointer.goto(startX,startY)
    pointer.down()
    pointer.goto(endX,endY)
    pointer.up()
#This function is used to make a dictionary.
#It first identifies if the star has a name or not. If there is a name, it checks if there are two or more names (spliting it by ", ").
#It then stores the name(s) as the key and the given x,y location as its value.
#if there is no name, it skips the star.
def starDictionary (starFile):
    myStarDictionary = {}
    stars = open(starFile)
    starlist = stars.readlines()
    length = len(starlist)
    counter = 1
    while counter <= length:
        data = starlist[counter-1]
        x,y,mag,name = starData(data)
        if name != "":
            if ", " in name:
                listofnames = name.split(", ")
                for Name in listofnames:
                    myStarDictionary[Name] = x,y
            else:
                myStarDictionary[name] = x,y
        counter += 1
    stars.close()
    return myStarDictionary
#this function is used to read the given constellation file.
#it reads the file and puts it all in a list
#it then takes the first line as the name of the constellation
#then after the first line, every other line is recorded as the starting value and ending value, separated by a comma.
#first it gets the starting values and uses it as a key to find the values in the star dictionary.
#then it gets the ending values and does the same thing.
#once the values are recieved, it draws the line
#after every line is used, it prtints out the name of the constellation and the stars(with names) that was used to make the given constellation.
#if the given file is not a constellation file, it will print that it was not a constellation file.
def readConstell(conFile,starfile,pointer,counter):
    try:
        starDict = starDictionary(starfile)
        constell = open(conFile)
        conList = constell.readlines()
        constellName = conList[0].strip("\n")
        conLength = len(conList)
        colorCounter = counter
        starsContained = []
        counter = 1
        while counter < conLength:
            namesForEdge = conList[counter].split(",")
            startName = namesForEdge[0].strip("\n")
            endName = namesForEdge[1].strip("\n")
            starsContained += (startName,endName)
            first = starDict[startName]
            startX = first[0]
            startY = first[1]
            end = starDict[endName]
            endX = end[0]
            endY = end[1]
            drawConstell(startX,startY,endX,endY,pointer,colorCounter)
            counter += 1
        #the code is insipred from https://stackoverflow.com/questions/29312508/how-do-i-remove-duplicate-words-from-a-list-in-python-without-using-sets
        #the code deletes any duplicated entities in the list
        starsContained = sorted(set(starsContained), key = lambda x:starsContained.index(x))
        constell.close()
        print(f"{constellName} constellation contains {starsContained}")
    except:
        print("The given file was not a constellation file")
#this function asks the user to input a constellation file until "" is inputed
#if the file is invalid, it asks again
#once the file is valid, it reads the file, and then draws the constellation, and asks for another input.
def inputConstell(starFile,pointer):
    constellFile = input("Enter in constellation filename: ")
    counter = 1
    checkConstell = os.path.isfile(constellFile)
    while checkConstell == False and constellFile != "":
        constellFile = input("Enter in a valid constellation filename: ")
        checkConstell = os.path.isfile(constellFile)
    while constellFile != "" and checkConstell == True:
        readConstell(constellFile, starFile,pointer,counter)
        counter +=1
        constellFile = input("Enter in another constellation filename: ")
        checkConstell = os.path.isfile(constellFile)
        while checkConstell == False and constellFile != "":
            constellFile = input("Enter in a valid constellation filename: ")
            checkConstell = os.path.isfile(constellFile)
    sys.exit(0)
def main():
    #Handle arguments
    file,names = readArg()
    #Read star information from file (function)
    pointer = setup()
    #Draw Axes (function)
    drawAxis(pointer)
    #Draw Stars (function)
    readDrawStars(file,pointer,names)
    #Loop getting filenames
    inputConstell(file,pointer)
        #Read constellation file (function)
            #this function is within the function: inputConstell(file,pointer)
        #Draw Constellation (function)
            #this function is also within the function: inputConstell(file,pointer)
        #Draw bounding box (Bonus) (function)
            #no bonus

main()
