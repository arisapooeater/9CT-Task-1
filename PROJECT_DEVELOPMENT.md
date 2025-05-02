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
        collected_obstacles = 0
        Autodrive
        Display "Program Ended :3"
    END Main_Routine
```
```
    BEGIN Autodrive
        WHILE collected_obstacles < 2 THEN
            move forwar
            IF ultrasonic_sensor < 15 cm THEN
                wait for 3 seconds
                Obstacle_Functions
            END IF
        END WHILE
    END Autodrive
```
```
    BEGIN Obstacle_Functions
        IF colour_sensor = Color.RED THEN
            turn 180°
            move forward by 20 cm
            turn 90°
            move forward by 55 cm
            turn 90°
            move forward by 20 cm
            move backward by 10 cm
            collected_obstacles += 1
        ELIF colour_sensor = Color.YELLOW THEN
            turn 180°
            move forward by 40 cm
            turn -90°
            move forward by 20 cm
            collected_obstacles += 1
            move backward by 20 cm
            turn 90°
            move forward by 55 cm
            turn -90°
        ELSE 
            move forward by -10 cm
            turn 90°
            move forward by 15 cm
            turn -90°
        END IF
    END Obstacle_Functions
  
```
**Note -**
 I  made the program so it uses the ultrasonic sensor to detect and avoid an obstacle, bring the yellow obstacle back to the start zone and move deliberately adjacent to the red obstacle before it goes to the start of the while loop so it can autodrive directly towards it.

### **Flowchart Development**
![Flowchart](./image/flowcharts.png "Flowcharts")

## **Development and Integration**
hammydamdumdamdom



## **Testing and Debugging**
###  1. Obstacle Detection
| Input | Process | Output|
|---------- |---------- |----------------   |
| Ultrasonic sensor detects obstacle within 15 cm distance | The robot stops, reverses | The robot avoids the obstacle

```
# TEST 1
# Play a beep sound to signal the program has started
ev3.speaker.beep()

# The robot drives continuously unless an obstacle is detected to be within 15 cm
while True:
    robot.drive(200, 0)
    
# If an obstacle is detected within 15 cm, the robot waits 3 seconds, goes back 10 cm, turns to the right, drives 25 cm then turns back to the left to begin driving continuously again.
    if obstacle_sensor.distance() < 150: 
        wait(3)
        robot.straight(-100)
        robot.turn(90)
        robot.straight(250)
        robot.turn(-90)

```
The robot didn't detect the wall fast enough and started rotating and moving on the wall. I think I need to probably make the "obstacle_sensor.distance()" larger so the robot can detect obstacles quickly without bumping into them.

**Working Towards:**
- Making the "obstacle_sensor.distance()" larger so the robot can detect obstacles more quickly
- Changing the "while True" later to "while collected_obstacles < 2" later when I start combining all the test cases.

```
# TEST 2
# Play a beep sound to signal the program has started
ev3.speaker.beep()

# The robot drives continuously unless there's a break in the loop
while True:
    robot.drive(200, 0)

# If an obstacle is detected within 30 cm, the robot waits 3 seconds, goes back 10 cm, turns to the right, drives 15 cm then turns back to the left to begin driving continuously again.
    if obstacle_sensor.distance() > 300:
        wait(3)
        robot.straight(-100)
        robot.turn(90)
        robot.straight(150)
        robot.turn(-90)
```

###  2. Green/Blue Obstacle Evasion
| Input | Process | Output|
|---------- |---------- |----------------   |
| Ultrasonic sensor detects obstacle within 15 cm distance + Colour sensor detects the obstacle is green or blue | Robot reverses, moves sideways, then returns to original path | Robot evades green and blue obstacles
```
# TEST 1
# Play a beep sound to signal the program has started
ev3.speaker.beep()

# The robot drives continuously unless there's a break in the loop
while True:
    robot.drive(200, 0)

    # If an obstacle is detected within 30 cm, wait 3 seconds
    if obstacle_sensor.distance() < 300:
        wait(3)
        # If the colour sensor detects blue, beep twice then break the while loop
        if colour_sensor.color() == Color.BLUE:
           ev3.speaker.beep()
           ev3.speaker.beep()
           break
        # If the colour sensor detects green, beep twice then break the while loop
        elif colour_sensor.color() == Color.GREEN:
           ev3.speaker.beep()
           ev3.speaker.beep()
           ev3.speaker.beep()
           break
        else:
           ev3.speaker.beep()
           break
```
I want to begin this test case by first figuring out how to use the colour sensor to make it detect the green and blue obstacles. We tested the code but it goes straight to the else statement, so the issue is probably in how I wrote "colour_sensor.color() == Color.X". 

I did some research and found that the distance and sensor should be pretty close for accurate colour detection so I'll decrease the "obstacle_sensor.distance" as well.

**Working Towards:**
- Figuring out how to make the colour sensor detect both green and blue
- Changing the code to fit my original program plan once I identify and fix the issue (with the colour sensor).

```
# TEST 2
# Play a beep sound to signal the program has started
ev3.speaker.beep()

# The robot drives continuously unless there's a break in the loop
while True:
    robot.drive(200, 0)

    # If an obstacle is detected within 15 cm, wait 3 seconds
    if obstacle_sensor.distance() < 150:
        wait(3)
        # If the colour sensor detects blue, beep twice then break the while loop
        if colour_sensor.color() == Color.BLUE:
           ev3.speaker.beep()
           ev3.speaker.beep()
           break
        # If the colour sensor detects green, beep three times then break the while loop
        elif colour_sensor.color() == Color.GREEN:
           ev3.speaker.beep()
           ev3.speaker.beep()
           ev3.speaker.beep()
           break
        else:
           ev3.speaker.beep()
           break
```
We changed the distance to 15 cm, but it still goes to the else statement when we have a green or blue obstacle, so I think its most likely a problem with how I wrote the if and elif statements. I think I'll do some more research on how to write codes that make the colour sensor detect colour then I'll come back and continue testing this out.

**Working Towards:**
- Researching out how to make the colour sensor detect both green and blue
- Changing the code to fit my original program plan once I identify and fix the issue (with the colour sensor).

```
# TEST 3
# Play a beep sound to signal the program has started
ev3.speaker.beep()

# The robot drives continuously unless there's a break in the loop
while True:
   colour = colour_sensor.color()
   robot.drive(200, 0)

    #if obstacle_sensor.distance() < 300:
      #wait(3)
    # If the colour sensor detects blue, beep twice then break the while loop
   if colour == Color.BLUE:
      ev3.speaker.beep()
      ev3.speaker.beep()
      break
    # If the colour sensor detects green, beep three times then break the while loop
   if colour == Color.GREEN:
      ev3.speaker.beep()
      ev3.speaker.beep()
      ev3.speaker.beep()
      break
   #else:
      #ev3.speaker.beep()
      #break
```
We receives some help from Mr Scott and the colour sensor works now! Contrary to my previous guesses, the problem wasn't entirely the our code's fault. By isolating just the code that detects the colour and working with that, he found that the colour sensor on our EV3 robot was on light detecting mode instead of colour, which is why our code wouldn't work. 

With his help, now we can start working on adapting this code into our program so the robot can evade blue and green obstacles.

**Working Towards:**
- Changing the code to fit my original program plan.
### 3. Red/Yellow Obstacle Capture
### 4. Return Path after Capture
(work on in class)
## **Evaluation**
### **Peer Evaluation**
hamdamdamdydum
### **Individual Project Evaluation** _(in relation to peer evaluation)_
1. Achievement of functional and non-functional requirements
2. Final Performance
3. Project Management
4. Suggestions for future improvement 