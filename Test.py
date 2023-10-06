import turtle
from PIL import Image
from PIL import ImageFilter

"""EDITING PICTURE"""

img = Image.open('TestingPictures/smiley.jpeg')
img.filter(ImageFilter.CONTOUR)
img = img.resize((50, int(img.size[1] * (50 / img.size[0]))))

thresh = 105  # setting a threshold from when a pixel is seen as B&W
fn = lambda x: 255 if x > thresh else 0
r = img.convert('L').point(fn, mode='1')
r.save('TestingPictures/new_BW.png')
new_BW = Image.open("TestingPictures/new_BW.png")

width = new_BW.size[0]
height = new_BW.size[1]

"""DEFINING METHODS"""


def getPixelList():
    pixelList = []

    for y in range(0, height):
        for x in range(0, width):
            pixelList.append(new_BW.getpixel((x, y)))

    return pixelList


def getBoolList():
    boolList = []

    for x in range(0, width * height):
        if PixelList[x] == 0:
            boolList.append(True)
        else:
            boolList.append(False)

    return boolList


def getRowList():
    rowList = list()  # List with Bools of every row -> 2D List
    for i in range(0, len(BoolList), width):
        rowList.append(BoolList[i: i + width])

    return rowList


def getNextList():
    nextList = []  # List with Bools and Nexts where row ends or is skipped -> 2D List either Bools or Next

    whiteLine = True

    for j in range(height):
        for k in range(width):
            if RowList[j][k]:
                whiteLine = False
                break

        if not whiteLine:
            nextList.append(RowList[j])

        nextList.append("next")

        whiteLine = True

    return nextList


def reverseNextList():
    reverseBool = False
    for l in range(0, len(NextList)):
        if NextList[l] == "next":
            continue
        if reverseBool:
            NextList[l].reverse()

        reverseBool = not reverseBool


def getStepList():
    stepList = []  # list with steps in each row until pen down and with nexts

    for x in range(len(NextList)):
        stepCounter = 0
        if NextList[x] == "next":
            stepList.append("next")
            continue
        appendedList = []  # necessary to get all steps in one row in on list
        for y in range(width):
            if NextList[x][y]:
                appendedList.append(stepCounter)
                stepCounter = 1
            else:
                stepCounter += 1

        stepList.append(appendedList)

    return stepList


def startTurtle():
    t = turtle.Turtle()
    turtle.setworldcoordinates(0, height, width, 0)
    t.penup()
    t.shape("square")
    t.shapesize(1.2)
    t.speed(0)

    rightDirection = True
    placeholder = None  # necessary to know if previous element in StepList was 'next' ; initial value = None

    for m in StepList:
        if m == "next":
            t.setheading(90)  # south
            t.forward(1)
        else:
            distanceToBorder = width - 1
            for x in m:
                distanceToBorder -= x
                if rightDirection:
                    t.setheading(0)  # east
                    t.forward(x)
                    t.stamp()
                else:
                    t.setheading(180)  # west
                    t.forward(x)
                    t.stamp()

            t.forward(distanceToBorder)

        if m == "next" and placeholder != "next" and placeholder is not None:
            rightDirection = not rightDirection

        placeholder = m

    turtle.done()  # keeps window open


"""CALLING METHODS"""

PixelList = getPixelList()

BoolList = getBoolList()

RowList = getRowList()

NextList = getNextList()

reverseNextList()

StepList = getStepList()

startTurtle()
