#Kreisbogen

from simrobot import *

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)

gear.leftArc(0.1)

while not robot.isEscapeHit():
    pass

robot.exit()
