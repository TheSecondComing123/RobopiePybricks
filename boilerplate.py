from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

__all__ = ["Robot"]

class Robot:
    MAX_ARM_DEGREES = 400

    def __init__(self):
        self.motors = {
            "left": Motor(Port.A, Direction.COUNTERCLOCKWISE),
            "right": Motor(Port.E),
            "lift_arm": Motor(Port.D),
            "razor_blade": Motor(Port.C)
        }
        
        self.drive_base = DriveBase(self.motors["left"], self.motors["right"], wheel_diameter=56, axle_track=112)
        self.speeds = {
            "straight_speed": 720,
            "straight_acceleration": 720,
            "turn_rate": 360,
            "turn_acceleration": 360
        }
        
        self.update_drive_settings()
        self.drive_base.use_gyro(True)
    
    def update_drive_settings(self):
        """Helper method to update the drive base settings."""
        self.drive_base.settings(self.speeds["straight_speed"],
                                 self.speeds["straight_acceleration"],
                                 self.speeds["turn_rate"],
                                 self.speeds["turn_acceleration"])
    
    def forward(self, distance_mm, speed_mm_s=None, wait=True):
        """Drive forward for a specified distance in millimeters."""
        if speed_mm_s is not None:
            self.speeds["straight_speed"] = speed_mm_s
            self.update_drive_settings()
        
        self.drive_base.straight(distance_mm, wait=wait)
    
    def turn(self, angle_deg, turn_rate_deg_s=None, wait=True):
        """Turn the robot by a specified angle in degrees."""
        if turn_rate_deg_s is not None:
            self.speeds["turn_rate"] = turn_rate_deg_s
            self.update_drive_settings()
        
        self.drive_base.turn(angle_deg, wait=wait)
    
    def drive_time(self, drive_speed_mm_s, turn_rate_deg_s, duration_ms):
        """Drive continuously at a given speed and turn rate for a specified duration."""
        self.drive_base.drive(drive_speed_mm_s, turn_rate_deg_s)
        wait(duration_ms)
        
        self.drive_base.stop()
    
    def move_motor(self, motor_name, rotation_deg, speed_dps=360, wait=True):
        """Rotate a specified motor by a given angle in degrees."""
        rotation_deg = max(min(rotation_deg, self.MAX_ARM_DEGREES), -self.MAX_ARM_DEGREES)
        self.motors[motor_name].run_angle(speed_dps, rotation_deg, then=Stop.HOLD, wait=wait)
    
    def reset_lift_arm_port(self):
        """Reset the lift arm motor to a known reference position."""
        self.motors["lift_arm"].run_angle(360, 300, then=Stop.HOLD, wait=True)
        wait(250)
    
    def stop(self):
        """Stop the drive base and all motors."""
        self.drive_base.stop()
        for motor in self.motors.values():
            motor.stop()
