#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" o+ the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

obstacle_sensor = UltrasonicSensor(Port.S4)
colour_sensor = ColorSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


# Beep to signal the program has started
ev3.speaker.beep()

# The robot drives up so its facing the red obstacle
robot.straight(200)
robot.turn(107)
robot.straight(595)
robot.turn(107)

while True:
   # Robot autodrives using the while code
   robot.drive(50, 0)
   # Once it detects an obstacle within 10 cm
   if obstacle_sensor.distance() < 100:
      robot.stop()
      # Its screen displays "Obstacle Detected! :0"
      ev3.screen.clear()
      ev3.screen.draw_text(40, 50, "Obstacle Detected! :0")
      break

# If that obstacle is red
if colour_sensor.color() == Color.RED:
   # Its screen displays "RED Detected! :3"
   ev3.screen.clear()
   ev3.screen.draw_text(40, 50, "RED Detected! :3")
   robot.straight(120)
   robot.turn(196)    
   # Robot going back to start area
   robot.straight(200)
   robot.turn(-107)
   robot.straight(595)
   robot.turn(-107)
   robot.straight(200)

# The robot drives up so its facing the yellow obstacle
robot.straight(200)
robot.turn(107)
robot.straight(670)
robot.turn(107)
robot.straight(450)
robot.turn(107)

while True:
   # Robot autodrives using the while code
   robot.drive(50, 0)
   # Once it detects an obstacle within 10 cm
   if obstacle_sensor.distance() < 100:
      robot.stop()
      # Its screen displays "Obstacle Detected! :0"
      ev3.screen.clear()
      ev3.screen.draw_text(40, 50, "Obstacle Detected! :0")
      break

# If that obstacle is yellow
if colour_sensor.color() == Color.YELLOW:
   # Its screen displays "YELLOW Detected! :3"
   ev3.screen.clear()
   ev3.screen.draw_text(40, 50, "YELLOW Detected! :3")
   # Robot going back to start area
   robot.straight(500)
   robot.turn(-107)
   robot.straight(200)
