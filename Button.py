#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Initialize the motors.
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S4)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=70, axle_track=140)
ev3 = EV3Brick()
# Calculate the light threshold. Choose values based on your measurements.
BLACK = 6
WHITE = 90
Anpassung = 1.1
threshold = (BLACK + WHITE) / 2
Sollwert = threshold * Anpassung
trigger_distance = 300
# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 100

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 0.5
DIFFERENTIAL_GAIN = 5
INTEGRAL_GAIN = 0
old_deviation = 0
integral = 0
Dumb = 0.75
Mode = -1 # -1 = right; 1 = left --> rechts bzw. links von dem Strich orientieren
arisList = ['rechts','links']
Ariles = 0

#Roboter ist auf linker Spur und wechselt nach rechts
def rechts():
    robot.turn(40)
    while line_sensor.reflection()>Sollwert:
        robot.drive(150,-4)
    global Mode
    Mode = 1
#Roboter ist auf rechter Spur und wechselt nach links
def links():
    robot.turn(-40)
    while line_sensor.reflection()>Sollwert:
        robot.drive(150,4)
    global Mode
    Mode = -1

# ask on which lane the robot is starting
'''
ev3.screen.print("insert lane")
while True:
    if Button.LEFT in ev3.buttons.pressed():
        Mode = 1
        ev3.screen.print("starting left!")
        sleep(3)
        break
    elif Button.RIGHT in ev3.buttons.pressed():
        Mode = -1
        ev3.screen.print("starting right!")
        sleep(3)
        break
    continue
ev3.screen.clear()
sleep(3)'''



# Start following the line endlessly.
while True:
    deviation = line_sensor.reflection() - Sollwert
    distance = ultrasonic_sensor.distance()
    integral = deviation + integral

    p = PROPORTIONAL_GAIN * deviation
    d = DIFFERENTIAL_GAIN * (deviation-old_deviation)
    i = INTEGRAL_GAIN*(integral)

    turn_rate = Mode*Dumb*(p+d+i)
    old_deviation = deviation
    robot.drive(DRIVE_SPEED, turn_rate)

    if distance<trigger_distance:
        if arisList[Ariles] == 'rechts':
            rechts()
            Ariles += 1
        elif arisList[Ariles] == 'links':
            links()
            Ariles += 1
