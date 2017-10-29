from simrobot import *
import time

RobotContext.setStartPosition(0,250)
RobotContext.setStartDirection(0)
RobotContext.useBackground("sprites/panels.gif")

count = 0
robot = LegoRobot()
gear = Gear()
#lsR = LightSensor(SensorPort.S1)
lsL = LightSensor(SensorPort.S2)
robot.addPart(gear)
#robot.addPart(lsR)
robot.addPart(lsL)

gear.setSpeed(50)
gear.forward()

while not robot.isEscapeHit():
    #vR = lsR.getValue()
    vL = lsL.getValue()
    if vL < 500:
        count+=1
        print count
        while vL < 500:
            vL = lsL.getValue()
robot.exit()