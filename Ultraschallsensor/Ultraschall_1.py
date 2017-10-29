from ev3robot import *

#mesh_hbar = [[200, 10], [-200, 10], [-200, -10], [200, -10]]
#RobotContext.useTarget("sprites/bar0.gif", mesh_hbar, 250, 100)

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
us = UltrasonicSensor(SensorPort.S4)
robot.addPart(us)
gear.setSpeed(25)
gear.forward()

while not robot.isEscapeHit():
    distance = us.getDistance()
    print distance
    

    if distance < 50:
        gear.backward(300)
        gear.left(200)
        gear.forward()
        
    
robot.exit()