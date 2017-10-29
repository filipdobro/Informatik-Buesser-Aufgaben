from simrobot import *

RobotContext.setStartPosition(250,250)
RobotContext.setStartDirection(-90)
RobotContext.useBackground("sprites/track.gif")

robot = LegoRobot()
gear = Gear()
lsR = LightSensor(SensorPort.S1)
lsL = LightSensor(SensorPort.S2)
robot.addPart(gear)
robot.addPart(lsR)
robot.addPart(lsL)

gear.setSpeed(20)
gear.forward()

while not robot.isEscapeHit():
    vR = lsR.getValue()
    vL = lsL.getValue()
    if vR < 500 and vL < 500:
        gear.forward()
    elif vR < 500 and vL > 500:
        gear.rightArc(0.1)
    elif vR > 500 and vL < 500:
        gear.leftArc(0.1)
    elif vR > 500 and vL > 500:
        gear.backward()
    Tools.delay(100)
robot.exit()