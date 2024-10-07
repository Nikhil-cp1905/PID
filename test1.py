import time

class Sabertooth:
    def __init__(self):
        print("Sabertooth 2x60 initialized for virtual demo via FTDI232 USB-to-Serial converter.")

    def send_command(self, command, data):
        """Simulates sending a command to the Sabertooth with specified data."""
        direction = ""
        movement = ""

        # Convert command and data to binary format
        command_binary = format(command, '04b')  # 4-bit binary for command
        data_binary = format(data, '07b')        # 7-bit binary for data

        # Convert command and data to bytes
        command_byte = command.to_bytes(1, byteorder='big')  # 1 byte for command
        data_byte = data.to_bytes(1, byteorder='big')        # 1 byte for data

        if command == 0:  # Drive forward motor 1
            direction = "Motor 1 moving forward"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 1:  # Drive backward motor 1
            direction = "Motor 1 moving backward"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 4:  # Drive forward motor 2
            direction = "Motor 2 moving forward"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 5:  # Drive backward motor 2
            direction = "Motor 2 moving backward"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 2:  # Set min voltage
            direction = "Setting minimum voltage"
            movement = f"to {data * 0.2 + 6} volts (binary data: {data_binary})"
        elif command == 3:  # Set max voltage
            direction = "Setting maximum voltage"
            movement = f"to {data / 5.12} volts (binary data: {data_binary})"
        elif command == 14:  # Set serial timeout
            direction = "Setting serial timeout"
            movement = f"to {data * 100} ms (binary data: {data_binary})"
        elif command == 15:  # Set baud rate
            baud_rates = {1: 2400, 2: 9600, 3: 19200, 4: 38400, 5: 115200}
            direction = "Setting baud rate"
            movement = f"to {baud_rates.get(data, 'Invalid rate')} bps (binary data: {data_binary})"
        elif command == 16:  # Set ramping
            direction = "Setting ramping"
            movement = f"to {'fast' if data == 1 else 'medium' if data <= 10 else 'slow' if data <= 20 else 'off'} (binary data: {data_binary})"
        elif command == 17:  # Set deadband
            direction = "Setting deadband"
            movement = f"to {data} (binary data: {data_binary})"

        # Print the byte representation of command and data
        print(f"Sending Command: {command} (binary: {command_binary}, byte: {command_byte}), "
              f"Data: {data} (binary: {data_binary}, byte: {data_byte}) => {direction} {movement}")
        time.sleep(2)  # Delay of 2 seconds

    # Existing methods are unchanged
    def drive_motor1_forward(self, speed):
        self.send_command(0, speed)

    def drive_motor1_backward(self, speed):
        self.send_command(1, speed)

    def set_min_voltage(self, volts):
        value = int((volts - 6) * 5)
        self.send_command(2, value)

    def set_max_voltage(self, volts):
        value = int(volts * 5.12)
        self.send_command(3, value)

    def drive_motor2_forward(self, speed):
        self.send_command(4, speed)

    def drive_motor2_backward(self, speed):
        self.send_command(5, speed)

    def drive_motor1_7bit(self, command):
        self.send_command(6, command)

    def drive_motor2_7bit(self, command):
        self.send_command(7, command)

    def drive_forward_mixed(self, speed):
        self.send_command(8, speed)

    def drive_backward_mixed(self, speed):
        self.send_command(9, speed)

    def turn_right_mixed(self, speed):
        self.send_command(10, speed)

    def turn_left_mixed(self, speed):
        self.send_command(11, speed)

    def drive_forward_back_7bit(self, command):
        self.send_command(12, command)

    def turn_7bit(self, command):
        self.send_command(13, command)

    def set_serial_timeout(self, timeout):
        self.send_command(14, timeout)

    def set_baud_rate(self, rate):
        self.send_command(15, rate)

    def set_ramping(self, value):
        self.send_command(16, value)

    def set_deadband(self, value):
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
