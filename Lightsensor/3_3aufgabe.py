from simrobot import *

RobotContext.setStartPosition(150,400)
RobotContext.useBackground("sprites/oval.gif")

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
    if vL == 500 or vR == 500:
        vL += 1
        vR += 1
    elif vL < 500 and vR < 500:
        gear.leftArc(0.1)
    elif vL < 500 and vR > 500:
        gear.forward()
    elif vL > 500 and vR > 500:
        gear.rightArc(0.1)
    elif vL > 500 and vR < 500:
        gear.rightArc(0.1)
    
robot.exit()