from simrobot import *

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
gear.setSpeed(100)

repeat:
    gear.leftArc(0.2,5000)
    gear.rightArc(0.2,5000)


while not robot.isEscapeHit():
    pass

robot.exit()
