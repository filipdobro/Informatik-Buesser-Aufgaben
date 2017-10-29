from ev3robot import *

RobotContext.useObstacle("sprites/field1.gif",250, 250)
RobotContext.setStartPosition(350, 350)

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ts = TouchSensor(SensorPort.S1)
robot.addPart(ts)

count = 0
turnTime = 500


while not robot.isEscapeHit():
    gear.forward()
    if ts.isPressed():
        count += 1
        gear.backward(500)
        if count % 2 == 0:
            gear.right(turnTime)
            gear.forward(turnTime)
            gear.right(turnTime)
        elif count % 2 != 0:
            gear.left(turnTime)
            gear.forward(turnTime)
            gear.left(turnTime)

robot.exit()