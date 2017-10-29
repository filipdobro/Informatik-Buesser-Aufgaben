from simrobot import *

#Context
RobotContext.useObstacle("sprites/racetrack.gif", 250, 250)
RobotContext.setStartPosition(420, 460)

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ts1 = TouchSensor(SensorPort.S1)
ts2 = TouchSensor(SensorPort.S2)

robot.addPart(ts1)
robot.addPart(ts2)
gear.forward()
#program
while not robot.isEscapeHit():
    if ts1.isPressed():
        gear.backward(250)
        gear.left(200)
        gear.forward()
    elif ts2.isPressed():
        gear.backward(250)
        gear.right(200)
        gear.forward()
            
robot.exit()