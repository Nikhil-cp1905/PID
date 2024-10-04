import time
import serial

class HW417:
    def __init__(self, port='/dev/ttyUSB0', baud_rate=19200):
        self.ser = serial.Serial(port, baud_rate, timeout=1)
        print("HW-417 V1.2 initialized for USB communication on port:", port)

    def send_command(self, command):
        """Sends a command byte to the HW-417 via USB."""
        command_byte = command.to_bytes(1, byteorder='big')  # Convert command to byte
        self.ser.write(command_byte)  # Send the command
        print(f"Sent Command: {command} => Bytes Sent: {list(command_byte)}")
        time.sleep(0.5)  # Delay of 0.5 seconds

    def drive_motor1_forward(self, speed):
        # Command for driving motor 1 forward with speed value (0-255)
        command = (0x01, speed)  # Example command structure
        self.send_command(command[0])  # Send command byte
        self.send_command(command[1])  # Send speed byte

    def drive_motor1_backward(self, speed):
        # Command for driving motor 1 backward with speed value (0-255)
        command = (0x02, speed)  # Example command structure
        self.send_command(command[0])  # Send command byte
        self.send_command(command[1])  # Send speed byte

    def drive_motor2_forward(self, speed):
        # Command for driving motor 2 forward with speed value (0-255)
        command = (0x03, speed)  # Example command structure
        self.send_command(command[0])  # Send command byte
        self.send_command(command[1])  # Send speed byte

    def drive_motor2_backward(self, speed):
        # Command for driving motor 2 backward with speed value (0-255)
        command = (0x04, speed)  # Example command structure
        self.send_command(command[0])  # Send command byte
        self.send_command(command[1])  # Send speed byte

    def stop_motor1(self):
        self.send_command(0x05)  # Send stop command for motor 1

    def stop_motor2(self):
        self.send_command(0x06)  # Send stop command for motor 2

    def close(self):
        """Close the serial connection."""
        self.ser.close()
        print("Serial connection closed.")

# Example usage
if __name__ == "__main__":
    hw417 = HW417(port='/dev/ttyUSB0', baud_rate=19200)

    # Drive motor 1 forward at full speed
    hw417.drive_motor1_forward(255)

    # Drive motor 1 backward at half speed
    hw417.drive_motor1_backward(128)

    # Drive motor 2 forward at full speed
    hw417.drive_motor2_forward(255)

    # Stop motor 1
    hw417.stop_motor1()

    # Stop motor 2
    hw417.stop_motor2()

    # Close the serial connection
    hw417.close()

