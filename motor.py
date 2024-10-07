import serial
import time

class Sabertooth:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        # Open the serial port connected to FTDI232
        self.ser = serial.Serial(port, baudrate)
        self.ser.timeout = 1  # Set a timeout for serial communication
        print(f"Connected to Sabertooth via {port} at {baudrate} baudrate.")

    def send_command(self, command, data):
        """Send a command to the Sabertooth over serial and print the action."""
        # Convert command and data to bytes
        command_byte = command.to_bytes(1, byteorder='big')  # 1 byte for command
        data_byte = data.to_bytes(1, byteorder='big')        # 1 byte for data

        # Send the command and data bytes over serial
        self.ser.write(command_byte + data_byte)

        # Log and print what action is being performed
        if command == 0:
            print(f"Motor 1: Moving forward at speed {data} (byte: {command_byte + data_byte})")
        elif command == 1:
            print(f"Motor 1: Moving backward at speed {data} (byte: {command_byte + data_byte})")
        elif command == 4:
            print(f"Motor 2: Moving forward at speed {data} (byte: {command_byte + data_byte})")
        elif command == 5:
            print(f"Motor 2: Moving backward at speed {data} (byte: {command_byte + data_byte})")
        elif data == 0:
            print(f"Motor {1 if command in [0, 1] else 2}: Stopped (byte: {command_byte + data_byte})")

        # Simulate a delay for motor action
        time.sleep(2)

    def drive_motor1_forward(self, speed):
        self.send_command(0, speed)

    def drive_motor1_backward(self, speed):
        self.send_command(1, speed)

    def drive_motor2_forward(self, speed):
        self.send_command(4, speed)

    def drive_motor2_backward(self, speed):
        self.send_command(5, speed)

    def close(self):
        self.ser.close()  # Close the serial port when done
        print("Serial connection closed.")

# Example usage
if __name__ == "__main__":
    sabertooth = Sabertooth(port='/dev/ttyUSB0', baudrate=9600)  # Adjust port as necessary

    try:
        # Drive both motors forward at full speed for 2 seconds
        sabertooth.drive_motor1_forward(127)
        sabertooth.drive_motor2_forward(127)
        time.sleep(2)  # Wait for 2 seconds

        # Stop both motors
        sabertooth.drive_motor1_forward(0)
        sabertooth.drive_motor2_forward(0)
        time.sleep(1)  # Wait for a moment before reversing

        # Drive both motors backward at full speed for 2 seconds
        sabertooth.drive_motor1_backward(127)
        sabertooth.drive_motor2_backward(127)
        time.sleep(2)  # Wait for 2 seconds

        # Stop both motors
        sabertooth.drive_motor1_forward(0)
        sabertooth.drive_motor2_forward(0)

    except KeyboardInterrupt:
        print("Program interrupted.")

    finally:
        # Close the serial port
        sabertooth.close()
