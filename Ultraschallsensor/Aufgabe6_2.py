from ev3robot import *
found = False
def objectFound():
    global found
    while not robot.isEscapeHit():
        distance = us.getDistance()
        if distance < 50:
            found = True
        else:
            found = False
        
def searchTarget():
    global found
    gear.setSpeed(15)
    while not robot.isEscapeHit():
        distance = us.getDistance
        gear.left()
        if found == True:
            gear.setSpeed(100)
            gear.forward()
            if distance < 10:
                gear.forward(250)
                gear.left()
        elif found == False:
            gear.left()

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(us)
gear.setSpeed(20)
gear.left()

while not robot.isEscapeHit():
    distance = us.getDistance()
    print "Distance = " + str(distance)
    searchTarget()
    
robot.exit()