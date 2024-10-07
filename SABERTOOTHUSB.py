import time
import serial

class Sabertooth:
    def __init__(self, port='/dev/ttyUSB0', baud_rate=19200):
        # Initialize the serial connection using FTDI232 (connected as /dev/ttyUSB0 in Linux)
        self.ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Sabertooth 2x60 initialized for USB communication on port: {port}, baud_rate: {baud_rate}")

    def send_command(self, command, data):
        """Sends a command to the Sabertooth motor driver using FTDI232 USB-to-Serial."""
        # Convert command and data to bytes
        command_byte = command.to_bytes(1, byteorder='big')  # 1 byte for command
        data_byte = data.to_bytes(1, byteorder='big')        # 1 byte for data
        
        # Combine command and data into a single message
        message = command_byte + data_byte
        
        # Send the combined message through the serial port
        self.ser.write(message)
        
        # Debugging output for sent data
        print(f"Sent Command: {command} => {list(message)}")

        # Delay to simulate communication timing
        time.sleep(2)

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

    def close(self):
        """Closes the serial connection."""
        self.ser.close()
        print("Serial connection closed.")

# Example usage
if __name__ == "__main__":
    # Initialize Sabertooth controller through FTDI232 (usually ttyUSB0)
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

