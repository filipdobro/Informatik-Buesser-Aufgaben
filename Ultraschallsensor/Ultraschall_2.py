from ev3robot import *

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(us)
gear.forward()

while not robot.isEscapeHit():
    distance = us.getDistance()
    print distance
    

    if distance < 40:
        gear.backward(500)
        gear.left(545)
        gear.forward()
        
    
robot.exit()