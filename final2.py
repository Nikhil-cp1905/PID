import time
import serial

class Sabertooth:
    def __init__(self, port='/dev/ttyUSB0', baud_rate=19200):
        self.ser = serial.Serial(port, baud_rate, timeout=1)
        print("Sabertooth 2x60 initialized for USB communication on port:", port)

    def send_command(self, command, data):
        """Sends a command to the Sabertooth via USB."""
        # Convert command and data to bytes
        command_byte = command.to_bytes(1, byteorder='big')  # 1 byte for command
        data_byte = data.to_bytes(1, byteorder='big')        # 1 byte for data

        # Combine command and data into a single byte array
        message = command_byte + data_byte
        
        # Send the command
        self.ser.write(message)
        
        # Print debug information
        print(f"Sent Command: {command}, Data: {data} => Bytes Sent: {message}")
        print(f"Command Byte: {command_byte}, Data Byte: {data_byte}, Combined Message Bytes: {message}")
        time.sleep(2)  # Delay of 2 seconds for sending command

    def drive_motor1_forward(self, speed):
        self.send_command(0, speed)

    def drive_motor1_backward(self, speed):
        self.send_command(1, speed)

    def stop_motor1(self):
        self.send_command(0, 0)  # Stop Motor 1

    def close(self):
        """Close the serial connection."""
        self.ser.close()
        print("Serial connection closed.")

# Example usage
if __name__ == "__main__":
    sabertooth = Sabertooth(port='/dev/ttyUSB0', baud_rate=19200)

    try:
        # Drive motor 1 forward at full speed for 2 seconds
        sabertooth.drive_motor1_forward(127)
        time.sleep(2)  # Wait for 2 seconds

        # Stop motor 1
        sabertooth.stop_motor1()
        time.sleep(1)  # Wait for 1 second

        # Drive motor 1 backward at full speed for 2 seconds
        sabertooth.drive_motor1_backward(127)
        time.sleep(2)  # Wait for 2 seconds

        # Stop motor 1 completely
        sabertooth.stop_motor1()

    except KeyboardInterrupt:
        print("Program interrupted.")

    finally:
        # Close the serial connection
        sabertooth.close()
