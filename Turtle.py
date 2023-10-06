import turtle
from PIL import Image
from PIL import ImageFilter


# method stuff
def convertPixelsToList():
    pixelList = []

    for y in range(0, picHeight):
        for x in range(0, picWidth):
            pixelList.append(new_BW.getpixel((x, y)))

    return pixelList


def convertPixelListToBoolList():
    def_boolList = []

    for x in range(0, picWidth * picHeight):
        if pixelList[x] == 0:
            def_boolList.append(True)
        else:
            def_boolList.append(False)

    return def_boolList


def cropListAndReverse():
    del boolList[(picHeight * picWidth):]  # deletes everything above picture dimension

    for x in range(1, picHeight, 2):  # sometimes picture is mirrored --> FIX
        newList = []
        for y in range(x * picWidth, x * picWidth + picWidth):
            newList.append(boolList[y])
        newList.reverse()

        counter = 0
        for y in range(x * picWidth, x * picWidth + picWidth):
            boolList[y] = newList[counter]
            counter += 1

    return boolList


def getWhiteLines():
    counter = 0
    whiteLine = True
    whiteLineList = []

    for x in range(0, picWidth * picHeight, picWidth):
        for y in range(counter, picWidth + counter):
            if finalList[y]:
                whiteLine = False
                break
        if whiteLine:
            whiteLineList.append(True)  # meaning: there is a white line
        else:
            whiteLineList.append(False)  # meaning: there is not a white line

        counter += picWidth
        whiteLine = True

    return whiteLineList


def startTurtle():
    t = turtle.Turtle()
    turtle.setworldcoordinates(0, picHeight, picWidth, 0)
    t.penup()
    t.shape("square")  # only useful when t.stamp()
    t.shapesize(1.2)  # only useful when t.stamp()
    # t.pensize(2) # only useful when t.dot()
    t.speed(0)

    for row in range(0, picHeight):
        if whiteLineList[row]:
            t.setheading(90)  # south
            t.forward(1)
            if int(t.xcor()) == 0:
                t.setheading(0)  # east
            else:
                t.setheading(180)  # west
            continue

        for column in range(0, picWidth):
            if boolList[column + picWidth * row]:
                t.stamp()  # t.dot()
            if column != picWidth - 1:  # checks if it should prepare for next x-cor
                t.forward(1)

        if int(t.ycor()) != picHeight - 1:  # checks if it should prepare for next y-cor
            if int(t.xcor()) == 0:
                t.setheading(90)  # south
                t.forward(1)
                t.setheading(0)  # east
            else:
                t.setheading(90)  # south
                t.forward(1)
                t.setheading(180)  # west

    turtle.done()  # keeps window open


"""START OF PROGRAM"""

# image stuff

# this opens image and converts to pure Black and White
img = Image.open('TestingPictures/woman1.jpeg')
img.filter(ImageFilter.CONTOUR)
img = img.resize((50, int(img.size[1] * (50 / img.size[0]))))

thresh = 105  # setting a threshold from when a pixel is seen as B&W
fn = lambda x: 255 if x > thresh else 0
r = img.convert('L').point(fn, mode='1')
r.save('TestingPictures/new_BW.png')
new_BW = Image.open("TestingPictures/new_BW.png")

picWidth = new_BW.size[0]
picHeight = new_BW.size[1]

"""CALLING METHODS"""

pixelList = convertPixelsToList()  # List with RGB-value (0 or 255)

boolList = convertPixelListToBoolList()  # converts RGB-value to True or False)

finalList = cropListAndReverse()  # adjusts List so that turtle prints the right dots

whiteLineList = getWhiteLines()  # lists empty Lines

startTurtle()
