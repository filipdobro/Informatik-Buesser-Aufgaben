#Grenzwert Licht berechnen

from ev3robot import *

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ls = LightSensor(SensorPort.S3)
robot.addPart(ls)

while not robot.isRightHit():
    white = ls.getValue()
    robot.drawString("White=>Right",0,0)
    robot.drawString(str(white),0,1)

while not robot.isLeftHit():
    black = ls.getValue()
    robot.drawString("Black=>Left",0,2)
    robot.drawString(str(black),0,3)
    
trigger=(white+black)/2
trigger = int(trigger)
robot.drawString(str(trigger),0,4)
Tools.delay(3000)
robot.exit()