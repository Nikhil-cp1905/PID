import serial
import time
import pygame

# Initialize Pygame and the joystick
pygame.init()
pygame.joystick.init()

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Adjust the port as needed
    print(f"Connected to {ser.portstr}")  # Confirm connection
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    """Send a single byte command to the Sabertooth."""
    command_byte = bytes([command])
    ser.write(command_byte)
    print(f"Command sent: {command} (0x{command:02X})")  # Show command in hex for clarity

# Initialize joystick
try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick connected: {joystick.get_name()}")
except pygame.error as e:
    print(f"Joystick not found: {e}")
    exit(1)

# Main control loop
try:
    while True:
        # Process Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt

        # Get joystick axes (left stick vertical)
        y_axis = joystick.get_axis(1)  # Axis 1 is typically the Y axis for the left stick

        # Control motors based on joystick input
        if y_axis < -0.1:  # Forward
            send_command(64 + 43)  # Move motor 1 forward
            send_command(192 + 43)  # Move motor 2 forward
        elif y_axis > 0.1:  # Backward
            send_command(64 - 43)  # Move motor 1 backward
            send_command(192 - 43)  # Move motor 2 backward
        else:  # Stop
            send_command(64)  # Stop motor 1
            send_command(192)  # Stop motor 2

        time.sleep(0.1)  # Limit loop speed

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Stop motors
    send_command(64)  # Stop motor 1
    send_command(192)  # Stop motor 2

    # Close the serial connection
    ser.close()
    print("Serial connection closed.")
