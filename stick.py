from boilerplate import *

# This does Sonar Discovery and takes the hoop out
robot = Robot()
robot.run_lift_arm(-360)
robot.forward(100)
robot.turn(-45)
robot.forward(100)
robot.turn(20)
robot.forward(200)
robot.turn(80)
robot.reset_lift_arm_port()
robot.forward(40, speed_mm_s=360)
robot.run_lift_arm(-360)
robot.forward(-100, speed_mm_s=360)

robot.reset_lift_arm_port()
robot.turn(-55)
robot.forward(125)
robot.turn(-17.5)
robot.forward(35)
robot.run_lift_arm(-360)
robot.forward(-500)
