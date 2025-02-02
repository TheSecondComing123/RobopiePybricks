from boilerplate import *

robot = Robot()
robot.reset_lift_arm_port()
robot.forward(180)
robot.turn(20)
robot.forward(360 * 2)
robot.turn(-45)
robot.forward(50)
robot.turn(-10)
robot.forward(75)
robot.run_lift_arm(-360)
robot.reset_lift_arm_port()
