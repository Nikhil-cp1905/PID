import time
import pygame
import serial

try:
    ser = serial.Serial('/dev/pts/2', 9600, timeout=1)
    print(f"Connected to {ser.portstr}")
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    try:
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")
    except Exception as e:
        print(f"Failed to send command: {e}")

pygame.init()
screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("Motor Control")

running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            send_command(64 + 43)
            send_command(192 + 43)
        elif keys[pygame.K_s]:
            send_command(64 - 43)
            send_command(192 - 43)
        elif keys[pygame.K_a]:
            send_command(64 + 43)
            send_command(192 - 43)
        elif keys[pygame.K_d]:
            send_command(64 - 43)
            send_command(192 + 43)
        else:
            send_command(64)
            send_command(192)

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
finally:
    send_command(64)
    send_command(192)
    ser.close()
    print("Serial connection closed.")
    pygame.quit()

