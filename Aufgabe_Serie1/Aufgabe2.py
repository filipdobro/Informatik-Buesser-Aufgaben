from simrobot import *

RobotContext.setStartPosition(320,480)
RobotContext.useBackground("sprites/bg.gif")

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)

fwd = 3000
turn = 500

gear.forward(fwd)
gear.left(turn)
gear.forward(fwd)
gear.right(turn)
gear.forward(fwd)
gear.right(turn)
gear.forward(fwd)
gear.left(turn)
gear.forward(fwd)

robot.exit()