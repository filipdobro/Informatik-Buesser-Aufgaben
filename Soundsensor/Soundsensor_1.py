from ev3robot import *


robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ss = NxtSoundSensor(SensorPort.S2)
robot.addPart(ss)

while not robot.isEscapeHit() and gear.isMoving():
    distance = us.getDistance()
    print "Distance = " + str(distance)
    if distance < 30:
        gear.stop()
        
    
robot.exit()