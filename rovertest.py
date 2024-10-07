import time
import pygame
import serial

class Sabertooth:
    def __init__(self, serial_port):
        print("Sabertooth 2x60 initialized for virtual demo.")
        # Initialize pygame for controller input
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)  # Assuming the first joystick
        self.joystick.init()
        print(f"Detected controller: {self.joystick.get_name()}")

        # Initialize serial communication
        self.serial_connection = serial.Serial(serial_port, 9600, timeout=1)  # Open serial port
        print(f"Connected to FTDI232 on {serial_port}")

    def send_command(self, command, data):
        """Sends a command to the Sabertooth via the FTDI232."""
        # Convert command and data to binary format
        command_byte = command.to_bytes(1, byteorder='big')  # 1 byte for command
        data_byte = data.to_bytes(1, byteorder='big')        # 1 byte for data

        # Create the full message to send to the Sabertooth
        message = command_byte + data_byte

        # Print the byte data in hexadecimal format
        command_hex = command_byte.hex().upper()  # Convert to hex
        data_hex = data_byte.hex().upper()        # Convert to hex
        message_hex = message.hex().upper()        # Convert to hex

        try:
            self.serial_connection.write(message)  # Send command over serial
            print(f"Sending Command: {command} (0x{command_hex}), Data: {data} (0x{data_hex}) => sent via FTDI232 (Message: 0x{message_hex})")
        except Exception as e:
            print(f"Failed to send command: {e}")

        time.sleep(2)  # Delay of 2 seconds

    def read_controller_input(self):
        """Reads input from the Xbox controller."""
        pygame.event.pump()  # Update events

        # Reading joystick axes (Assuming 0 for left stick X, 1 for left stick Y, etc.)
        left_stick_y = -self.joystick.get_axis(1)  # Forward/Backward for motor 1
        right_stick_y = -self.joystick.get_axis(3)  # Forward/Backward for motor 2

        # Map axis values (-1.0 to 1.0) to speed (0 to 127)
        motor1_speed = int((left_stick_y + 1) * 63.5)  # Scale from -1 to 1 to 0 to 127
        motor2_speed = int((right_stick_y + 1) * 63.5)

        return motor1_speed, motor2_speed

    def control_loop(self):
        """Main control loop to read input and send commands."""
        while True:
            motor1_speed, motor2_speed = self.read_controller_input()

            # Control Motor 1
            if motor1_speed > 63:  # Forward movement
                self.send_command(0, motor1_speed)  # Drive forward motor 1
            elif motor1_speed < 63:  # Backward movement
                self.send_command(1, 127 - motor1_speed)  # Drive backward motor 1

            # Control Motor 2
            if motor2_speed > 63:  # Forward movement
                self.send_command(4, motor2_speed)  # Drive forward motor 2
            elif motor2_speed < 63:  # Backward movement
                self.send_command(5, 127 - motor2_speed)  # Drive backward motor 2

            time.sleep(0.1)  # Small delay to avoid overloading the system

# Example usage
if __name__ == "__main__":
    serial_port = '/dev/ttyUSB0'  # Replace with your FTDI232 port
    sabertooth = Sabertooth(serial_port)
    try:
        sabertooth.control_loop()
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        sabertooth.serial_connection.close()  # Close the serial connection on exit
