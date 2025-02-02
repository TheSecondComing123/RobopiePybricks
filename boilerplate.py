from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

__all__ = ["Robot"]

class Robot:
    MAX_ARM_DEGREES = 360

    def __init__(self):
        """
        Initialize the Robot with drive motors, an arm motor, and a razor blade motor.
        Uses standard FLL Spike hub and Spike Large wheels.
        """
        self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.E)
        self.lift_arm_motor = Motor(Port.D)
        self.razor_blade_motor = Motor(Port.C)
        self.drive_base = DriveBase(self.left_motor, self.right_motor,
                                    wheel_diameter=56, axle_track=112)
        self.straight_speed_mm_s = 720
        self.straight_acceleration_mm_s2 = 720
        self.turn_rate_deg_s = 360
        self.turn_acceleration_deg_s2 = 360
        self.drive_base.settings(self.straight_speed_mm_s,
                                 self.straight_acceleration_mm_s2,
                                 self.turn_rate_deg_s,
                                 self.turn_acceleration_deg_s2)
        self.drive_base.use_gyro(True)

    def forward(self, distance_mm, speed_mm_s=None, delay=0):
        """
        Drive forward for a specified distance in millimeters.
        Optionally update the straight-line speed.
        """
        if speed_mm_s is not None:
            self.straight_speed_mm_s = speed_mm_s
            self.drive_base.settings(self.straight_speed_mm_s,
                                     self.straight_acceleration_mm_s2,
                                     self.turn_rate_deg_s,
                                     self.turn_acceleration_deg_s2)
        self.drive_base.straight(distance_mm)
        wait(int(delay * 1000))

    def turn(self, angle_deg, turn_rate_deg_s=None, delay=0):
        """
        Turn the robot by a specified angle in degrees.
        Optionally update the turning rate.
        """
        if turn_rate_deg_s is not None:
            self.turn_rate_deg_s = turn_rate_deg_s
            self.drive_base.settings(self.straight_speed_mm_s,
                                     self.straight_acceleration_mm_s2,
                                     self.turn_rate_deg_s,
                                     self.turn_acceleration_deg_s2)
        self.drive_base.turn(angle_deg)
        wait(int(delay * 1000))

    def drive_time(self, drive_speed_mm_s, turn_rate_deg_s, duration_ms):
        """
        Drive continuously at a given speed and turn rate for a specified duration.
        """
        self.drive_base.drive(drive_speed_mm_s, turn_rate_deg_s)
        wait(duration_ms)
        self.drive_base.stop()

    def move_front_motor(self, rotation_deg, speed_dps=360):
        """
        Rotate the lift arm motor by a specified angle in degrees.
        """
        rotation_deg = max(min(rotation_deg, self.MAX_ARM_DEGREES),
                           -self.MAX_ARM_DEGREES)
        self.lift_arm_motor.run_angle(speed_dps, rotation_deg,
                                      then=Stop.HOLD, wait=True)
        wait(250)

    def move_back_motor(self, rotation_deg, speed_dps=360):
        """
        Rotate the razor blade motor by a specified angle in degrees.
        """
        rotation_deg = max(min(rotation_deg, self.MAX_ARM_DEGREES),
                           -self.MAX_ARM_DEGREES)
        self.razor_blade_motor.run_angle(speed_dps, rotation_deg,
                                         then=Stop.HOLD, wait=True)
        wait(250)

    def run_lift_arm(self, rotation_deg, speed_dps=1000):
        """
        Run the lift arm motor for a specified rotation in degrees.
        """
        rotation_deg = max(min(rotation_deg, self.MAX_ARM_DEGREES),
                           -self.MAX_ARM_DEGREES)
        self.lift_arm_motor.run_angle(speed_dps, rotation_deg,
                                      then=Stop.HOLD, wait=True)

    def reset_lift_arm_port(self):
        """
        Reset the lift arm motor to a known reference position.
        """
        self.lift_arm_motor.run_angle(360, 300,
                                      then=Stop.HOLD, wait=True)
        wait(250)

    def stop(self):
        """
        Stop the drive base and all motors.
        """
        self.drive_base.stop()
        self.left_motor.stop()
        self.right_motor.stop()
        self.lift_arm_motor.stop()
        self.razor_blade_motor.stop()

    def emergency_stop(self):
        """
        Immediately halt all robot motion.
        """
        self.stop()

    def log_status(self):
        """
        Return a dictionary with current status including drive base and motor angles.
        """
        status = {
            "drive_distance": self.drive_base.distance(),
            "drive_angle": self.drive_base.angle(),
            "left_motor_angle": self.left_motor.angle(),
            "right_motor_angle": self.right_motor.angle(),
            "lift_arm_angle": self.lift_arm_motor.angle(),
            "razor_blade_angle": self.razor_blade_motor.angle()
        }
        
        return status
