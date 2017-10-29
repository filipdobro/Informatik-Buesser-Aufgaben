from simrobot import *
import time

RobotContext.setStartPosition(150,400)
RobotContext.useBackground("sprites/bg_a4.gif")
RobotContext.setStartDirection(230)

robot = LegoRobot()
gear = Gear()
lsR = LightSensor(SensorPort.S1)
lsL = LightSensor(SensorPort.S2)
robot.addPart(gear)
robot.addPart(lsR)
robot.addPart(lsL)

gear.setSpeed(30)

while not robot.isEscapeHit():
    #Colors
    blue = 686
    green = 600
    yellow = 1000
    black = 3
    
    vR = lsR.getValue()
    vL = lsL.getValue()
    print vR
    
    if vL == blue and vR == blue:
        gear.rightArc(0.05)
    elif vL == green and vR == green:
        gear.leftArc(0.05)
    elif vL == yellow and vR == yellow:
        gear.forward()
    elif vL == blue and vR == yellow:
        gear.rightArc(0.25)
    elif vL == yellow and vR == green:
        gear.leftArc(0.25)
    elif vR == black:
        gear.stop()
        for n in range(200000):
            if n == 199999:
                gear.forward()
        
        
    
robot.exit()