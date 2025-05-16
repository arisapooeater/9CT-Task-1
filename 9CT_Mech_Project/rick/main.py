# <-------------------------------------- SETUP -------------------------------------->
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

# <-------------------------------------- FUNCTIONS -------------------------------------->

def autodrive():
   
   while True:
       # Robot auto drives by driving 5 cm at a time while checking the if the if statement is true
      robot.drive(50, 0)
       # Once it detects an obstacle within 10 cm
      if obstacle_sensor.distance() < 100:
         robot.stop()
<<<<<<< Updated upstream
         if colour_sensor.reflection() > 50: # Colour sensor detects the floor is white (white reflects around 60-100 but the sheet is kind of off-white )
=======
         if colour_sensor.color() == 6: # Colour sensor detects the floor is white
>>>>>>> Stashed changes
            ev3.screen.clear()
            # The robot's screen displays that the floor is white (non-functional)
            ev3.screen.draw_text(20, 50, "w w waitt.. the floor MIGHT be white. heh.")
            wait(3000)
         # The robot's screen displays "Obstacle Detected!""
         ev3.screen.clear()
         ev3.screen.draw_text(20, 50, "Obstacle Detected!")

def move_path(forward1, turn1, forward2, turn2, forward3, turn3):
   robot.straight(forward1)
   robot.turn(turn1)
   robot.straight(forward2)
   robot.turn(turn2)
   robot.straight(forward3)
   robot.turn(turn3)

# <-------------------------------------- PROGRAM -------------------------------------->

# Beep to signal the program has started
ev3.speaker.beep()

# The robot drives up so it's facing the red obstacle
move_path(200, 107, 595, 107, 0, 0)

# Robot drives forward (toward red block) until the ultrasonic sensor detects it within 10 cm
autodrive()

# Robot moves forward 12 cm and turns back to capture obstacle
move_path(120, 196, 0, 0, 0, 0) 

# Robot going back to start area
move_path(200, -90, 595, -107, 200, 0)

# The robot drives up so it's facing the yellow obstacle
move_path(200, 107, 670, 107, 450, 107)

# Robot drives forward (toward yellow block) until the ultrasonic sensor detects it within 10 cm
autodrive()

# Robot going back to start area
move_path(500, -107, 200, 0, 0, 0)
