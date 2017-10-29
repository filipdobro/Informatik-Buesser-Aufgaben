#Wiederholte Bewegungen for-Schleife Quadrat

#libraryimport
from ev3robot import *

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)

for n in range(4):
    gear.forward(1000)
    gear.right(550)

robot.exit()
