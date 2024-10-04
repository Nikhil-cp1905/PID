import serial
import time

# Serial port configuration
serial_port = "/dev/ttyUSB0"  # Replace with your actual serial port
baud_rate = 9600

# Sabertooth 2x60 parameters
address = 130  # Adjust the address as needed
command_drive_forward = 0
command_drive_backward = 1
command_min_voltage = 2
command_max_voltage = 3
command_drive_forward_motor2 = 4
command_drive_backward_motor2 = 5
command_drive_motor1_7bit = 6
command_drive_motor2_7bit = 7
command_drive_forward_mixed_mode = 8
command_drive_backward_mixed_mode = 9
command_turn_right_mixed_mode = 10
command_turn_left_mixed_mode = 11
command_drive_forwards_back_7bit = 12
command_turn_7bit = 13
command_serial_timeout = 14
command_baud_rate = 15
command_ramping = 16
command_deadband = 17

# Function to send a packet
def send_packet(command, data):
    checksum = (address + command + data) & 0x7F
    packet = f"{address:02X} {command:02X} {data:02X} {checksum:02X}\n"
    ser.write(packet.encode())

# Example usage: Drive motor 1 forward at 50% speed
def drive_motor1_forward(speed):
    send_packet(command_drive_forward, speed)

# Example usage: Set minimum voltage to 8V
def set_min_voltage(voltage):
    data = int((voltage - 6) * 5)
    send_packet(command_min_voltage, data)

# ... Add more functions for other commands

if __name__ == "__main__":
    try:
        ser = serial.Serial(serial_port, baud_rate)
        print("Serial port opened successfully")

        # Example usage: Drive motor 1 forward at 50% speed
        drive_motor1_forward(64)

        # ... Add more commands as needed

        ser.close()
        print("Serial port closed")
    except serial.SerialException as e:
        print("Error opening serial port:", e)
