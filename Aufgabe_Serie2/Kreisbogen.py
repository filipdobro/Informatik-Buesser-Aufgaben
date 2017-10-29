#Kreisbogen

from simrobot import *

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)

for n in range(4):
    gear.leftArc(0.1,1500)
    gear.rightArc(0.2,1050)

robot.exit()
