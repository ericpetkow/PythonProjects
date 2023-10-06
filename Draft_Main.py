# !/usr/bin/env pybricks-micropython
import screen
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

from angle.py import myfunction
from pixel.py import myList


# Objects
ev3 = EV3Brick()
Motory = Motor(Port.A)  # moves length
Motorx = Motor(Port.B)  # moves width
Motorz = Motor(Port.C)  # moves pen
Button1 = TouchSensor(Port.S1)  # start-button
Button2 = TouchSensor(Port.S2)
SheetTracker = ColorSensor(Port.S3)

# Variables
z = 0  # Zählvariabel
Winkelx = 6  # X
Angle = 0
Randx = 5
yRotation = 7.9  # Y
yVerschiebung = 0.5
Winkely = (yVerschiebung / yRotation) * 360
Randy = 5
Breite = 26

# Program
for x in range(10):
    bigMotor.run_angle(1000, 5)
    medMotor.run_angle(1000, 360)
    wait(10)


img = Image.open('manSW.jpg')
width = img.size[0]
height = img.size[1]

for x in range(0, width):
    for y in range(0, height):
        pixel = (x, y)
        rgb = img.getpixel(pixel)
        print(rgb)
        break

myList = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True,
          True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, True, False, False, False, False, False, False, False, True, True, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False,
          False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False,
          False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False,
          False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False,
          True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,
          False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False,
          False, False, False, True, False, False, False, False, False, True, False, False, False, False, True, False,
          False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False,
          False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, True,
          False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False,
          False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False,
          True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False,
          False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False,
          False, False, True, False, False, False, False, True, False, False, False, False, False, False, True, False,
          False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False,
          False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, True,
          False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False,
          False, False, False, True, False, False, False, False, False, False, True, True, True, True, False, False,
          False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False,
          False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False,
          False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False,
          False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,
          True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True,
          True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, False, False, False, False]
screen.load_image('manKlein.jpg')

while not SheetTracker.color() == Color.WHITE:
    continue
Motory.run_angle(500, 90)

while not Button1.pressed():
    continue
# rest of code

# predict white line and skip row
picWidth = 20
counter = 0
whiteLine = True

for x in range(0, len(myList), picWidth):
    for y in range(counter, picWidth):
        if myList[y]:
            whiteLine = False
            break
# if whiteLine:
# skip row


z = 0
for x in myList:
    if Button2.pressed():
        break
    elif z == Breite:
        Motorx.run_angle(-1000, Winkelx * Breite)
        Motory.run_angle(500, Winkely)
        z = 0
        Angle = 0
    else:
        Motorx.run_angle(1000, Winkelx)
        if x:
            Motorz.run_angle(1000, 360)
            z += 1
            Angle += Winkelx
        else:
            z += 1
            Angle += Winkelx
            continue

Motorx.run_angle(-1000, Angle)
