from ev3robot import *

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)

ss = NxtSoundSensor(SensorPort.S2)
robot.addPart(ss)

Tools.delay(2000)

while not robot.isEscapeHit():
    loudness = ss.getValue()
    print loudness
    if loudness > 60:
        gear.forward()
    


robot.exit()