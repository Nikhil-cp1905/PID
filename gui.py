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
    """Send a command to the Sabertooth motor controller."""
    try:
        # Ensure command is sent as a single byte
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")  # Show command in hex for clarity
    except Exception as e:
        print(f"Failed to send command: {e}")

# Initialize pygame for GUI
pygame.init()
screen = pygame.display.set_mode((300, 300))  # Create a window
pygame.display.set_caption("Motor Control")

# Define colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0) 

# Define button properties
button_width = 80
button_height = 80
button_margin = 20

# Create rectangles for buttons
w_button = pygame.Rect(110, 40, button_width, button_height)
a_button = pygame.Rect(40, 110, button_width, button_height)
s_button = pygame.Rect(110, 110, button_width, button_height)
d_button = pygame.Rect(180, 110, button_width, button_height)

# Main loop for GUI
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position
                pos = pygame.mouse.get_pos()
                
                # Check if buttons were clicked
                if w_button.collidepoint(pos):
                    send_command(64 + 43)  # Move motor 1 forward
                    send_command(192 + 43)  # Move motor 2 forward
                elif s_button.collidepoint(pos):
                    send_command(64 - 43)  # Move motor 1 backward
                    send_command(192 - 43)  # Move motor 2 backward
                elif a_button.collidepoint(pos):
                    send_command(64 + 43)  # Move motor 1 forward
                    send_command(192 - 43)  # Move motor 2 backward
                elif d_button.collidepoint(pos):
                    send_command(64 - 43)  # Move motor 1 backward
                    send_command(192 + 43)  # Move motor 2 forward

        # Draw buttons
        screen.fill(WHITE)  # Fill background with white
        pygame.draw.rect(screen, GRAY, w_button)
        pygame.draw.rect(screen, GRAY, a_button)
        pygame.draw.rect(screen, GRAY, s_button)
        pygame.draw.rect(screen, GRAY, d_button)

        # Add text labels
        font = pygame.font.Font(None, 36)
        text_w = font.render('W', True, RED)
        text_a = font.render('A', True, RED)
        text_s = font.render('S', True, RED)
        text_d = font.render('D', True, RED)

        screen.blit(text_w, (w_button.centerx - 10, w_button.centery - 20))
        screen.blit(text_a, (a_button.centerx - 10, a_button.centery - 20))
        screen.blit(text_s, (s_button.centerx - 10, s_button.centery - 20))
        screen.blit(text_d, (d_button.centerx - 10, d_button.centery - 20))

        pygame.display.flip()  # Update the display
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

