import serial
import time
import pygame

# Initialize Pygame and the joystick module
pygame.init()
pygame.joystick.init()

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/pts/3', 9600, timeout=1)  # Adjust as needed
    print(f"Connected to {ser.portstr}")  # Confirm connection
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    """Send a command to the motor driver."""
    try:
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")
    except Exception as e:
        print(f"Failed to send command: {e}")

def control_motors():
    """Control the motors using a game controller."""
    print("Control the motors using the game controller:")
    print("Press the corresponding buttons to control direction.")

    # Check if a joystick is connected
    if pygame.joystick.get_count() < 1:
        print("No joystick detected.")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                
                # Get the state of the joystick axes/buttons
                axis_x = joystick.get_axis(0)  # Left stick horizontal
                axis_y = joystick.get_axis(1)  # Left stick vertical

                if axis_y < -0.5:  # Forward
                    send_command(64 + 43)  # Motor 1 forward
                    send_command(192 + 43)  # Motor 2 forward
                elif axis_y > 0.5:  # Backward
                    send_command(64 - 43)  # Motor 1 backward
                    send_command(192 - 43)  # Motor 2 backward
                else:
                    send_command(64)  # Stop motor 1
                    send_command(192)  # Stop motor 2
                
                if axis_x < -0.5:  # Left
                    send_command(128)  # Example command for left
                elif axis_x > 0.5:  # Right
                    send_command(255)  # Example command for right

            time.sleep(0.1)  # Short delay to reduce CPU usage

    except KeyboardInterrupt:
        print("Program interrupted.")

    # Stop all motors on exit
    send_command(64)  # Stop motor 1
    send_command(192)  # Stop motor 2

# Start controlling the motors
control_motors()

# Close the serial connection
ser.close()
print("Serial connection closed.")

