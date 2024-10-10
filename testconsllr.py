import serial
import time
import pygame
import math

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/pts/3', 9600, timeout=1)
    print(f"Connected to {ser.portstr}")
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    """Send a command to the motor via serial."""
    try:
        # Ensure command is sent as a single byte
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X}")  
    except Exception as e:
        print(f"Failed to send command: {e}")

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick {joystick.get_name()} initialized")
else:
    print("No joystick connected!")
    exit()

def control_motors(left_y_axis, right_x_axis):
    """Control motors based on joystick input."""
    # Map left joystick for forward/backward movement
    left_speed = int((left_y_axis + 1) * 63.5)  # Scale to 0-127
    right_speed = int((left_y_axis + 1) * 63.5)  # Scale to 0-127

    # Adjust for right joystick turning
    if right_x_axis > 0.1:  # Right
        left_speed -= int(right_x_axis * 63.5)  # Reduce left motor speed
        right_speed += int(right_x_axis * 63.5)  # Increase right motor speed
    elif right_x_axis < -0.1:  # Left
        left_speed += int(-right_x_axis * 63.5)  # Increase left motor speed
        right_speed -= int(-right_x_axis * 63.5)  # Reduce right motor speed

    # Ensure speeds are within range
    left_speed = max(0, min(127, left_speed))
    right_speed = max(0, min(127, right_speed))

    # Send commands to motors
    send_command(64 + left_speed if left_speed >= 0 else 64 - abs(left_speed))  # Motor 1
    send_command(192 + right_speed if right_speed >= 0 else 192 - abs(right_speed))  # Motor 2

# Main loop to read joystick input
try:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get joystick axis values
        left_y_axis = joystick.get_axis(1)  # Left stick Y-axis (for forward/backward)
        right_x_axis = joystick.get_axis(0)  # Right stick X-axis (for turning)

        control_motors(left_y_axis, right_x_axis)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    send_command(64)  # Stop motor 1
    send_command(192)  # Stop motor 2
    ser.close()
    pygame.quit()

