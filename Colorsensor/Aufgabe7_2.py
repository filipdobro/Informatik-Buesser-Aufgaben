from simrobot import *

RobotContext.useBackground("A7_2.png") 
RobotContext.setStartPosition(160, 210)
#RobotContext.setStartDirection(0)
robot = LegoRobot()
cs = ColorSensor(SensorPort.S3)
robot.addPart(cs)
gear = Gear()
robot.addPart(gear);
gear.setSpeed(30)

while not robot.isEscapeHit():
    color = cs.getColorStr()
    if color == "WHITE":
        gear.forward()
    elif color == "RED":
        while not robot.isEscapeHit():
            gear.backward(300)
            gear.left(850)
            break
    elif color == "GREEN":
        while not robot.isEscapeHit():
            gear.backward(300)
            gear.right(850)
            break
        
    elif color == "BLACK":
        gear.leftArc(0.01)
    
     
robot.exit()