from ev3robot import *

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
gear.setSpeed(100)

while not robot.isRightHit():
    pass

Tools.delay(2000)

while not robot.isEscapeHit():
    gear.forward()
    
robot.exit()