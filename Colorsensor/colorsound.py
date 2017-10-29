from ev3robot import *

robot = LegoRobot()

#redefine black color cube
ColorSensor.colorCubes[0]=[0,20,0,20,0,10]

#redefine blue color cube
ColorSensor.colorCubes[4]=[10,20,10,15,15,20]

#redefine green color cube
ColorSensor.colorCubes[2]=[35,40,45,53,10,17]

#redefine yellow color cube
ColorSensor.colorCubes[3]=[85,95,60,73,5,15]

#redefine red color cube
ColorSensor.colorCubes[4]=[40,100,5,25,5,25]

#redefine white color cube
ColorSensor.colorCubes[5]=[90,105,60,80,60,75]

#black[0],blue[1],green[2],yellow[3],red[4],white[5]

cs = ColorSensor(SensorPort.S3)
robot.addPart(cs)
gear=Gear()
robot.addPart(gear)
gear.setSpeed(5)

for i in range(6):
    print ColorSensor.colorCubes[i]

while not robot.isEscapeHit():
    color = cs.getColorStr()
    if color == "BLACK":
        robot.playTone(264,300)
        gear.backward()
    elif color == "BLUE":
        robot.playTone(297,300)
    elif color == "GREEN":
        robot.playTone(330,300)
    elif color == "YELLOW":
        robot.playTone(352,300)
    elif color == "RED":
        robot.playTone(396,300)
    elif color == "WHITE":
        robot.playTone(400,300)
        gear.forward()
    print color
    robot.drawString(color,0,0)
    
robot.exit()