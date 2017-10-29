#Touchsensor

from ev3robot import *
#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ts = TouchSensor(SensorPort.S1)
robot.addPart(ts)

#count
count = 0

#program

while not robot.isEscapeHit():
    if ts.isPressed():
        count +=1
        print count
        while ts.isPressed():
            pass
        
    
robot.exit()