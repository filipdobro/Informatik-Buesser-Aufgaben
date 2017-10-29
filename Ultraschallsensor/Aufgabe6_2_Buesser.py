from ev3robot import *

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(us)
gear.left()

while not robot.isEscapeHit() and gear.isMoving():
    distance = us.getDistance()
    if distance > 50:
        gear.setSpeed(8)
        gear.left()
    else:
        gear.setSpeed(70)
        gear.forward()
        if distance < 10:
            gear.setSpeed(100)
            gear.left(2000)
    
robot.exit()