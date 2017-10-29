from ev3robot import *

#Constructor
robot = LegoRobot()
gear = Gear()
ts = TouchSensor(SensorPort.S1)
ls = LightSensor(SensorPort.S3)
ss = NxtSoundSensor(SensorPort.S2)
us = UltrasonicSensor(SensorPort.S4)
motor = Motor(MotorPort.C)

#addPart
robot.addPart(gear)
robot.addPart(ts)
robot.addPart(ls)
robot.addPart(ss)
robot.addPart(us)
robot.addPart(motor)

motor.setSpeed(100)

#Constants
valueBlack = 500
usDistance = 30
ssValue = 130

while not ts.isPressed():
    pass

dist=us.getDistance()
print dist
robot.drawString(str(dist),0,0)

while dist>15:
    dist=us.getDistance()
    print dist
    robot.drawString(str(dist), 0,0)
    
    lsValue = ls.getValue()
    if lsValue < 700:
        gear.leftArc(0.2)
        robot.drawString(str(lsValue), 0,1)
    else:
        gear.rightArc(0.2)
        robot.drawString(str(lsValue), 0,1)

gear.stop()

volume=ss.getValue()       
print volume
robot.drawString(str(volume),0,2)
while volume < 60:
    volume=ss.getValue()       
    print volume
    robot.drawString(str(volume),0,2)
    
motor.setSpeed(100)
motor.backward()
Tools.delay(1000)
gear.left()
robot.playTone(250,1000)


robot.exit()
    
