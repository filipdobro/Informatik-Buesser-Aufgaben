from simrobot import *

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)

for n in range(4):
    gear.forward(2000)
    gear.right(1075)
    gear.forward(2000)
    gear.right(525)

robot.exit()
