from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port, Stop
from pybricks.media.ev3dev import Image


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

        if whiteLine:
            nextList.append("next")
        else:
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


def startPrint():
    Prozent = 1
    rightDirection = True  # meaning: direction = right
    placeholder = None  # necessary to know if previous element in StepList was 'next'

    for m in StepList:
        if m == "next":
            Motory.run_angle(-1000, Winkely)
            Screen(Prozent)
            Prozent += 1

        else:
            distanceToBorder = 0
            for x in m:
                distanceToBorder += x
                if rightDirection:
                    Motorx.run_angle(1000, Winkelx * x)
                    Motorz.run_angle(1000, 360)

                else:
                    Motorx.run_angle(-1000, Winkelx * x)
                    Motorz.run_angle(1000, 360)
            if rightDirection:
                Motorx.run_angle(1000, Winkelx * (width - distanceToBorder - 1))
            else:
                Motorx.run_angle(-1000, Winkelx * (width - distanceToBorder - 1))

        if m == "next" and placeholder != "next" and placeholder is not None:
            rightDirection = not rightDirection  # reverses direction
        placeholder = m


def Signatur():
    Motorx.run_until_stalled(-300, Stop.COAST, 20)
    Motorx.run_angle(1000, 100)
    Motory.run_angle(-1000, 10 * Winkely)
    # Malen
    Motorz.run_angle(1000, 360)
    Motorx.run_angle(1000, 4 * Winkelx)
    Motorz.run_angle(1000, 360)
    Motory.run_angle(-1000, 2 * Winkely)
    Motorx.run_angle(1000, 2 * Winkelx)
    Motorz.run_angle(1000, 90)
    Motory.run_angle(-1000, 2 * Winkely)
    Motorx.run_angle(-1000, 9 * Winkelx)
    Motory.run_angle(1000, 2 * Winkely)
    Motorz.run_angle(-1000, 90)


def Screen(Prozent):
    ev3.screen.clear()
    ev3.screen.load_image(BILD)
    ev3.screen.draw_text(20, 100, "printing... " + (str(int(Prozent * (100 / height))) + "%"))


"""CALLING METHODS"""

ev3 = EV3Brick()
Motory = Motor(Port.A)
Motorx = Motor(Port.B)
Motorz = Motor(Port.C)
Button1 = TouchSensor(Port.S4)
BILD = Image('john.png')

width = 26
height = 26

Winkelx = 6  # X
Winkely = 15  # (yVerschiebung/yRotation)*360

BoolList = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, True, False, False, False, False,
            False, False, False, False, False, False, True, False, False, False, False, False, False, False, False,
            False, False, False, False, False, True, False, False, False, False, False, False, False, False, False,
            False, False, False, True, False, False, False, False, False, False, False, False, False, False, False,
            True, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            True, False, False, False, False, False, False, False, False, False, True, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, True, False, False,
            False, False, False, False, False, False, True, False, False, False, False, False, True, False, False,
            False, False, True, False, False, False, False, False, True, False, False, False, False, False, False,
            False, True, False, False, False, False, False, False, True, False, False, False, False, True, False, False,
            False, False, False, False, True, False, False, False, False, False, False, True, False, False, False,
            False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, True,
            False, False, False, False, False, False, True, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, True, False, False, False, False,
            False, False, True, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False,
            False, False, False, False, True, False, False, False, False, False, False, True, False, False, False,
            False, True, False,
            False, False, False, False, False, False, False, True, False, False, False, False, True, False, False,
            False, False, False, False, True, False, False, False, False, False, True, False, False, False, False,
            False, False, True, False, False, False, False, False, True, False, False, False, False, False, False,
            False, True, False, False, False, False, False, True, False, False, False, False, True, False, False, False,
            False, False, True, False, False, False, False, False, False, False, False, True, False, False, False,
            False, False, False, True, True, True, True, False, False, False, False, False, False, True, False, False,
            False, False, False, False, False, False, False, True, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, True, False, False, False, False, False, False, False,
            False, False, False, False, True, False, False, False, False, False, False, False, False, False, False,
            False, False, True, False, False, False, False, False, False, False, False, False, False, False, False,
            False, True, False, False, False, False, False, False, False, False, False, False, True, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, True, True,
            False, False, False, False, False, False, True, True, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True,
            True, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False]

RowList = getRowList()

NextList = getNextList()

reverseNextList()

StepList = getStepList()

Motorx.run_until_stalled(-300, Stop.COAST, 20)
Motorx.run_angle(1000, 20)

ev3.screen.draw_text(30, 55, "press button")
ev3.screen.draw_text(60, 70, "to start")
while not Button1.pressed():
    continue

startPrint()

Signatur()
