from ev3robot import *

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(us)
gear.setSpeed(20)

while not robot.isEscapeHit():
    distance = us.getDistance()
    print distance
    
    gear.forward()

    if distance > 20:
        gear.forward()
    elif distance < 20:
        gear.backward()
    elif distance == 20:
        gear.stop()

    
robot.exit()