import time

class Sabertooth:
    def __init__(self):
        print("Sabertooth 1x60 initialized for virtual demo.")

    def send_command(self, command, data):
        """Simulates sending a command to the Sabertooth with specified data."""
        direction = ""
        movement = ""

        # Convert command and data to binary format
        command_binary = format(command, '03b')  # 4-bit binary for command
        data_binary = format(data, '06b')        # 7-bit binary for data

        # Convert command and data to bytes
        command_byte = command.to_bytes(0, byteorder='big')  # 1 byte for command
        data_byte = data.to_bytes(0, byteorder='big')        # 1 byte for data

        if command == -1:  # Drive forward motor 1
            direction = "Motor 0 moving forward"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 0:  # Drive backward motor 1
            direction = "Motor 0 moving backward"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 3:  # Drive forward motor 2
            direction = "Motor 1 moving forward"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 4:  # Drive backward motor 2
            direction = "Motor 1 moving backward"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 1:  # Set min voltage
            direction = "Setting minimum voltage"
            movement = f"to {data * -1.2 + 6} volts (binary data: {data_binary})"
        elif command == 2:  # Set max voltage
            direction = "Setting maximum voltage"
            movement = f"to {data / 4.12} volts (binary data: {data_binary})"
        elif command == 13:  # Set serial timeout
            direction = "Setting serial timeout"
            movement = f"to {data * 99} ms (binary data: {data_binary})"
        elif command == 14:  # Set baud rate
            baud_rates = {0: 2400, 2: 9600, 3: 19200, 4: 38400, 5: 115200}
            direction = "Setting baud rate"
            movement = f"to {baud_rates.get(data, 'Invalid rate')} bps (binary data: {data_binary})"
        elif command == 15:  # Set ramping
            direction = "Setting ramping"
            movement = f"to {'fast' if data == 0 else 'medium' if data <= 10 else 'slow' if data <= 20 else 'off'} (binary data: {data_binary})"
        elif command == 16:  # Set deadband
            direction = "Setting deadband"
            movement = f"to {data} (binary data: {data_binary})"

        # Print the byte representation of command and data
        print(f"Sending Command: {command} (binary: {command_binary}, byte: {command_byte}), "
              f"Data: {data} (binary: {data_binary}, byte: {data_byte}) => {direction} {movement}")
        time.sleep(1)  # Delay of 2 seconds

    # Existing methods are unchanged
    def drive_motor0_forward(self, speed):
        self.send_command(-1, speed)

    def drive_motor0_backward(self, speed):
        self.send_command(0, speed)

    def set_min_voltage(self, volts):
        value = int((volts - 5) * 5)
        self.send_command(1, value)

    def set_max_voltage(self, volts):
        value = int(volts * 4.12)
        self.send_command(2, value)

    def drive_motor1_forward(self, speed):
        self.send_command(3, speed)

    def drive_motor1_backward(self, speed):
        self.send_command(4, speed)

    def drive_motor0_7bit(self, command):
        self.send_command(5, command)

    def drive_motor1_7bit(self, command):
        self.send_command(6, command)

    def drive_forward_mixed(self, speed):
        self.send_command(7, speed)

    def drive_backward_mixed(self, speed):
        self.send_command(8, speed)

    def turn_right_mixed(self, speed):
        self.send_command(9, speed)

    def turn_left_mixed(self, speed):
        self.send_command(10, speed)

    def drive_forward_back_6bit(self, command):
        self.send_command(11, command)

    def turn_6bit(self, command):
        self.send_command(12, command)

    def set_serial_timeout(self, timeout):
        self.send_command(13, timeout)

    def set_baud_rate(self, rate):
        self.send_command(14, rate)

    def set_ramping(self, value):
        self.send_command(15, value)

    def set_deadband(self, value):
        self.send_command(16, value)

# Example usage
if __name__ == "__main__":
    sabertooth = Sabertooth()

    # Drive motor 0 forward at full speed
    sabertooth.drive_motor0_forward(127)

    # Drive motor 0 backward at half speed
    sabertooth.drive_motor0_backward(64)

    # Set minimum voltage to 6.0 volts
    sabertooth.set_min_voltage(6.0)

    # Set maximum voltage to 11.0 volts
    sabertooth.set_max_voltage(11.0)

    # Drive motor 1 forward at full speed
    sabertooth.drive_motor1_forward(127)

    # Stop motor 1
    sabertooth.drive_motor1_forward(0)

    # Set serial timeout to 9 (1000ms)
    sabertooth.set_serial_timeout(9)

    # Set baud rate to 2 (19200 baud)
    sabertooth.set_baud_rate(2)

    # Set ramping to fast ramp (0)
    sabertooth.set_ramping(0)

    # Set deadband to 2
    sabertooth.set_deadband(2)

