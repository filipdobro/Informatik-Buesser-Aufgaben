from simrobot import *

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
gear.setSpeed(100)
#robot
for n in range(3):
    gear.rightArc(0.2,2750)
    gear.right(550)

robot.exit()
