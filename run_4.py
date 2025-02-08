from boilerplate import *

robot = Robot()

# Alignment: 3
# Shark
robot.reset_lift_arm_port()
robot.forward(180, speed_mm_s=720)
robot.turn(40)
robot.forward(240)
robot.turn(-45)
robot.forward(57.5)
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


# Send the Submersible
robot.reset_lift_arm_port()
robot.forward(40)
robot.turn(180)
robot.forward(48)
robot.run_lift_arm(-360)
robot.turn(-18)
robot.reset_lift_arm_port()

# Back to home base left
robot.forward(-90)
robot.turn(25)
robot.forward(-270)
robot.turn(120)
robot.forward(360)
