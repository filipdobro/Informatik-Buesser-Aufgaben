from ev3robot import *

#init
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
gear.setSpeed(75)

while not robot.isEscapeHit():
    if robot.isUpHit():
        gear.forward()
    elif robot.isDownHit():
        gear.backward()
    elif robot.isLeftHit():
        gear.leftArc(0.2)
    elif robot.isRightHit():
        gear.rightArc(0.2)
    elif robot.isEnterHit():
        gear.stop()  
    
robot.exit()
