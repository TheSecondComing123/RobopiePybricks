from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

class Robot:
    MAX_FORWARD_DEGREES = 10000
    MAX_TURN_DEGREES = 720
    MAX_ARM_DEGREES = 360

    def __init__(self):
        self.hub = PrimeHub()
        self.lift_arm_motor = Motor(Port.D)
        self.razor_blade_motor = Motor(Port.C)
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.E)

    def clamp(self, value, min_value, max_value):
        return max(min(value, max_value), min_value)

    def forward(self, degrees, speed=360, delay=0):
        degrees = self.clamp(degrees, -self.MAX_FORWARD_DEGREES, self.MAX_FORWARD_DEGREES)
        self.left_motor.run_angle(-speed, degrees, then=Stop.COAST, wait=False)
        self.right_motor.run_angle(speed, degrees, then=Stop.COAST, wait=True)
        wait(int((abs(degrees) / speed + delay - 1) * 1000))

    def turn(self, degrees, speed=360, delay=0):
        degrees = self.clamp(degrees * 2, -self.MAX_TURN_DEGREES, self.MAX_TURN_DEGREES)
        if degrees > 0:
            self.left_motor.run_angle(-speed, degrees, then=Stop.COAST, wait=False)
            self.right_motor.run_angle(speed, -degrees, then=Stop.COAST, wait=True)
        elif degrees < 0:
            self.left_motor.run_angle(speed, -degrees, then=Stop.COAST, wait=False)
            self.right_motor.run_angle(-speed, degrees, then=Stop.COAST, wait=True)
        wait(int((abs(degrees) / speed + delay - 1) * 1000))

    def move_front_motor(self, degrees, speed=360):
        degrees = self.clamp(degrees, -self.MAX_ARM_DEGREES, self.MAX_ARM_DEGREES)
        self.lift_arm_motor.run_angle(speed, degrees, then=Stop.HOLD, wait=True)
        wait(250)

    def move_back_motor(self, degrees, speed=360):
        degrees = self.clamp(degrees, -self.MAX_ARM_DEGREES, self.MAX_ARM_DEGREES)
        self.razor_blade_motor.run_angle(speed, degrees, then=Stop.HOLD, wait=True)
        wait(250)

    def run_lift_arm(self, degrees, speed=1000, delay=0):
        degrees = self.clamp(degrees, -self.MAX_ARM_DEGREES, self.MAX_ARM_DEGREES)
        self.lift_arm_motor.run_angle(speed, degrees, then=Stop.HOLD, wait=True)
        wait(int((abs(degrees) / speed + delay - 1) * 1000))

    def reset_lift_arm_port(self):
        self.lift_arm_motor.run_angle(360, 300, then=Stop.HOLD, wait=True)
        wait(250)

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
