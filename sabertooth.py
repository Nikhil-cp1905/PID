import serial
import time

class SabertoothController:
    def __init__(self, port, baudrate=9600):
        # Initialize serial connection to Sabertooth via FTDI232
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Give time for the serial connection to initialize

    def send_command(self, command):
        """Send a byte command to Sabertooth controller."""
        self.ser.write(command)
        time.sleep(0.1)  # Allow time for Sabertooth to process the command

    def move_motor(self, speed):
        """
        Control the motor speed.
        Speed values:
        - 0 to 127: Reverse
        - 128 to 255: Forward
        """
        if 0 <= speed <= 255:
            command = bytes([speed])
            self.send_command(command)
        else:
            print("Speed value must be between 0 and 255")

    def stop_motor(self):
        """Send a stop command to the motor."""
        self.move_motor(0)  # Stop motor (simplified serial)

    def close(self):
        """Close the serial connection when done."""
        self.ser.close()


def main():
    # Replace '/dev/ttyUSB0' with the correct serial port for your FTDI232
    sabertooth = SabertoothController('/dev/ttyUSB0')

    try:
        # Move the motor forward
        print("Moving motor forward...")
        sabertooth.move_motor(200)  # Send speed command to move forward
        time.sleep(2)  # Move for 2 seconds

        # Stop the motor
        print("Stopping motor...")
        sabertooth.stop_motor()
        time.sleep(1)  # Pause before reversing

        # Move the motor backward
        print("Moving motor backward...")
        sabertooth.move_motor(50)  # Send speed command to move backward
        time.sleep(2)  # Move for 2 seconds

        # Stop the motor
        print("Stopping motor...")
        sabertooth.stop_motor()

    finally:
        # Ensure the serial connection is closed after the operation
        sabertooth.close()

if __name__ == "__main__":
    main()

