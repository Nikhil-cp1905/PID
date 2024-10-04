import time
import serial

class Sabertooth:
    def __init__(self, port='/dev/ttyUSB0', baud_rate=19200):
        self.ser = serial.Serial(port, baud_rate, timeout=1)
        print("Sabertooth 2x60 initialized for USB communication on port:", port)

    def send_command(self, command, data):
        """Sends a command to the Sabertooth via USB."""
        # Ensure command is an integer
        command = int(command)

        # Check if data is already in bytes, if not, convert it
        if isinstance(data, bytes):
            data_byte = data  # Data is already in bytes
        else:
            # Convert data to bytes; ensure it's treated as a single byte
            data = int(data)
            data_byte = data.to_bytes(1, byteorder='big')

        # Convert command to bytes
        command_byte = command.to_bytes(1, byteorder='big')  # 1 byte for command

        # Combine command and data into a single byte array
        message = command_byte + data_byte
        
        # Send the command
        self.ser.write(message)
        
        # Print debug information
        print(f"Sent Command: {command}, Data: {data} => Bytes Sent: {list(message)}")
        time.sleep(2)  # Delay of 2 seconds

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

    def close(self):
        """Close the serial connection."""
        self.ser.close()
        print("Serial connection closed.")

# Example usage
if __name__ == "__main__":
    sabertooth = Sabertooth(port='/dev/ttyUSB0', baud_rate=19200)

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

    # Close the serial connection
    sabertooth.close()
