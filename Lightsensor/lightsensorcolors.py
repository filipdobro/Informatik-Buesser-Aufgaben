from ev3robot import *

RobotContext.useBackground("sprites/circle.gif")
RobotContext.setStartPosition(250,490)

#init
def onDark(port, level):
    gear.backward(1500)
    gear.left(550)
    gear.forward()

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
lightsensor = LightSensor(SensorPort.S3, dark = onDark)
robot.addPart(lightsensor)
lightsensor.activate(True)
gear.setSpeed(20)

while not robot.isEscapeHit():
    v = lightsensor.getValue()
    if v < 100:
        gear.forward()
    elif v < 500:
        gear.leftArc(0.2)
    elif v > 500:
        gear.rightArc(0.2)
    pass
robot.exit()
