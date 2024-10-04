class Sabertooth:
    def __init__(self):
        print("Sabertooth 2x60 initialized for virtual demo.")

    def send_command(self, command, data):
        """Simulates sending a command to the Sabertooth with specified data."""
        print(f"Sending Command: {command}, Data: {data}")

    def drive_motor1_forward(self, speed):
        """Drive motor 1 forward at specified speed (0-127)."""
        self.send_command(0, speed)

    def drive_motor1_backward(self, speed):
        """Drive motor 1 backward at specified speed (0-127)."""
        self.send_command(1, speed)

    def set_min_voltage(self, volts):
        """Set the minimum voltage. Converts volts to command data."""
        value = int((volts - 6) * 5)
        self.send_command(2, value)

    def set_max_voltage(self, volts):
        """Set the maximum voltage. Converts volts to command data."""
        value = int(volts * 5.12)
        self.send_command(3, value)

    def drive_motor2_forward(self, speed):
        """Drive motor 2 forward at specified speed (0-127)."""
        self.send_command(4, speed)

    def drive_motor2_backward(self, speed):
        """Drive motor 2 backward at specified speed (0-127)."""
        self.send_command(5, speed)

    def drive_motor1_7bit(self, command):
        """Drive motor 1 using 7-bit commands (0-127)."""
        self.send_command(6, command)

    def drive_motor2_7bit(self, command):
        """Drive motor 2 using 7-bit commands (0-127)."""
        self.send_command(7, command)

    def drive_forward_mixed(self, speed):
        """Drive vehicle forward in mixed mode."""
        self.send_command(8, speed)

    def drive_backward_mixed(self, speed):
        """Drive vehicle backward in mixed mode."""
        self.send_command(9, speed)

    def turn_right_mixed(self, speed):
        """Turn vehicle right in mixed mode."""
        self.send_command(10, speed)

    def turn_left_mixed(self, speed):
        """Turn vehicle left in mixed mode."""
        self.send_command(11, speed)

    def drive_forward_back_7bit(self, command):
        """Drive forwards/backwards using 7-bit commands."""
        self.send_command(12, command)

    def turn_7bit(self, command):
        """Turn using 7-bit commands."""
        self.send_command(13, command)

    def set_serial_timeout(self, timeout):
        """Set the serial timeout in units of 100ms."""
        self.send_command(14, timeout)

    def set_baud_rate(self, rate):
        """Set the baud rate (1-5 corresponds to various rates)."""
        self.send_command(15, rate)

    def set_ramping(self, value):
        """Adjust or disable the ramping feature."""
        self.send_command(16, value)

    def set_deadband(self, value):
        """Set the deadband range."""
        self.send_command(17, value)

# Example usage
if __name__ == "__main__":
    sabertooth = Sabertooth()

    # Drive motor 1 forward at full speed
    sabertooth.drive_motor1_forward(127)

    # Drive motor 1 backward at half speed
    sabertooth.drive_motor1_backward(64)

    # Set minimum voltage to 7.0 volts
    sabertooth.set_min_voltage(7.0)

    # Set maximum voltage to 12.0 volts
    sabertooth.set_max_voltage(12.0)

    # Drive motor 2 forward at full speed
    sabertooth.drive_motor2_forward(127)

    # Stop motor 2
    sabertooth.drive_motor2_forward(0)

    # Set serial timeout to 10 (1000ms)
    sabertooth.set_serial_timeout(10)

    # Set baud rate to 3 (19200 baud)
    sabertooth.set_baud_rate(3)

    # Set ramping to fast ramp (1)
    sabertooth.set_ramping(1)

    # Set deadband to 3
    sabertooth.set_deadband(3)
