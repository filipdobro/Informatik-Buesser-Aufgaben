#Touchsensor

from simrobot import *
import time

#Context
RobotContext.useObstacle("sprites/bg.gif",250,250)
RobotContext.setStartPosition(310,470)

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ts = TouchSensor(SensorPort.S3)
robot.addPart(ts)

turnTime = 545          #Drehzeit 90°
startTime = time.clock()
#program
while not robot.isEscapeHit():
    gear.forward()
    if ts.isPressed():
        dT= time.clock() - startTime
        print dT
        if dT > 2:
            gear.backward(400)
            gear.left(turnTime)
        else:
            gear.backward(400)
            gear.right(turnTime*2)
        startTime = time.clock()
        
robot.exit()