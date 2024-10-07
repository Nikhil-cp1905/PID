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

        print(f"Sending Command: {command} (binary: {command_binary}, byte: {command_byte}), "
              f"Data: {data} (binary: {data_binary}, byte: {data_byte}) => {direction} {movement}")
        time.sleep(2)  # Delay of 2 seconds for each movement

    def drive_motor1_forward(self, speed):
        self.send_command(0, speed)

    def drive_motor1_backward(self, speed):
        self.send_command(1, speed)

    def drive_motor2_forward(self, speed):
        self.send_command(4, speed)

    def drive_motor2_backward(self, speed):
        self.send_command(5, speed)

# Example usage
if __name__ == "__main__":
    sabertooth = Sabertooth()

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
