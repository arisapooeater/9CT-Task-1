#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

obstacle_sensor = UltrasonicSensor(Port.S4)
colour_sensor = ColorSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
collected_obstacles = 0

# Write your program here.
ev3.speaker.beep()

while collected_obstacles < 2:
   colour = colour_sensor.color()
   robot.drive(200, 0)

   if obstacle_sensor.distance() < 300:
      wait(3)
      if colour == Color.RED:
         robot.turn(180) 
         robot.straight(200)
         robot.turn(90) 
         robot.straight(550)
         robot.turn(90) 
         robot.straight(200)
         robot.straight(-100)
         collected_obstacles += 1

      elif colour == Color.GREEN:
         ev3.speaker.beep()
         ev3.speaker.beep()
         ev3.speaker.beep()
         collected_obstacles += 1
      else
         robot.straight(-100)
         robot.turn(90)
         robot.straight(150)
         robot.turn(-90)
      