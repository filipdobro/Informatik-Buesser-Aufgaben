from ev3robot import *

def searchTarget():
    global right, left
    found = False
    count = 0
    
    while not robot.isEscapeHit():
        gear.right(50)
        count += 1
        dist = us.getDistance()
        
        if dist != -1:
            if not found:
                found = True
                left = count
            else:
                right = count
                break

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(us)
gear.setSpeed(20)



while not robot.isEscapeHit():
    distance = us.getDistance()
    print "Distance = " + str(distance)
    
    if distance != -1:
        gear.forward()
    
    

    
robot.exit()