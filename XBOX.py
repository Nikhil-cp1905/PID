import time
import pygame
import serial

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/pts/6', 9600, timeout=1)  # Adjust as needed
    print(f"Connected to {ser.portstr}")  # Confirm connection
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    """Send a command to the Sabertooth motor controller."""
    try:
        # Ensure command is sent as a single byte
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")  # Show command in hex for clarity
    except Exception as e:
        print(f"Failed to send command: {e}")

# Initialize pygame for joystick input
pygame.init()
pygame.joystick.init()

# Check for joystick connections
if pygame.joystick.get_count() < 1:
    print("No joystick found.")
    exit(1)

# Create a joystick object
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Using joystick: {joystick.get_name()}")

# Main loop for joystick input
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Read joystick axes
            left_y = joystick.get_axis(1)  # Left joystick Y-axis (-1 is up, +1 is down)
            left_x = joystick.get_axis(0)  # Left joystick X-axis

            # Map joystick input to motor speeds
            # Forward: Y < 0 (up), Backward: Y > 0 (down)
            motor_speed = int((-left_y + 1) * 63.5)  # Map from -1 to 1 to 0-127
            
            # Adjust speeds based on left_x for turning
            if left_x < -0.1:  # Turning left
                motor1_speed = motor_speed  # Motor 1 forward
                motor2_speed = int(motor_speed * -1)  # Motor 2 backward
            elif left_x > 0.1:  # Turning right
                motor1_speed = int(motor_speed * -1)  # Motor 1 backward
                motor2_speed = motor_speed  # Motor 2 forward
            else:  # Moving straight
                motor1_speed = motor_speed
                motor2_speed = motor_speed

            # Ensure the motor speeds are within acceptable range (0-127)
            motor1_speed = max(0, min(motor1_speed, 127))
            motor2_speed = max(0, min(motor2_speed, 127))

            # Send commands to motors
            send_command(motor1_speed)  # Command for motor 1
            send_command(motor2_speed)  # Command for motor 2

        time.sleep(0.1)  # Small delay to reduce CPU usage
except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
finally:
    # Stop motors and close the serial connection
    send_command(64)  # Stop motor 1
    send_command(192)  # Stop motor 2
    ser.close()
    print("Serial connection closed.")
    pygame.quit()
