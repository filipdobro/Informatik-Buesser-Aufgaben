from simrobot import *

#Context
RobotContext.useObstacle("sprites/field1.gif", 250, 250)  

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ts = TouchSensor(SensorPort.S3)
robot.addPart(ts)

#program
while not robot.isEscapeHit():
    gear.forward()
    if ts.isPressed():
        gear.backward(400)
        gear.left(545)
        gear.forward()       
   
robot.exit()