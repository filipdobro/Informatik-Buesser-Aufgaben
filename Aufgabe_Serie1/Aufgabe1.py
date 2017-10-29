from ev3robot import *
#Intialisierung
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
#gear.setSpeed(50)

#Variablen
forwardInput = 1750
leftRightInput = 500

#Robot

gear.forward()
Tools.delay(forwardInput)
gear.left(leftRightInput)
gear.forward(forwardInput)
gear.right(leftRightInput)
gear.forward(forwardInput)
gear.right(leftRightInput)
gear.forward(forwardInput)
gear.left(leftRightInput)
gear.forward(750)

robot.exit()