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

# The robot drives up so it's facing the red obstacle
robot.straight(200)
robot.turn(107)
robot.straight(595)
robot.turn(107)

while True:
   # Robot auto drives by driving 5 cm at a time while checking the if the if statement is true
   robot.drive(50, 0)
   # Once it detects an obstacle within 10 cm
   if obstacle_sensor.distance() < 100:
      robot.stop()
      # Its screen displays "Obstacle Detected! :0"
      ev3.screen.clear()
      ev3.screen.draw_text(20, 50, "Obstacle Detected!")
      # Robot moves forward 12 cm and turns back to capture obstacle
      robot.straight(120)
      robot.turn(196)    
      # Robot going back to start area
      robot.straight(200)
      robot.turn(-107)
      robot.straight(595)
      robot.turn(-107)
      robot.straight(200)
      break

# The robot drives up so it's facing the yellow obstacle
robot.straight(200)
robot.turn(107)
robot.straight(670)
robot.turn(107)
robot.straight(450)
robot.turn(107)

while True:
   # Robot auto drives by driving 5 cm at a time while checking the if the if statement is true
   robot.drive(50, 0)
   # Once it detects an obstacle within 10 cm
   if obstacle_sensor.distance() < 100:
      robot.stop()
      if colour_sensor.color()  == 6:  # Colour sensor detects the floor is white
        ev3.screen_clear()
        # The robot's screen displays that the floor is white (non-functional)
        ev3.screen.draw_text(20, 50, "w w waitt.. the floor MIGHT be white. heh.")
        wait(3000)
      # The robot's screen displays "Obstacle Detected!"
      ev3.screen.clear()
      ev3.screen.draw_text(20, 50, "Obstacle Detected!")
      # Robot going back to start area
      robot.straight(500)
      robot.turn(-107)
      robot.straight(200)
      
