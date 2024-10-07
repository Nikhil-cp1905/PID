import serial
import time
import pygame

# Initialize Pygame and the joystick module
pygame.init()
pygame.joystick.init()

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Adjust as needed
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
    """Control the motors using a game controller with variable speed."""
    print("Control the motors using the game controller:")
    print("Use the left stick to control motion and speed.")

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

                # Map joystick values to motor speed range (0-255 for example)
                speed_y = int((axis_y + 1) / 2 * 255)  # Maps -1..1 to 0..255
                speed_x = int((axis_x + 1) / 2 * 255)

                if axis_y < -0.1:  # Forward
                    send_command(64 + speed_y)  # Motor 1 forward (variable speed)
                    send_command(192 + speed_y)  # Motor 2 forward (variable speed)
                elif axis_y > 0.1:  # Backward
                    send_command(64 - speed_y)  # Motor 1 backward (variable speed)
                    send_command(192 - speed_y)  # Motor 2 backward (variable speed)
                else:
                    send_command(64)  # Stop motor 1
                    send_command(192)  # Stop motor 2
                
                if axis_x < -0.1:  # Left
                    send_command(128 - speed_x)  # Variable left turn
                elif axis_x > 0.1:  # Right
                    send_command(128 + speed_x)  # Variable right turn

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

