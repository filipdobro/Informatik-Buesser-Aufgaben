from simrobot import *

RobotContext.setStartPosition(250,250)
RobotContext.setStartDirection(0)
RobotContext.useBackground("sprites/blacktapes.gif")

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
        gear.left(1075)
    else:
        gear.forward()
robot.exit()