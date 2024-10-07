import time
import pygame
import serial

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Adjust as needed
    print(f"Connected to {ser.portstr}")  # Confirm connection
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    try:
        # Ensure command is sent as a single byte
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")  # Show command in hex for clarity
    except Exception as e:
        print(f"Failed to send command: {e}")

# Initialize pygame for keyboard input
pygame.init()
screen = pygame.display.set_mode((100, 100))  # Create a window to capture events
pygame.display.set_caption("Motor Control")

# Main loop for keyboard input
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Move motors based on key presses
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:  # If 'W' is pressed
                send_command(64 + 43)  # Move motor 1 forward at medium speed
                send_command(192 + 43)  # Move motor 2 forward at medium speed
            elif keys[pygame.K_s]:  # If 'S' is pressed
                send_command(64 - 43)  # Move motor 1 backward at medium speed
                send_command(192 - 43)  # Move motor 2 backward at medium speed
            else:  # Stop motors if no key is pressed
                send_command(64)  # Stop motor 1
                send_command(192)  # Stop motor 2

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
