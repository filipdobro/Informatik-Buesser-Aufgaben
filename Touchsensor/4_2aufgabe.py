from simrobot import *

#Context
RobotContext.useObstacle("sprites/cleaner.gif",250, 250)  

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

#program
while not robot.isEscapeHit():
    gear.forward()
    if tsR.isPressed() and tsL.isPressed():
        gear.backward(backTime)
        gear.left(turnTime)
    elif tsR.isPressed():
        gear.backward(backTime)
        gear.left(turnTime)
    elif tsL.isPressed():
        gear.backward(backTime)
        gear.right(turnTime)
   
robot.exit()