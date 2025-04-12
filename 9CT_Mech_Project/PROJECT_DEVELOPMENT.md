# 9CT Assessment Task 1
### *By Arisa Komatsu*

## **Requirements Outline**
I need to design a program for the EV3 MINDSTORMS robot to allow it to identify and collect the yellow and red blocks back to the start zone using the colour sensor whilst navigating past other blocks using the ultrasonic sensor to detect obstacles and adjust its path automatically.
>### **Key Actions**
>1. Move forward until an obstacle is detected.
>2. Move back and turn 90° from obstacle if the obstacle is green or blue.
>3. Continue moving forward if an obstacle is red or yellow, then turn 180°.
>4. Robot moves forward in a set 'return' path corresponding to colour when red or yellow obstacle is 'captured'.
### **Functional Requirements (of key actions)**
>1. Obstacle Detection - Use Case

Scenario: The robot is navigating a path and encounters an obstacle.

Inputs: The ultrasonic sensor detects an object within 10 cm.

Action: The robot moves forward until an obstacle is detected.

Expected Outcome: The robot stops moving.

>2. Green/Blue Obstacle Evasion - Use Case

Scenario: The robot is has stopped moving after encountering an obstacle.

Inputs: The colour sensor detects the obstacle is green or blue.

Action: The robot moves backward, turns 90° from the obstacle, moves 15 cm, then turns 270° and continues moving forward until an obstacle is detected.

Expected Outcome: The robot avoids the green/blue blocks.

>3. Red/Yellow Obstacle Capture - Use Case

Scenario: The robot has stopped moving after encountering an obstacle.

Inputs: The colour sensor detects the obstacle is red or yellow.

Action: The robot moves forward until ultrasonic sensor detects the obstacle is within 0 cm, then turns 180° and continues moving forward until an obstacle is detected.

Expected Outcome: The robot captures the red/yellow obstacle in its 'arms'.

>4. Return Path after Capture - Use Case

Scenario: The robot has 'captured' a red or yellow obstacle (0 cm distance with obstacle).

Inputs: n/a (The colour sensor has already detected if the obstacle is either red or yellow)

Action: The robot moves forward until ultrasonic sensor detects the obstacle is within 0 cm, then turns 180° and continues moving forward until an obstacle is detected.

Expected Outcome: The robot captures the red/yellow obstacle in its 'arms'.
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
| 1. Obstacle Detection          | Ultrasonic sensor detects obstacle           | The robot stops moving.                  |
| 2. Green/Blue Obstacle Evasion          | Colour sensor detects obstacle is green/blue           | The robot avoids the green/blue obstacle.                  |
| 3. Red/Yellow Obstacle Capture          | Colour sensor detects obstacle is red/yellow          | The robot captures red/yellow obstacle in its 'arms'.                 | The robot captures red/yellow obstacle
| 4. Return Path after Capture | n/a |The robot moves (with red/yellow obstacle) back to start zone, stops and turns 180°.
### **Non-Functional Requirements**

- Efficiency - The robot should be able to complete the task within 2-3 minutes.

- Response Time - The robot should respond to sensor input(for both ultrasonic and colour sensor) within 1 second.

- Accuracy - The red and yellow blocks should be transported back to the start area  with all or most of its area within the box.

- Recognition - The robot should be able to identify when it needs to retrieve one more obstacle(red/yellow).



## **Design**
### **Pseudocode Development**
```
    BEGIN Main_Routine
        WHILE collected_obstacles < 2 THEN
            move forward
            IF ultrasonic_sensor < 15 cm THEN
                wait for 3 seconds
                IF colour_sensor = Color.RED THEN
                    RED_HomePath
                ELIF colour_sensor = Color.YELLOW THEN
                    YELLOW_HomePath
                ELSE 
                    move forward by -10 cm
                    turn(90)
                    move forward by 15 cm
                    turn(-90)
                END IF
            END IF
        END WHILE
        Display "Program Ended :3"
    END Main_Routine
```
```
    BEGIN RED_HomePath
        turn(180)
        collected_obstacles += 1
        pass
    END RED_HomePath
  
```
```
    BEGIN YELLOW_HomePath
        turn(180)
        collected_obstacles += 1
        pass
    END YELLOW_HomePath
```

