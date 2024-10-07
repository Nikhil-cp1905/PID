import time
import pygame

class Sabertooth:
    def __init__(self):
        print("Sabertooth 2x60 initialized for virtual demo.")
        # Initialize pygame for controller input
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)  # Assuming the first joystick
        self.joystick.init()
        print(f"Detected controller: {self.joystick.get_name()}")

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
        elif command == 10:  # Turn right
            direction = "Turning right"
            movement = f"at speed {data} (binary data: {data_binary})"
        elif command == 11:  # Turn left
            direction = "Turning left"
            movement = f"at speed {data} (binary data: {data_binary})"
        
        # Print the byte representation of command and data
        print(f"Sending Command: {command} (binary: {command_binary}, byte: {command_byte}), "
              f"Data: {data} (binary: {data_binary}, byte: {data_byte}) => {direction} {movement}")
        time.sleep(0.2)  # Delay of 0.2 seconds for real-time control

    def read_controller_input(self):
        """Reads input from the Xbox controller."""
        pygame.event.pump()  # Update events

        # Reading joystick axes
        left_stick_y = -self.joystick.get_axis(1)  # Forward/Backward for both motors
        right_stick_x = self.joystick.get_axis(4)  # Left/Right turning

        # Map axis values (-1.0 to 1.0) to speed (0 to 127)
        forward_speed = int((left_stick_y + 1) * 63.5)  # Scale from -1 to 1 to 0 to 127
        turn_speed = int((right_stick_x + 1) * 63.5)    # Scale for turning

        return forward_speed, turn_speed

    def control_loop(self):
        """Main control loop to read input and send commands."""
        while True:
            forward_speed, turn_speed = self.read_controller_input()

            if forward_speed > 63:  # Forward movement
                self.send_command(0, forward_speed)  # Drive forward motor 1
                self.send_command(4, forward_speed)  # Drive forward motor 2
            elif forward_speed < 63:  # Backward movement
                self.send_command(1, 127 - forward_speed)  # Drive backward motor 1
                self.send_command(5, 127 - forward_speed)  # Drive backward motor 2

            if turn_speed > 63:  # Turn right
                self.send_command(10, turn_speed)  # Turn right
            elif turn_speed < 63:  # Turn left
                self.send_command(11, 127 - turn_speed)  # Turn left

            time.sleep(0.1)  # Small delay to avoid overloading the system

# Example usage
if __name__ == "__main__":
    sabertooth = Sabertooth()
    sabertooth.control_loop()
