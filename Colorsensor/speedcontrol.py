from simrobot import *

RobotContext.useBackground("sprites/colortrack.png") 
RobotContext.setStartPosition(430, 410)
RobotContext.showStatusBar(30)
robot = LegoRobot()
cs = ColorSensor(SensorPort.S3)
robot.addPart(cs)
gear = Gear()
robot.addPart(gear);
gear.setSpeed(20)
isRed = False

while not robot.isEscapeHit():   
   color = cs.getColorStr()
   print color 
   robot.drawString(color, 0, 1)     
   if color == "BLACK":
      gear.setSpeed(50)
      gear.leftArc(0.1)
   elif color == "BLUE":
      gear.setSpeed(50)
      gear.rightArc(0.1)
   else:
      if color == "GREEN":
         gear.setSpeed(40);
         isRed = False
      elif color == "YELLOW":
         gear.setSpeed(30)
         isRed = False
      elif (color == "RED" and not isRed):
         gear.stop()
         isRed = True
         Tools.delay(250)
         gear.setSpeed(20)
      gear.forward()
robot.exit()