### **Flowchart Development**
hamamamdmadmdmamdmamdmadm



## **Development and Integration**
hammydamdumdamdom



## **Testing and Debugging**
###  1. Obstacle Detection
```
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

# Write your program here.
ev3.speaker.beep()

while True:
    robot.drive(200, 0)

    if obstacle_sensor.distance() < 150:
        wait(3)
        robot.straight(-100)
        robot.turn(90)
        robot.straight(250)
        robot.turn(-90)

```
didnt detect quick enough and kept rotating and moving on the wall - it probably needs some tweaks for the sensor distance so its larger so it has time to detect
- i made the distance it moves while going sideways smaller because i feel like it might run off the map really easily if its too long

```
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
line_sensor = ColorSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Write your program here.
ev3.speaker.beep()

while True:
    robot.drive(200, 0)

    if obstacle_sensor.distance() > 300:
        wait(3)
        robot.straight(-100)
        robot.turn(90)
        robot.straight(150)
        robot.turn(-90)
```

###  2. Green/Blue Obstacle Evasion
```
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

# Write your program here.
ev3.speaker.beep()

while True:
    robot.drive(200, 0)

    if obstacle_sensor.distance() < 300:
        wait(3)
        if colour_sensor.color() == Color.BLUE:
           ev3.speaker.beep()
           ev3.speaker.beep()
           break
        elif colour_sensor.color() == Color.GREEN:
           ev3.speaker.beep()
           ev3.speaker.beep()
           ev3.speaker.beep()
           break
        else:
           ev3.speaker.beep()
           break
```
we're just playing around to see if it actually dtects the colour/finding a way to make it detect colour 
- so far it hasn't worked and it just goes to the else statement even when its blue or green
- i rsearched and i found that the distance between the object and the sensor should be pretty close so it can detect accurately so i think ill decrease the obstacle_sensor.distance to 150mm

```
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

# Write your program here.
ev3.speaker.beep()

while True:
    robot.drive(200, 0)

    if obstacle_sensor.distance() < 150:
        wait(3)
        if colour_sensor.color() == Color.BLUE:
           ev3.speaker.beep()
           ev3.speaker.beep()
           break
        elif colour_sensor.color() == Color.GREEN:
           ev3.speaker.beep()
           ev3.speaker.beep()
           ev3.speaker.beep()
           break
        else:
           ev3.speaker.beep()
           break
```
we changed it to 150 but it still goes to the else statement so its not a probably with the colour not being detected right its probably a problem with the if and elif statements. i think we'll do some more research on codes that make the colour sensor detect colour then we'll come back and fix

ITS STILL NOT WORKING
- we saw in some other codes that they say 'while colour_sensor.color() in ' so we'll switch the == with 'in'
- i also see that people say 'if color == Color.BLUE' with color = colour_sensor.color() so well try that  out

```
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

# Write your program here.
ev3.speaker.beep()

while True:
    colour = colour_sensor.color()
    robot.drive(200, 0)

    if obstacle_sensor.distance() < 300:
      wait(3)
      if colour == Color.BLUE:
         ev3.speaker.beep()
         ev3.speaker.beep()
         break
      elif colour == Color.GREEN:
         ev3.speaker.beep()
         ev3.speaker.beep()
         ev3.speaker.beep()
         break
      else:
         ev3.speaker.beep()
         break
```
it doesnt work :(
    i think our main issue is figuring out what is wrong with our code - well come back later when we understand what's wrong with out code and we have a better understanding of the colour sensor
## **Evaluation**
### **Peer Evaluation**
hamdamdamdydum
### **Individual Project Evaluation** _(in relation to peer evaluation)_
1. Achievement of functional and non-functional requirements
2. Final Performance
3. Project Management
4. Suggestions for future improvement 