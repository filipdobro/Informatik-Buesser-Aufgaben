from simrobot import *
import random

def turn():
    gear.backward(100)
    turnTime = random.randrange(50,500)
    turnDirection=random.randrange(0,2)
    if turnDirection == 0:
        gear.left(turnTime)
    else:
        gear.right(turnTime)

#Context
RobotContext.useObstacle("cleaner.gif",250, 250)  

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ts = TouchSensor(SensorPort.S1)
robot.addPart(ts)


gear.forward()

turnTime = 550
backTime = 300

#program
while not robot.isEscapeHit():
    gear.forward()
    if ts.isPressed():
        turn()
   
robot.exit()