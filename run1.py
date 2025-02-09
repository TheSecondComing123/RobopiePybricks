from boilerplate import *

robot = Robot()

robot.reset_lift_arm_port()
robot.forward(169)
robot.turn(100)
robot.forward(-320)

robot.forward(70)
robot.turn(-45)
robot.run_lift_arm(-450)
robot.forward(70)
robot.run_lift_arm(360, speed_dps=180, wait=False)
robot.turn(90, turn_rate_deg_s=180)
robot.forward(300)
