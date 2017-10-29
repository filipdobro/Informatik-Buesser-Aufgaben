from ev3robot import *

def searchTarget():
    global left, right
    found = False
    step = 0
    while not robot.isEscapeHit():
        gear.right(50)
        step += 1
        dist = us.getDistance()
        
        if dist != -1:
            if not found:
                found = True
                left = step
            else:
                if found: 
                    right = step
                    break

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(us)
gear.left()
gear.setSpeed(20)

while not robot.isEscapeHit() and gear.isMoving():
    distance = us.getDistance()
    print "Distance = " + str(distance)
    if distance < 30:
        gear.stop()
        
    
robot.exit()