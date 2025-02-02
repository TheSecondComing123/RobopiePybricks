from boilerplate import *

robot = Robot()

# Alignment: 2
# Shark
robot.reset_lift_arm_port()
robot.forward(180, speed_mm_s=720)
robot.turn(40)
robot.forward(240)
robot.turn(-45)
robot.forward(60)
robot.turn(-40)
robot.forward(45)
robot.run_lift_arm(-360)
robot.reset_lift_arm_port()

# Coral
robot.forward(-90)
robot.turn(140)
robot.forward(-90)

# Coral
robot.forward(30)
robot.turn(-90)
robot.forward(120)
robot.turn(35)
robot.forward(-25)
robot.run_lift_arm(-360)
robot.reset_lift_arm_port()

# Anglerfish
robot.turn(-45)
robot.forward(-90)
robot.turn(80)
robot.forward(350)
robot.run_lift_arm(-360)
robot.turn(180)

# Back to home base left
robot.forward(270)
robot.turn(-40)
robot.forward(360 * 1.25)
