from simrobot import *

RobotContext.useBackground("sprites/bridge.gif")
RobotContext.useObstacle("sprites/bar2.gif", 250, 350)

#Constructors
robot = LegoRobot()
gear = Gear()
ss = SoundSensor(SensorPort.S1)
ls = LightSensor(SensorPort.S3)
ts = TouchSensor(SensorPort.S4)

#addPart
robot.addPart(gear)
robot.addPart(ss)
robot.addPart(ls)
robot.addPart(ts)

while not robot.isEscapeHit():
    if ss.getValue() > 75:
        print ss.getValue()
        gear.forward()
    if ts.isPressed():
        gear.forward()
    if ls.getValue() < 500:
        gear.backward()
        
    Tools.delay(100)
    
robot.exit()