import time
import pygame
import serial

# Initialize serial connection
try:
    ser = serial.Serial('/dev/pts/2', 9600, timeout=1)
    print(f"Connected to {ser.portstr}")
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    """Send command to the motor via serial."""
    try:
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")
    except Exception as e:
        print(f"Failed to send command: {e}")

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Set up joystick (assuming the Xbox controller is connected)
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Detected controller: {joystick.get_name()}")

screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("Motor Control")

running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Read joystick axes
        left_stick_y = -joystick.get_axis(1)  # Left stick Y-axis (up/down)
        left_stick_x = joystick.get_axis(0)    # Left stick X-axis (left/right)

        # Map joystick values to command
        forward_speed = int((left_stick_y + 1) * 63.5)  # Scale to 0-127
        turn_speed = int((left_stick_x + 1) * 63.5)     # Scale to 0-127

        # Send commands based on joystick input
        if forward_speed > 63:
            send_command(64 + forward_speed)  # Move forward
        elif forward_speed < 63:
            send_command(64 - (127 - forward_speed))  # Move backward
        else:
            send_command(64)  # Stop

        # Handling turning (left/right)
        if turn_speed > 63:
            send_command(192 + turn_speed)  # Turn right
        elif turn_speed < 63:
            send_command(192 - (127 - turn_speed))  # Turn left
        else:
            send_command(192)  # Stop turning

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
finally:
    send_command(64)  # Stop motors
    send_command(192)  # Stop turning
    ser.close()
    print("Serial connection closed.")
    pygame.quit()

