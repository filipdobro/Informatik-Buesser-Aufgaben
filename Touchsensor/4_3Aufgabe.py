from simrobot import *
import time

#Context
RobotContext.useObstacle("sprites/channel.gif",250, 250)
RobotContext.setStartPosition(150, 250)
RobotContext.setStartDirection(0)

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
tsR = TouchSensor(SensorPort.S1)
tsL = TouchSensor(SensorPort.S2)
robot.addPart(tsR)
robot.addPart(tsL)

gear.forward()

turnTime = 550
backTime = 300
startTime = time.clock()

#program
while not robot.isEscapeHit():
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
   
robot.exit()