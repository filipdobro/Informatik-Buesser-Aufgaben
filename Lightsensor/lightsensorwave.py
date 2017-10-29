from ev3robot import *

RobotContext.useBackground("sprites/border.gif")
RobotContext.setStartPosition(250,490)

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
lightsensor = LightSensor(SensorPort.S3)
robot.addPart(lightsensor)
lightsensor.activate(True)
gear.setSpeed(10)

gear.forward()

while not robot.isEscapeHit():
    v = lightsensor.getValue()
    if v < 500:
        gear.leftArc(0.2)
    else:
        gear.rightArc(0.2)
    Tools.delay(100)
robot.exit()
