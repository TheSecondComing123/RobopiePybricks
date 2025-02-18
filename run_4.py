from boilerplate import *

robot = Robot()

# Alignment: 2.5 to the right of left home base (jacob knows)
# Shark
robot.reset_lift_arm_port()
robot.forward(180, speed_mm_s=720)
robot.turn(40)
robot.forward(240)
robot.turn(-45)
robot.forward(50)
robot.turn(-40)
robot.forward(45)
robot.run_lift_arm(-360)
robot.reset_lift_arm_port()

# Coral 1
robot.forward(-100)
robot.turn(140)
robot.forward(-100)

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
robot.turn(-20)
robot.reset_lift_arm_port()
robot.reset_lift_arm_port()


# Scuba Diver
robot.forward(-90)
robot.turn(25)
robot.run_lift_arm(-100)
robot.forward(-270)
robot.turn(-160)
robot.run_lift_arm(-75)
robot.forward(40)
robot.run_lift_arm(300)

#Back to home base
robot.forward(-60)
robot.turn(100)
robot.forward(-450)
