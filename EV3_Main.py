#!/usr/bin/env pybricks-micropython
import screen as screen

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color)
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# from angle.py import myfunction
# from pixel.py import myList


# Objects
ev3 = EV3Brick()
Motory = Motor(Port.A)
Motorx = Motor(Port.B)  #
Motorz = Motor(Port.C)  #
Button1 = TouchSensor(Port.S1)  # start-button?

# Variables
Winkel = 3
Angle = 0
z = 0
width = 20  # = img.size[0]
myList = []

# Program
"""x=0
while x<10:
    bigMotor.run_angle(1000,5)
    medMotor.run_angle(1000,360)
    wait(10)
    x += 1"""
"""img = Image.open('manSW.jpg')
width = img.size[0]
height = img.size[1]

for x in range(0, width):
    for y in range(0, height):
        pixel = (x,y)
        rgb = img.getpixel(pixel)
        if rgb<150:
            myList.append(True)
        elif rgb>=150:
            myList.append(False)
        else:
            break"""

# myList = [True, True, False, True, False, False, True, False, True, True, False, True, True, False, True, False,
#           False, False, False, False, False, False, False, False, True]
myList = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
          True, True, True, True]

# screen.load_image(manKlein.jpg)

while not Button1.pressed():
    continue

# program will continue when button is pressed

for x in myList:
    if z == width:
        Motorx.run_angle(-1000, Winkel * 20)
        Motory.run_angle(500, 90)
        z = 0
        Angle = 0
    else:
        Motorx.run_angle(1000, Winkel)
        if x:
            Motorz.run_angle(1000, 360)
        else:
            continue
        z += 1
        Angle += Winkel
Motorx.run_angle(-1000, Angle)
