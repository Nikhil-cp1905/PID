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

# Initialize Pygame and joystick
pygame.init()
pygame.joystick.init()

# Set up joystick (assuming a PS4 controller is connected)
joystick = pygame.joystick.Joystick(0)
joystick.init()

screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("Motor Control")

running = True

# Initialize last command values
last_left_command = None
last_right_command = None

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get joystick axis positions (-1 to 1)
        axis_left_y = joystick.get_axis(1)  # Left joystick Y-axis (up/down)
        axis_right_x = joystick.get_axis(2)  # Right joystick X-axis (left/right)

        # Interpolate speed based on axis values
        speed_left = int(64 + axis_left_y * 63/100)  # Adjust speed with left joystick
        speed_right = int(192 + axis_right_x *63/100)  # Adjust speed with right joystick

        # Send commands only if they have changed
        if speed_left != last_left_command:
            send_command(speed_left)
            last_left_command = speed_left

        if speed_right != last_right_command:
            send_command(speed_right)
            last_right_command = speed_right

        # Delay for stability
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Keyboard interrupt detected.")

finally:
    send_command(64)  # Stop left motor
    send_command(192)  # Stop right motor
    ser.close()
    print("Serial connection closed.")
    pygame.quit()

